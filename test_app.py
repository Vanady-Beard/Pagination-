import unittest
from app import app, db
from flask_jwt_extended import create_access_token

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_login(self):
        response = self.app.post('/login', json={
            'username': 'admin',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 200)

    def test_get_orders_unauthorized(self):
        response = self.app.get('/orders')
        self.assertEqual(response.status_code, 401)

    def test_get_orders_authorized(self):
        with app.app_context():
            access_token = create_access_token(identity={'username': 'admin'})
            headers = {
                'Authorization': f'Bearer {access_token}'
            }
            response = self.app.get('/orders', headers=headers)
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

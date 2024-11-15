import unittest
from app import app, db
from models import User, Item

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_hello_world(self):
        response = self.app.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, World!', response.data)

    def test_create_item(self):
        response = self.app.post('/items', json={"name": "Item 1", "description": "Description 1"})
        self.assertEqual(response.status_code, 201)
        self.assertIn(b"Item created", response.data)

    def test_create_user_and_login(self):
        user = User(name="Admin", email="admin@example.com", password="password")
        db.session.add(user)
        db.session.commit()
        
        response = self.app.post('/login', json={"email": "admin@example.com", "password": "password"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"token", response.data)

if __name__ == '__main__':
    unittest.main()

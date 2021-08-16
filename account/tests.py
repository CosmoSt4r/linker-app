from django.test import TestCase
from django.urls import reverse

class SignupViewTests(TestCase):
    
    def test_get(self):
        response = self.client.get('/account/signup/')
        self.assertEqual(response.status_code, 200)

    def test_auto_redirect(self):
        self.assertRedirects(self.client.get('/account/signup'), 
                            '/account/signup/', 
                            status_code=301)

    def test_reverse(self):
        url = reverse('account:signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_username_error(self):
        data = {"username" : "user", 
                "password" : "password",
                "confirm-password" : "password"}
        response = self.client.post('/account/signup/', data=data)
        self.assertContains(response, "Username must be from")  # username length error

    def test_user_create(self):
        data = {"username" : "testuser", 
                "password" : "testpassword",
                "confirm-password" : "testpassword"}
        response = self.client.post('/account/signup/', data=data)
        self.assertEqual(response.status_code, 200)

    def test_username_exists(self):
        data = {"username" : "testuser", 
                "password" : "testpassword",
                "confirm-password" : "testpassword"}
        response = self.client.post('/account/signup/', data=data)
        self.assertContains(response, "Username already exists")

    def test_password_error(self):
        data = {"username" : "user", 
                "password" : "pass",
                "confirm-password" : "pass2"}
        response = self.client.post('/account/signup/', data=data)
        self.assertContains(response, "Password must contain")  # password length error
        self.assertContains(response, "Passwords are")  # passwords matching error

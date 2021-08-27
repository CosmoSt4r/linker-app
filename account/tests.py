from django.test import TestCase
from django.urls import reverse


class BaseViewTests(TestCase):
    def test_get(self):
        self.assertRedirects(
            self.client.get("/account/"), "/account/login/", status_code=302
        )


class SignupViewTests(TestCase):
    def test_get(self):
        response = self.client.get("/account/signup/")
        self.assertEqual(response.status_code, 200)

    def test_auto_redirect(self):
        self.assertRedirects(
            self.client.get("/account/signup"), "/account/signup/", status_code=301
        )

    def test_reverse(self):
        url = reverse("account:signup")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_field_length_error(self):
        data = {"username": "user", "password": "pass", "confirm_password": "pass"}
        response = self.client.post("/account/signup/", data=data)
        self.assertContains(response, "Ensure this value has at least 8 characters", 3)

    def test_user_create(self):
        data = {
            "username": "testuser",
            "password": "testpassword",
            "confirm_password": "testpassword",
        }
        response = self.client.post("/account/signup/", data=data)
        self.assertEqual(response.status_code, 302)

    def test_password_error(self):
        data = {
            "username": "username",
            "password": "password1",
            "confirm_password": "password2",
        }
        response = self.client.post("/account/signup/", data=data)
        self.assertContains(response, "Passwords are not matching")


class LoginViewTests(TestCase):
    def test_get(self):
        response = self.client.get("/account/login/")
        self.assertEqual(response.status_code, 200)

    def test_auto_redirect(self):
        self.assertRedirects(
            self.client.get("/account/login"), "/account/login/", status_code=301
        )

    def test_reverse(self):
        url = reverse("account:login")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_field_length_error(self):
        data = {"username": "user", "password": "pass"}
        response = self.client.post("/account/login/", data=data)
        self.assertContains(response, "Ensure this value has at least 8 characters", 2)

    def test_user_login_error(self):
        data = {"username": "testuser", "password": "testpassword"}
        response = self.client.post("/account/login/", data=data)
        self.assertContains(response, "Username or password is invalid")

    def test_user_login(self):
        data = {
            "username": "username",
            "password": "password",
            "confirm_password": "password",
        }
        self.assertRedirects(
            self.client.post("/account/signup/", data=data), "/account/home/", 302
        )
        self.assertRedirects(
            self.client.get("/account/logout/"), "/account/login/", 302
        )
        self.assertRedirects(
            self.client.post("/account/login/", data=data), "/account/home/", 302
        )


class LogoutViewTest(TestCase):
    def test_logout(self):
        data = {
            "username": "testuser",
            "password": "testpassword",
            "confirm_password": "testpassword",
        }

        self.assertRedirects(
            self.client.post("/account/signup/", data=data), "/account/home/", 302
        )
        self.assertRedirects(
            self.client.get("/account/logout/"), "/account/login/", 302
        )

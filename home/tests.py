from django.test import TestCase


class BaseViewTest(TestCase):
    data = {
        "username": "username",
        "password": "password",
        "confirm_password": "password",
    }

    def test_get(self):
        self.assertRedirects(
            self.client.post("/account/signup/", data=self.data), "/account/home/", 302
        )
        self.assertRedirects(self.client.get("/account/home"), "/account/home/", 301)

    def test_account_redirect(self):
        self.assertRedirects(
            self.client.post("/account/signup/", data=self.data), "/account/home/", 302
        )

        self.assertRedirects(self.client.get("/account/login/"), "/account/home/", 302)
        self.assertRedirects(self.client.get("/account/signup/"), "/account/home/", 302)


class MainViewTest(TestCase):
    data = {
        "username": "username",
        "password": "password",
        "confirm_password": "password",
    }

    def test_get(self):
        self.assertRedirects(
            self.client.post("/account/signup/", data=self.data), "/account/home/", 302
        )
        self.assertEqual(self.client.get("/account/home/").status_code, 200)

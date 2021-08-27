from django.test import TestCase


class MainViewTest(TestCase):
    def test_get(self):
        self.assertEquals(self.client.get("").status_code, 200)

    def test_search(self):
        self.assertEquals(
            self.client.post("", data={"username": "username"}).status_code, 200
        )


class UserViewTest(TestCase):
    data = {
        "username": "username",
        "password": "password",
        "confirm_password": "password",
    }

    def test_get(self):
        self.assertEquals(self.client.get("/username/").status_code, 404)

    def test_user_page(self):
        self.assertRedirects(
            self.client.post("/account/signup/", data=self.data), "/account/home/", 302
        )
        self.assertEquals(self.client.get("/username/").status_code, 200)
        self.assertContains(self.client.get("/username/"), "username")

    def test_search_user(self):
        self.assertRedirects(
            self.client.post("/account/signup/", data=self.data), "/account/home/", 302
        )
        self.assertRedirects(
            self.client.post("/", data={"username": "username"}), "/username/", 302
        )

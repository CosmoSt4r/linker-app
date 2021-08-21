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

    def test_add(self):
        self.assertRedirects(
            self.client.post("/account/signup/", data=self.data), "/account/home/", 302
        )
        self.assertEqual(self.client.get("/account/home/add/").status_code, 200)
        data = {"title": "title", "url": "url"}
        self.assertRedirects(
            self.client.post("/account/home/add/", data=data), "/account/home/add/", 302
        )

    def test_edit(self):
        self.assertRedirects(
            self.client.post("/account/signup/", data=self.data), "/account/home/", 302
        )
        data = {"title": "title", "url": "url"}
        self.assertRedirects(
            self.client.post("/account/home/add/", data=data), "/account/home/add/", 302
        )
        self.assertEqual(self.client.get("/account/home/edit/").status_code, 200)
        self.assertEqual(self.client.get("/account/home/edit/1/").status_code, 200)
        data = {"title": "title2", "url": "url2", "submit": True}
        self.assertRedirects(
            self.client.post("/account/home/edit/1/", data=data),
            "/account/home/edit/",
            302,
        )
        self.assertContains(self.client.get("/account/home/"), "url2")

    def test_delete(self):
        self.assertRedirects(
            self.client.post("/account/signup/", data=self.data), "/account/home/", 302
        )
        data = {"title": "title", "url": "url"}
        self.assertRedirects(
            self.client.post("/account/home/add/", data=data), "/account/home/add/", 302
        )
        self.assertRedirects(
            self.client.post("/account/home/delete/1/", data={"submit": True}),
            "/account/home/edit/",
            302,
        )
        self.assertNotContains(self.client.get("/account/home/"), "url")

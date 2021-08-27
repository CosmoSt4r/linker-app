from django.test import TestCase
from .models import QRCode


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
        data = {"title": "title", "text": "text"}
        self.assertRedirects(
            self.client.post("/account/home/add/", data=data), "/account/home/add/", 302
        )
        self.assertTrue(QRCode.objects.filter(title='title').exists())
        self.assertEquals(QRCode.objects.filter(title='title').get().get_absolute_url(),
        '/account/home/edit/1/')

    def test_edit(self):
        self.assertRedirects(
            self.client.post("/account/signup/", data=self.data), "/account/home/", 302
        )
        self.assertEqual(self.client.get("/account/edit/1/").status_code, 404)
        data = {"title": "title", "text": "text"}
        self.assertRedirects(
            self.client.post("/account/home/add/", data=data), "/account/home/add/", 302
        )
        self.assertEqual(self.client.get("/account/home/edit/").status_code, 200)
        self.assertEqual(self.client.get("/account/home/edit/1/").status_code, 200)
        data = {"title": "title2", "text": "text2", "submit": True}
        self.assertRedirects(
            self.client.post("/account/home/edit/1/", data=data),
            "/account/home/edit/",
            302,
        )
        self.assertContains(self.client.get("/account/home/"), "text2")

    def test_delete(self):
        self.assertRedirects(
            self.client.post("/account/signup/", data=self.data), "/account/home/", 302
        )
        self.assertEqual(self.client.get("/account/delete/1/").status_code, 404)
        data = {"title": "title", "text": "text"}
        self.assertRedirects(
            self.client.post("/account/home/add/", data=data), "/account/home/add/", 302
        )
        self.assertRedirects(
            self.client.post("/account/home/delete/1/", data={"delete": True}),
            "/account/home/edit/",
            302,
        )
        self.assertNotContains(self.client.get("/account/home/"), "text")

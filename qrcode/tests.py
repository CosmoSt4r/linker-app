from django.test import TestCase
from .models import QRCode


class MainViewTest(TestCase):
    data = {
        "username": "username",
        "password": "password",
        "confirm_password": "password",
    }

    def test_add(self):
        self.assertRedirects(
            self.client.post("/account/signup/", data=self.data), "/account/home/", 302
        )
        self.assertEqual(self.client.get("/code/add/").status_code, 200)
        data = {"title": "title", "text": "text"}
        self.assertRedirects(
            self.client.post("/code/add/", data=data), "/code/add/", 302
        )
        self.assertTrue(QRCode.objects.filter(title="title").exists())
        self.assertEquals(
            QRCode.objects.filter(title="title").get().get_absolute_url(),
            "/code/edit/2/",
        )

    def test_edit(self):
        self.assertRedirects(
            self.client.post("/account/signup/", data=self.data), "/account/home/", 302
        )
        self.assertEqual(self.client.get("/code/edit/1/").status_code, 404)
        data = {"title": "title", "text": "text"}
        self.assertRedirects(
            self.client.post("/code/add/", data=data), "/code/add/", 302
        )
        self.assertEqual(self.client.get("/account/home/edit/").status_code, 200)
        self.assertEqual(self.client.get("/code/edit/2/").status_code, 200)
        data = {"title": "title2", "text": "text2", "submit": True}
        self.assertRedirects(
            self.client.post("/code/edit/2/", data=data),
            "/account/home/edit/",
            302,
        )
        self.assertContains(self.client.get("/account/home/"), "text2")

    def test_delete(self):
        self.assertRedirects(
            self.client.post("/account/signup/", data=self.data), "/account/home/", 302
        )
        self.assertEqual(self.client.get("/code/delete/2/").status_code, 404)
        data = {"title": "title", "text": "text"}
        self.assertRedirects(
            self.client.post("/code/add/", data=data), "/code/add/", 302
        )
        self.assertRedirects(
            self.client.post("/code/delete/2/", data={"delete": True}),
            "/account/home/edit/",
            302,
        )
        self.assertNotContains(self.client.get("/account/home/"), "text")

    def test_show_get(self):
        self.assertRedirects(
            self.client.post("/account/signup/", data=self.data), "/account/home/", 302
        )
        self.assertEqual(self.client.get("/code/show/1/").status_code, 200)

    def test_show_post(self):
        self.assertRedirects(
            self.client.post("/account/signup/", data=self.data), "/account/home/", 302
        )
        self.assertEqual(self.client.post("/code/show/1/").status_code, 200)

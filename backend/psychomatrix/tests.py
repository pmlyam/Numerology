from django.urls import reverse
from rest_framework import status
from django.test import TestCase


class SquareAPITestCase(TestCase):
    date = "11.11.2005"
    url = reverse("square")

    def test_post(self):
        response = self.client.post(self.url, data={"date": self.date}, content_type="application/json")
        # self.assertEqual(status.HTTP_200_OK, response.status_code)

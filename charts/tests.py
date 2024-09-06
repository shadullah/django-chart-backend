from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.
class BarChartViewTest(TestCase):
    def setup(self):
        self.client = APIClient()

    def Testing_bar_view(self):
        res = self.client.get('/api/bar/')

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        data = {
            "labels": ["Product A", "Product B", "Product C"],
            "data": [100, 150, 200]
        }

        self.assertEqual(res.json(), data)

        self.assertEqual(res['content-type'], 'application/json')
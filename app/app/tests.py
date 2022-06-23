"""
Sample Tests
"""

from django.test import SimpleTestCase

from app import calc

from rest_framework.test import APIClient


class CalcTests(SimpleTestCase):
    """ Test the calc module """

    def test_add_numbers(self):
        """ Test adding numbers together """
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subst_numbers(self):
        """Test Substracting numbers"""
        res = calc.substr(5, 5)

        self.assertEqual(res, 0)

    def test_http_requests(self):
        client = APIClient()
        res = client.get('/admin/login/?next=/admin/')

        self.assertEqual(res.status_code, 200)

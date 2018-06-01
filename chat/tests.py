from django.http import Http404
from django.test import TestCase, Client


class ViewTest(TestCase):

    def testView(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)

        response = c.get('/chat/')
        self.assertEqual(response.status_code, 200)

        response = c.get('/chat/lobby/')
        self.assertEqual(response.status_code, 200)
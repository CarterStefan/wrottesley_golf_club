from django.test import TestCase, SimpleTestCase

# Create your tests here.


class HomepageTest(SimpleTestCase):
    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertEqual(response.status_code, 200)


class HomepageTemplateTest(SimpleTestCase):
    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home/index.html')

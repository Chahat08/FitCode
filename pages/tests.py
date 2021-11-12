# pages tests

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView
# Create your tests here.

class HomepageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_base_template(self):
        self.assertTemplateUsed(self.response, '_base.html')

    def test_homepage_contains_html(self):
        self.assertContains(self.response, 'Home')

    def test_homepage_doesnt_contain_html(self):
        self.assertNotContains(self.response, 'blah')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
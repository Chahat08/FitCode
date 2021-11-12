#accounts/tests.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from .views import SignupPageView

# Create your tests here.

class CustomUserTests(TestCase):

    def test_create_user(self):

        User = get_user_model()
        user = User.objects.create_user(
            username='abc',
            email='abc123@email.com',
            password='testpass123'
            )

        self.assertEqual(user.username, 'abc')
        self.assertEqual(user.email, 'abc123@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='super',
            email='superuser@email.com',
            password='notreallysuper'
            )

        self.assertEqual(admin_user.username, 'super')
        self.assertEqual(admin_user.email, 'superuser@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_staff)

class SignupPageTests(TestCase):

    username='newuser'
    email='newuser@email.com'


    def setUp(self):
        url=reverse('signup')
        self.response=self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Sign Up')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
        self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
        [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()
        [0].email, self.email)


    def test_signup_view(self):
        view=resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)
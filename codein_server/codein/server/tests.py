'''
test server Models
--------------------------------
'''

from django.test import TestCase
from .models import User
from .serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory


class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        User.objects.create(username='zee', password='top_secret', email='zee@aol.com',
                            developer=2, python=True, is_staff=False, is_active=True,
                            date_joined='2018-04-18')

    def test_returned_username(self):
        shortname = User(username="zeeno")
        self.assertEqual(str(shortname), shortname.username)

'''
test server Serializers
--------------------------------
'''




'''
test server Views
--------------------------------
'''


class HomePageTests(TestCase):

    """ Test LOGIN + REGISTRATION """

    def setUp(self):
        self.user = get_user_model().objects.create(username='some_user')

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)











'''
test server API
--------------------------------
'''
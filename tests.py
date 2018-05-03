'''
test server Models
--------------------------------
'''

from .models import User
from django.contrib.auth import get_user_model
from .views import UserViewset
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_jwt import utils, views
from rest_framework_jwt.compat import get_user_model

User = get_user_model()


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
        self.client = APIClient()
        view = UserViewset
        self.email = 'some_user@gmail.com'
        self.username = 'some_user'
        self.password = 'top_secret'
        self.user = get_user_model().objects.create(username='some_user',password='top_secret', email='some_user@gmail.com')
        self.user.save()

        self.data = {'username': self.username, 'password': self.password}

    def test_jwt_login_using_zero(self):

            client = APIClient(enforce_csrf_checks=True)

            data = {
                'username': '0',
                'password': '0'
            }

            response = client.post('/rest-auth/login/', data, format='json')

            self.assertEqual(response.status_code, 400)

    def test_jwt_login_json_missing_fields(self):
            """
            Ensure JWT login view using JSON POST fails if missing fields.
            """
            client = APIClient(enforce_csrf_checks=True)

            response = client.post('/rest-auth/login/',
                                   {'username': self.username}, format='json')

            self.assertEqual(response.status_code, 400)

    def test_jwt_login_json(self):
            """
            Ensure JWT login view using JSON POST works.
            """
            client = APIClient(enforce_csrf_checks=True)

            response = client.post('/rest-auth/login/', self.data, format='json')

            response_content = str(response.content, encoding='utf8')

            decoded_payload = utils.jwt_decode_handler(response_content['token'])

            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(decoded_payload['username'], self.username)

    def test_jwt_login_json_bad_creds(self):
            """
            Ensure JWT login view using JSON POST fails
            if bad credentials are used.
            """
            client = APIClient(enforce_csrf_checks=True)

            self.data['password'] = 'wrong'
            response = client.post('/rest-auth/login/', self.user)

            self.assertEqual(response.status_code, 400)

    
    def test_jwt_login_form(self):
            """
            Ensure JWT login view using form POST works.
            """
            client = APIClient(enforce_csrf_checks=True)

            response = client.post('/rest-auth/login/', self.data)

            #decoded_payload = utils.jwt_decode_handler(response.data['Jwttoken'])

            self.assertEqual(response.status_code, status.HTTP_200_OK)
            #self.assertEqual(decoded_payload['username'], self.username)



    def test_jwt_login_with_expired_token(self):
            """
            Ensure JWT login view works even if expired token is provided
            """
            payload = utils.jwt_payload_handler(self.user)
            payload['exp'] = 1
            token = utils.jwt_encode_handler(payload)

            auth = 'JWT {0}'.format(token)
            client = APIClient(enforce_csrf_checks=True)
            response = client.post(
                '/auth-token/', self.data,
                HTTP_AUTHORIZATION=auth)

            decoded_payload = utils.jwt_decode_handler(response.data['token'])

            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(decoded_payload['username'], self.username)

    


    def test_get_token(self):
        response = self.client.post("/auth/api/get_token/", {"username": "Heffalumps", "password": "Woozles"})
        self.assertEqual(response.status_code, 200, "The token should be successfully returned.")

        response_content = json.loads(response.content.decode('utf-8'))
        token = response_content["token"]

        # The following request fails
        response = self.client.post("/auth/api/authenticated/", {}, Authorization='JWT ' + token)
        response_content = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response_content["authenticated"], "mooh", "The user should be able to access this endpoint.")
    




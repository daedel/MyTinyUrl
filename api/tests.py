import re
from unittest.mock import patch

from django.http import HttpResponseRedirect
from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_404_NOT_FOUND, \
    HTTP_302_FOUND
from rest_framework.test import APIClient

from api.models import TinyUrl
from api.utils import ensure_https_prefix, generate_url_for_redirection


# Create your tests here.

class TinyUrlTests(TestCase):

    def test_ensure_https_prefix_has_correct_prefix_when_url_dont_have_prefix(self) -> None:
        url = 'www.google.pl'
        self.assertEquals('https://www.google.pl', ensure_https_prefix(url))

    def test_ensure_https_prefix_has_correct_prefix_when_url_have_prefix(self) -> None:
        url = 'https://www.google.pl'
        self.assertEquals('https://www.google.pl', ensure_https_prefix(url))

    @patch('api.utils.CONFIG')
    def test_generate_url_for_redirection(self, config_mock) -> None:
        config_mock.HOST = 'test_env.com'
        code = '432ty'
        self.assertEquals(f'test_env.com/{code}', generate_url_for_redirection(code))


class TinyUrlViewTests(TestCase):

    def setUp(self) -> None:
        self.api_client = APIClient()

    def test_creating_tiny_url_with_correct_params(self) -> None:
        url = reverse('tiny_url-create-tiny-url')
        response = self.api_client.post(url, data={'url': 'www.google.pl'})

        self.assertEquals(HTTP_201_CREATED, response.status_code)
        self.assertTrue(re.match('localhost:8000/[a-z0-9]{5}', response.json()))

    def test_creating_tiny_url_with_empty_url(self) -> None:
        url = reverse('tiny_url-create-tiny-url')
        response = self.api_client.post(url, data={'url': ''})

        self.assertEquals(HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEquals({'url': ['This field may not be blank.']}, response.json())

    def test_creating_tiny_url_without_payload(self) -> None:
        url = reverse('tiny_url-create-tiny-url')
        response = self.api_client.post(url)

        self.assertEquals(HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEquals({'url': ['This field is required.']}, response.json())

    def test_get_original_url_from_code(self) -> None:
        tiny_url = TinyUrl.objects.create(url='www.google.pl')
        url = reverse('tiny_url-reverse', kwargs={'code': tiny_url.code})
        response = self.api_client.get(url)

        self.assertEquals(HTTP_200_OK, response.status_code)
        self.assertEquals(tiny_url.url, response.json())

    def test_get_original_url_from_non_existing_code(self) -> None:
        url = reverse('tiny_url-reverse', kwargs={'code': '1234'})
        response = self.api_client.get(url)

        self.assertEquals(HTTP_404_NOT_FOUND, response.status_code)
        self.assertEquals({'detail': 'Not found.'}, response.json())

    def test_redirection_for_returned_url(self) -> None:
        tiny_url = TinyUrl.objects.create(url='https://www.google.pl')
        url = reverse('redirection', kwargs={'code': tiny_url.code})
        print(url)
        response = self.api_client.get(url)

        self.assertEquals(HTTP_302_FOUND, response.status_code)
        self.assertEquals(tiny_url.url, response.url)

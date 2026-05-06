from datetime import datetime
from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from .models import Booking, Menu


class MenuModelTest(TestCase):
    def test_str_returns_name_and_price(self):
        item = Menu.objects.create(name='Bruschetta', price=Decimal('5.50'), description='Toasted bread')
        self.assertEqual(str(item), 'Bruschetta : 5.50')


class MenuApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(name='Greek Salad', price=Decimal('8.99'), description='Fresh and crisp')
        Menu.objects.create(name='Lemon Tart', price=Decimal('4.25'), description='House dessert')

    def test_list_returns_all_items(self):
        response = self.client.get(reverse('menu-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        names = sorted(item['name'] for item in response.data)
        self.assertEqual(names, ['Greek Salad', 'Lemon Tart'])

    def test_create_item(self):
        payload = {'name': 'Pasta', 'price': '12.50', 'description': 'Fresh pasta'}
        response = self.client.post(reverse('menu-list'), payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Menu.objects.filter(name='Pasta').exists())

    def test_retrieve_single_item(self):
        item = Menu.objects.first()
        response = self.client.get(reverse('menu-detail', args=[item.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], item.name)


class BookingApiAuthTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='alice', password='wonderland-99')
        self.token, _ = Token.objects.get_or_create(user=self.user)
        self.url = '/api/booking/tables/'

    def test_anonymous_request_is_rejected(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_request_succeeds(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_user_can_create_booking(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        payload = {
            'name': 'Birthday party',
            'no_of_guests': 4,
            'bookingdate': timezone.now().isoformat(),
        }
        response = self.client.post(self.url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)


class StaticHomepageTest(TestCase):
    def test_homepage_renders(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Little')

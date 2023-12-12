import uuid
from django.utils import timezone

from django.urls import reverse
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.test import TestCase

from base.models import Artisan, Customer, Material, Order


class ArtisanTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_artisan(self):
        url = reverse('createArtisan')
        data = {
            'name': 'Test Artisan',
            'surname': 'Test Surname',
            'address': 'Test Address',
            'phone_number': '1234567890',
            'email': 'test@example.com',
            'specialization': 'Test Specialization',
            'salary': '1000.00',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Artisan.objects.count(), 1)
        self.assertEqual(Artisan.objects.get().name, 'Test Artisan')

    def test_delete_artisan(self):
        artisan = Artisan.objects.create(
            name='Test Artisan',
            surname='Test Surname',
            address='Test Address',
            phone_number='1234567890',
            email='test@example.com',
            specialization='Test Specialization',
            salary='1000.00'
        )
        url = reverse('deleteArtisan', args=[str(artisan.artisan_id)])

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Artisan.objects.count(), 0)

    def test_get_artisan_detail(self):
        artisan = Artisan.objects.create(
            name='Test Artisan',
            surname='Test Surname',
            address='Test Address',
            phone_number='1234567890',
            email='test@example.com',
            specialization='Test Specialization',
            salary='1000.00'
        )
        url = reverse('getArtisan', args=[str(artisan.artisan_id)])

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Artisan')

    def test_update_artisan(self):
        artisan = Artisan.objects.create(
            name='Test Artisan',
            surname='Test Surname',
            address='Test Address',
            phone_number='1234567890',
            email='test@example.com',
            specialization='Test Specialization',
            salary='1000.00'
        )
        url = reverse('updateArtisan', args=[str(artisan.artisan_id)])
        data = {
            'name': 'Updated Artisan',
            'surname': 'Updated Surname',
            'address': 'Updated Address',
            'phone_number': '9876543210',
            'email': 'updated@example.com',
            'specialization': 'Updated Specialization',
            'salary': '1500.00',
        }

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Artisan.objects.get().name, 'Updated Artisan')

class CustomerTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_customer(self):
        url = reverse('createCustomer')
        data = {
            'name': 'Test Customer',
            'surname': 'Test Surname',
            'address': 'Test Address',
            'phone_number': '1234567890',
            'email': 'test@example.com',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().name, 'Test Customer')

    def test_delete_customer(self):
        customer = Customer.objects.create(
            name='Test Customer',
            surname='Test Surname',
            address='Test Address',
            phone_number='1234567890',
            email='test@example.com',
        )
        url = reverse('deleteCustomer', args=[str(customer.customer_id)])

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Customer.objects.count(), 0)

    def test_get_artisan_detail(self):
        customer = Customer.objects.create(
            name='Test Customer',
            surname='Test Surname',
            address='Test Address',
            phone_number='1234567890',
            email='test@example.com',
        )
        url = reverse('getCustomer', args=[str(customer.customer_id)])

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Customer')

    def test_update_customer(self):
        customer = Customer.objects.create(
            name='Test Customer',
            surname='Test Surname',
            address='Test Address',
            phone_number='1234567890',
            email='test@example.com',
        )
        url = reverse('updateCustomer', args=[str(customer.customer_id)])
        data = {
            'name': 'Updated Customer',
            'surname': 'Updated Surname',
            'address': 'Updated Address',
            'phone_number': '9876543210',
            'email': 'updated@example.com',
        }

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Customer.objects.get().name, 'Updated Customer')

class MaterialTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_material(self):
        url = reverse('createMaterial')
        data = {
            'name': 'Test Material',
            'description': 'Test Description',
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Material.objects.count(), 1)
        self.assertEqual(Material.objects.get().name, 'Test Material')

    def test_delete_material(self):
        material = Material.objects.create(
            name='Test Material',
            description='Test Description',
        )
        url = reverse('deleteMaterial', args=[str(material.material_id)])

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Material.objects.count(), 0)

    def test_get_material_detail(self):
        material = Material.objects.create(
            name='Test Material',
            description='Test Description',
        )
        url = reverse('getMaterial', args=[str(material.material_id)])

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Material')

    def test_update_material(self):
        material = Material.objects.create(
            name='Test Material',
            description='Test Description',
        )
        url = reverse('updateMaterial', args=[str(material.material_id)])
        data = {
            'name': 'Updated Material',
            'description': 'Updated Description',
        }

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Material.objects.get().name, 'Updated Material')
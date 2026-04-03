from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class BackendRESTTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_tarjeta_endpoint(self):
        # Verifica que el endpoint de tarjeta responde
        response = self.client.post('/visaAppWSBackendWSBackend/tarjeta/', {'numero': '1234'}, format='json')
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_404_NOT_FOUND])

    def test_pago_endpoint(self):
        # Verifica el registro de pago
        response = self.client.post('/visaAppWSBackendWSBackend/pago/', {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

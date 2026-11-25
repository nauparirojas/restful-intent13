from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Producto


class ProductoAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='Password123!')
        self.producto = Producto.objects.create(
            nombre='Teclado Mecánico',
            codigo='TEC-001',
            categoria='Periféricos',
            precio='180.00',
            stock=12,
            estado='activo',
        )

    def test_listar_productos_paginado_y_hateoas(self):
        url = reverse('producto-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)
        self.assertIn('_links', response.data['results'][0])

    def test_crear_producto_autenticado(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('producto-list')
        data = {
            'nombre': 'Mouse Óptico',
            'codigo': 'MOU-001',
            'categoria': 'Periféricos',
            'precio': '65.50',
            'stock': 5,
            'estado': 'activo',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['codigo'], 'MOU-001')

    def test_validacion_activo_sin_stock_falla(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('producto-list')
        data = {
            'nombre': 'Monitor 24',
            'codigo': 'MON-024',
            'categoria': 'Pantallas',
            'precio': '550.00',
            'stock': 0,
            'estado': 'activo',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
from rest_framework.test import APITestCase
from order import models
from user.models import UserModel
from product.models import ProductModel
from rest_framework.test import APIClient

class TestOrder(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = UserModel.objects.create_superuser(email='admin@mail.com', password='123')
        self.product = ProductModel.objects.create(name='test', content='test', price='1000')
        self.custom_user = UserModel.objects.create_user(email='test1@mail.com', password='test')

        self.client.login(email='admin@mail.com', password='123')
    
    def test_order_list(self):
        response = self.client.get('/api/v1/order/orders/')
        self.assertEqual(response.status_code, 200)

    def test_get_order(self):
        models.OrderModel.objects.create(
            product=self.product,
            count=10, free_count=1,
            customer=self.custom_user,
            longitude=1.0,
            latitude=1.0,
            status='created',
            product_price=10000,
            total_price=1000000,
            admin=self.user
        )
        response = self.client.get('/api/v1/order/order/1/')

        self.assertEqual(response.status_code, 200)
    
    def test_order_update(self):
        models.OrderModel.objects.update(
            product=self.product,
            count=10, free_count=1,
            customer=self.custom_user,
            longitude=1.0,
            latitude=1.0,
            status='created',
            product_price=100,
            total_price=100000,
            admin=self.user
        )
        response = self.client.patch('/api/v1/order/order/update/1/')
        self.assertEqual(response.status_code, 200)
from rest_framework.test import APITestCase
from order import models
from user.models import UserModel

# class TestOrder(APITestCase):
    
#     def test_order_list(self):
#         UserModel.objects.create_user(email='admin@gmail.com', password='123', is_staff=True)
#         self.client.login(email='admin@gmail.com', password='123')
#         response = self.client.get('/api/v1/orders/')
#         self.assertEqual(response.status_code, 200)

    # def test_order_get(self):
    #     UserModel.objects.create_user(email='admin@gmail.com', password='123', is_staff=True)
    #     self.client.login(email='admin@gmail.com', password='123')
    #     response = self.client.get('/api/v1/order/')
    #     self.assertEqual(response.status_code, 200)
    
    # def test_order_get(self):
    #     UserModel.objects.create_user(email='admin@gmail.com', password='123', is_staff=True)
    #     self.client.login(email='admin@gmail.com', password='123')
    #     response = self.client.get('/api/v1/order/update/')
    #     self.assertEqual(response.status_code, 200)
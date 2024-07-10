from rest_framework.test import APITestCase
from product import models
from user.models import UserModel

# class TestProduct(APITestCase):
#     def test_product_list(self):
#         UserModel.objects.create_user(email='admin@gmail.com', password='123', is_staff=True)
#         self.client.login(email='admin@gmail.com', password='123')
#         response = self.client.get('/api/v1/admin/product/products/')
#         self.assertEqual(response.status_code, 200)

#     def test_product_create(self):
#         UserModel.objects.create_user(email='admin@gmail.com', password='123', is_staff=True)
#         self.client.login(email='admin@gmail.com', password='123')
#         data = {
#             'name': 'Phone',
#             'content': 'asdasd',
#             'price': 123
#         }
#         response = self.client.post('/api/v1/admin/product/product/create/', data=data)
#         self.assertEqual(response.status_code, 201)



# class TestFreeProduct(APITestCase):
#     def test_product_list(self):
#         UserModel.objects.create_user(email='admin@gmail.com', password='123', is_staff=True)
#         self.client.login(email='admin@gmail.com', password='123')
#         response = self.client.get('/api/v1/admin/product/free-products/')
#         self.assertEqual(response.status_code, 200)

#     def test_product_create(self):
#         UserModel.objects.create_user(email='admin@gmail.com', password='123', is_staff=True)
#         self.client.login(email='admin@gmail.com', password='123')
#         data = {
#             'product': 1,
#             'count': '123',
#             'free_count': '123'
#         }
#         response = self.client.post('/api/v1/admin/product/free-product/create/', data=data)
#         self.assertEqual(response.status_code, 201)

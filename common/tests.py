from rest_framework.test import APITestCase
from common import models
from user.models import UserModel

# class TestSettings(APITestCase):
#     def test_settings_get(self):
#         UserModel.objects.create_user(email='admin@gmail.com', password='123', is_staff=True)
#         self.client.login(email='admin@gmail.com', password='123')
#         response = self.client.get('/api/v1/admin/settings/')
#         self.assertEqual(response.status_code, 200)

# class TestPage(APITestCase):
#     def test_settings_get(self):
#         UserModel.objects.create_user(email='admin@gmail.com', password='123', is_staff=True)
#         self.client.login(email='admin@gmail.com', password='123')
#         response = self.client.get('/api/v1/admin/pages/')
#         self.assertEqual(response.status_code, 200)

#     def test_settings_get(self):
#         UserModel.objects.create_user(email='admin@gmail.com', password='123', is_staff=True)
#         self.client.login(email='admin@gmail.com', password='123')
#         data = {
#             'slug': 'qwe',
#             'title': 'asd',
#             'content': 'asdada'
#         }
#         response = self.client.post('/api/v1/admin/page/create/', data=data)
#         self.assertEqual(response.status_code, 201) 

# class TestGallery(APITestCase):
#     def test_settings_get(self):
#         UserModel.objects.create_user(email='admin@gmail.com', password='123', is_staff=True)
#         self.client.login(email='admin@gmail.com', password='123')
#         response = self.client.get('/api/v1/admin/gallerys/')
#         self.assertEqual(response.status_code, 200)

#     def test_settings_get(self):
#         UserModel.objects.create_user(email='admin@gmail.com', password='123', is_staff=True)
#         self.client.login(email='admin@gmail.com', password='123')
#         data = {
            
#         }
#         response = self.client.post('/api/v1/admin/gallery/create/', data=data)
#         self.assertEqual(response.status_code, 201) 
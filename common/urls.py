from django.urls import path
from common import views

urlpatterns = [
    path('setting/', views.SettingsView.as_view()),
    path('gallery/', views.GalleryView.as_view()),
    path('page/', views.PageView.as_view()),
]
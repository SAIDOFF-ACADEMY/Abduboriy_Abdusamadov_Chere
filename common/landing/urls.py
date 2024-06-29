from django.urls import path
from common.landing import views

urlpatterns = [
    path('settings/', views.SettingsView.as_view()),
    path('gallerys/', views.GalleryView.as_view()),
    path('page/<str:slug>/', views.PageView.as_view()),
]
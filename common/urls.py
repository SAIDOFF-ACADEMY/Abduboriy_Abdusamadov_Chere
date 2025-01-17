from django.urls import include, path
from common import views

urlpatterns = [
    path('settings/', views.SettingsView.as_view()),
    path('pages/', views.PageView.as_view()),
    path('page/<int:slug>/', views.PageGetView.as_view()),
    path('page/delete/<int:slug>/', views.PageDeleteView.as_view()),
    path('page/update/<int:slug>/', views.PageUpdateView.as_view()),
    path('page/create/', views.PageCreateView.as_view()),
    path('gallerys/', views.GalleryView.as_view()),
    path('gallery/create/', views.GalleryCreateView.as_view()),
    path('gallery/delete/<int:pk>/', views.GalleryDeleteView.as_view()),
]

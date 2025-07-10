from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:category>/', views.category_news, name='category_news'),
    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
]

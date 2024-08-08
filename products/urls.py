from django.urls import path

from . import views


urlpatterns = [
    path('hello/', views.hello, name = 'hello'),
    path('productowners/', views.productsname , name = 'productowners' ),
]
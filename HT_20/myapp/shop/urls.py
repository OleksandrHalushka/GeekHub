from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category', views.category, name='category'),
    path('product', views.product, name='product'),
    path('login', views.log_in, name='login'),
    path('logout', views.log_out, name='logout'),
    path('delete', views.delete_product, name='delete'),
    path('edite', views.edite_product, name='edite'),
    path('buy', views.buy, name='buy'),
    path('basket', views.basket, name='basket')
]
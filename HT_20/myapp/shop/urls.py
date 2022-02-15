from django.urls import path, include

from . import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='products')

urlpatterns = [
    path('', views.index, name='index'),
    path('category', views.category, name='category'),
    path('product', views.product, name='product'),
    path('login', views.log_in, name='login'),
    path('logout', views.log_out, name='logout'),
    path('delete', views.delete_product, name='delete'),
    path('edite', views.edite_product, name='edite'),
    path('cart', views.cart, name='cart'),
    path('api/', include(router.urls), name='api')
]
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .forms import LoginForm
from django.contrib.auth.decorators import permission_required
from .serializer import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def index(request):
    is_logined = request.user.is_authenticated
    user = request.user
    categories = ('Technic', 'Mobile', 'Television')
    products = Product.objects.all()
    is_superuser = request.user.is_superuser
    context = {'authenticated': is_logined,
               'categories': categories,
               'user': user,
               'products': products,
               'super': is_superuser}
    return render(request, "index.html", context)


def category(request):
    category = request.GET.get('category')
    is_logined = request.user.is_authenticated
    user = request.user
    categories = ('Technic', 'Mobile', 'Television')
    products = Product.objects.all().filter(category=category)
    is_superuser = request.user.is_superuser
    context = {'authenticated': is_logined,
               'categories': categories,
               'user': user,
               'products': products,
               'super': is_superuser}
    return render(request, "index.html", context)


def product(request):
    product_id = request.GET.get('id')
    is_logined = request.user.is_authenticated
    user = request.user
    categories = ('Technic', 'Mobile', 'Television')
    products = Product.objects.all().filter(id=product_id)
    is_superuser = request.user.is_superuser
    context = {'authenticated': is_logined,
               'categories': categories,
               'user': user,
               'products': products,
               'super': is_superuser}
    return render(request, "product.html", context)


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'form': LoginForm(),
                                                  'error': 'Invalid login'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('index')


@permission_required('superuser', 'index')
def delete_product(request):
    product_id = request.GET.get('id')
    product = [Product.objects.all().filter(id=product_id)][0]
    product.delete()
    return redirect('index')


@permission_required('superuser', 'index')
def edite_product(request):
    product_id = request.GET.get('id')
    return redirect(f'/admin/shop/product/{product_id}/change/')


def cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        cart = request.session.setdefault('cart', {})
        if product_id:
            products = cart.setdefault('product', [])
            products.append(product_id)
            request.session.modified = True
        return JsonResponse({'products': request.session['cart']}, status=200)
    else:
        try:
            id_products = request.session['cart']['product']
        except:
            user = request.user
            return render(request, 'cart.html', {'message': 'Cart is empty', 'user': user})
        products = []
        for id in id_products:
            product = Product.objects.filter(id=id)[0]
            products.append(product)
        return render(request, 'cart.html', {'products': products})
from django.contrib.auth import login
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .forms import ProductForm
from django.contrib.auth.models import User
from .models import Product


def list_items(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, "inventory/list_items.html", context)


def view_item(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'profile': product}
    return render(request, "inventory/view_item.html", context)


def edit_item(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST or None, instance=product)
        if form.is_valid():
            form.save()
            context = {'product': product}
            return render(request, "inventory/view_item.html", context)
    else:
        form = Product(instance=product)
    context = {'product': product}
    return render(request, "inventory/edit_item.html", context)


def del_item(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    context = {'product': product}
    return render(request, "inventory/list_items.html", context)


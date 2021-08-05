from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request = request, template_name="inventory/home.html")

from django.shortcuts import render
from .models import product
# Create your views here.

def index(r):
    prd = product.objects.all()
    return render(r,'apiapp/index.html',{'prd':prd})

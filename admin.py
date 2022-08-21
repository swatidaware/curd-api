from django.contrib import admin
from .models import product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['qnty','name','price']

admin.site.register(product,ProductAdmin)
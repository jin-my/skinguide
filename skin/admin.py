from django.contrib import admin
from .models import Product, Photo

class PhotoInline(admin.TabularInline):
    model = Photo

class ProductAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]
# Register your models here.
admin.site.register(Product, ProductAdmin)
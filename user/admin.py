from django.contrib import admin
from .models import User
# Register your models here.
admin.site.register(User)

# from django.contrib import admin
# from .models import Product, Photo

# class ProductInline(admin.TabularInline):
#     model = Product

# class ProductAdmin(admin.ModelAdmin):
#     inlines = [ProductInline, ]
# # Register your models here.
# admin.site.register(User, ProductAdmin)
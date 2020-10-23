from django.contrib import admin
from .models import User
# Register your models here.
admin.site.register(User)

# from django.contrib import admin
# from .models import Product, Photo

# class ProductInline(admin.TabularInline):
#     model = Product

<<<<<<< HEAD
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductInline, ]
# Register your models here.
admin.site.register(User, ProductAdmin)
=======
# class ProductAdmin(admin.ModelAdmin):
#     inlines = [ProductInline, ]
# # Register your models here.
# admin.site.register(User, ProductAdmin)
>>>>>>> d6db616b558060b52154a2347acf3a97ccb0af1a

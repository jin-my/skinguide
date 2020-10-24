from django.db import models
# from user.models import User
from skinguide import settings
# Create your models here.

class Product(models.Model):
    # objects = models.Manager()
    title = models.CharField(max_length=150)
    brand = models.CharField(max_length=100, null = True)
    #image = models.ImageField(upload_to='images/',blank=True, null=True)
    # writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, related_name="write")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.IntegerField(null = True)
    skintype = models.CharField(max_length=5, null = True)
    categories = models.CharField(max_length=100, null = True)
    gender = models.CharField(max_length=2, null = True) #남/여 or M/F
    body = models.TextField()
    # example_choice = (
    #     ('S', 'Small'),
    #     ('M', 'Medium'),
    #     ('L', 'Large'),
    # )

    def __str__(self):
        return self.title
        # 제목으로 표시되게

class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

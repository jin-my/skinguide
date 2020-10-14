from django.db import models
from user.models import User
from skinguide import settings
# Create your models here.

class Product(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, related_name="write")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()
    # writer = models.ForeignKey('user.User', on_delete = models.CASCADE)

    def __str__(self):
        return self.title
        # 제목으로 표시되게
from django.db import models
import os


def add_image(instance,file_name):
    return os.path.join('gadget/media',instance.model, file_name)


# Create your models here.
class Gadgets(models.Model):
    CATEGORY = (
        ('SAMSUNG', 'SAMSUNG'),
        ('OPPO', 'OPPO'),
        ('REDMI', 'REDMI'),
        ('VIVO','VIVO')
    )
    id = models.IntegerField(primary_key=True)
    model = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY)
    picture = models.ImageField(upload_to=add_image)
    price = models.IntegerField()
    about = models.CharField(max_length=500)
    agree = models.BooleanField()
    upload_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)



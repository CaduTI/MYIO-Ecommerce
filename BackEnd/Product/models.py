import os

from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.SlugField
    name = models.CharField(max_length=255)
    type_product = models.CharField(default='V',
                                    max_length=1,
                                    choices=(
                                        ('V', 'variation'),
                                        ('S', 'simple'),
                                    )
                                    )
    price = models.FloatField
    description = models.TextField
    image_product = models.ImageField(
        upload_to='product_images/%Y/%m/', blank=True, null=True)

    @staticmethod
    def resize_image(img, new, max_width=800):
        pass

    def save(img):
        pass

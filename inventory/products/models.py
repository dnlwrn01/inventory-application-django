from django.db import models
from users.models import Profile


class Product(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    product_description = models.TextField(max_length=500)
    product_unit = models.CharField(max_length=50)
    product_price = models.DecimalField(max_digits=999, decimal_places=2)
    product_quantity = models.DecimalField(max_digits=999, decimal_places=2)
    product_status = models.BooleanField()
    product_details = models.TextField(max_length=500)
    product_category = models.CharField(max_length=50)
    product_sku = models.DecimalField(max_digits=999999, decimal_places=0, null=True)

    def __str__(self):
        return self.product_name

    objects = models.Manager()


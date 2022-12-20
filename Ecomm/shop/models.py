from django.db import models

# Create your models here.

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    publish_date=models.DateField()
    price=models.IntegerField()
    product_category=models.CharField(max_length=30,default="")
    image = models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name
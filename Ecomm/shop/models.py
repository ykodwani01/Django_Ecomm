from django.db import models

# Create your models here.

class Product(models.Model):
    product_id=models.IntegerField(default=1)
    product_name=models.CharField(max_length=50)
    publish_date=models.DateField()
    price=models.IntegerField()
    product_category=models.CharField(max_length=30,default="")
    image = models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name

class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000,null=True)
    name=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)

from django.db import models

# Create your models here.

class post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50,default="")
    publish_date=models.DateField()
    content=models.CharField(max_length=5000,default="")

    def __str__(self):
        return self.title



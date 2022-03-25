from tabnanny import verbose
from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    feedback = models.CharField(max_length=300)

    def __str__(self):
        self.disp_name = self.name
        return self.disp_name

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name

''''''
class Joinus(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    location = models.CharField(max_length=20)
    file = models.FileField(upload_to='shop/files', default="")
    subject = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = "Join Us"

    def __str__(self):
        self.disp_name = self.name
        return self.disp_name

class Orders(models.Model):
    ORDERSTATUS = (
        ("Ordered",'Ordered'),
        ("Preparing",'Preparing'),
        ("Ready",'Ready'),
        ("Completed",'Completed'),
    )
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    order_status = models.CharField(choices = ORDERSTATUS, default="Ordered", max_length=256)
    # address=models.CharField(max_length=111)
    # city=models.CharField(max_length=111)
    # state=models.CharField(max_length=111)
    # zip_code=models.CharField(max_length=111)
    last_modified=models.DateTimeField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)

    
from django.db import models

# Create your models here.

# prodect catogory


# customer models
class Customer (models.Model):
    name = models.CharField( max_length=100)
    phone = models.CharField( max_length=10)
    email = models.EmailField( max_length=50)

    def __str__(self) :
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=250, default="", blank=True, null=True)
    image = models.ImageField(upload_to="upload/product/")  # corrected the typo here

    def __str__(self):
        return self.product_name
    
    

    













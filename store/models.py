from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    detail = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    offer_price = models.CharField(max_length=100,blank=True, null=True)
    brand = models.CharField(max_length=100,blank=True, null=True)
    diamension = models.CharField(max_length=50,blank=True, null=True)
    material = models.ManyToManyField(Material)
    image1 = models.ImageField(upload_to= 'photos/products',null=True,blank=True)
    image2 = models.ImageField(upload_to= 'photos/products', null=True,blank=True)
    image3 = models.ImageField(upload_to= 'photos/products',null=True,blank=True)
    image4 = models.ImageField(upload_to= 'photos/products',null=True,blank=True)
    image5 = models.ImageField(upload_to= 'photos/products',null=True,blank=True)
    image6 = models.ImageField(upload_to= 'photos/products',null=True,blank=True)
    video_file = models.FileField(upload_to='videos/',null = True,blank=True)
    manufacturer = models.CharField(max_length= 200,blank=True, null=True)
    in_stock = models.BooleanField(default=False)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    # specific room type field - many to many
    # home page display --check

    def __str__(self):
        return self.name


# services

# interior stories

# clients page
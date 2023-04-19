from django.db import models

# Create your models here.
class Product(models.Model) :
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    size = models.CharField(max_length=30 , default=False)
    price = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True) 
    special_price = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,default=False)
    quantity = models.IntegerField(default=1, null=True,blank=True)
    instock = models.BooleanField(default=True)
    #file
    #picture = models.ImageField(upload_to='product',null=True,blank = True)
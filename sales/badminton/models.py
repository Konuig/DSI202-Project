from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.
class Product(models.Model) :
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    size = models.CharField(max_length=30 , default=False)
    price = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True) 
    special_price = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,default=False)
    quantity = models.IntegerField(default=1, null=True,blank=True)
    instock = models.BooleanField(default=True)
    #CHOICE
    class Type_racket_CHOICE(models.TextChoices) :
        POWER_RACKET = "Power racket"
        ALL_AROUND = "All around racket"
        SPEED = "Speed racket"

    type_racket = models.CharField(max_length=20,choices=Type_racket_CHOICE.choices,
                  default = Type_racket_CHOICE.ALL_AROUND )

    #file
    picture = models.ImageField(upload_to='product',null=True,blank = True)


class Profile(models.Model) :
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=5)

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class Order(models.Model) :
    profile = models.ForeignKey( Profile, on_delete=models.CASCADE)
    reciept = models.ImageField(upload_to='reciepts',null=True,blank = True)
    
    #CHOICE
    class STATUS(models.TextChoices) :
        UNAPPROVED = "รอการชำระเงิน"
        AAPPROVED = "ชำระเงินแล้ว"

    status = models.CharField(max_length=100,choices=STATUS.choices,default=STATUS.UNAPPROVED)
    def __str__(self) -> str:
        return self.pk

    order_at = models.DateTimeField(auto_now_add=True)

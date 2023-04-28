from django.contrib import admin
from .models import *

# Register your models here.
class BookProduct(admin.ModelAdmin):
    list_display = ('id','instock','title', 'description', 'size','price','special_price','type_racket')
    list_display_links = ('id',)
    list_editable = ('title',)
    list_filter = ('instock',)
    search_fields =('title',)
    

admin.site.register(Product,BookProduct)
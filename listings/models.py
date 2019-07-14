from django.db import models
from realtors.models import Realtor
from datetime import datetime
# Create your models here.


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete = models.DO_NOTHING)
    title = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    zipcode = models.CharField(max_length = 20)
    # description is optional. this is done by 'blank = True' part
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=3,decimal_places=1)
    # setting a defualt value of 0 for garage
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()    # sqft = squre feet
    # lot size is decimal with only one decimal places and 4 integer digit
    lot_size = models.DecimalField(max_digits=6,decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now,blank=True)

    ## for default property showing in admin area
    def __str__(self):
        return self.title

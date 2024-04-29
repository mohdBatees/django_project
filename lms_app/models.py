from pickle import TRUE
from random import choices
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Book(models.Model):


    status_book =[

        ('avaliable','avaliable'),
        ('rental','rental'),
        ('sold','sold'),
    ]


    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250,null=TRUE, blank = TRUE)
    photo_book = models.ImageField(upload_to='photos',null=TRUE, blank=True)
    photo_author = models.ImageField(upload_to='photos',null=TRUE, blank=True)
    pages = models.IntegerField(null=TRUE, blank = TRUE)
    price = models.DecimalField(max_digits=5 ,decimal_places=2,null=TRUE, blank = TRUE)
    rental_price_day = models.DecimalField(max_digits=5 ,decimal_places=2,null=TRUE, blank = TRUE)
    total_rental =models.DecimalField(max_digits=5 ,decimal_places=2,null=TRUE, blank = TRUE)
    rental_period = models.IntegerField(null=TRUE, blank = TRUE)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50,choices = status_book,null=TRUE, blank = TRUE)
    category = models.ForeignKey(Category,on_delete = models.PROTECT, null=TRUE, blank = TRUE)
def __str__(self):
        return self.title
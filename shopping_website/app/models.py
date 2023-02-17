from django.contrib.auth.models import User
from django.db import models

# Create your models here.
STATE_CHOICES=(('Nagaland','Nagaland'),
                ('Odisha','Odisha'),
                ('Punjab','Punjab'),
                ('Rajasthan','Rajasthan'),
                ('Sikkim','Sikkim'),
               ('Tripura','Tripura'),
               ('Uttarkhand','Uttarkhand'),
               ('Uttar Pradesh','Uttar Pradesh'))


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    name = models.CharField(max_length=264)
    locality = models.CharField(max_length=264)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def __str__(self):
        return self.name

CATEGORY_CHOICES=(
    ('M','Mobiles'),
    ('L','Laptop'),
    ('TV','Television'),
    ('WM','WashingMachine')
)


class Product(models.Model):
    title=models.CharField(max_length=250)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    brand=models.CharField(max_length=250)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    product_image=models.ImageField(upload_to='product_images')


    def __str__(self):
        return str(self.id)









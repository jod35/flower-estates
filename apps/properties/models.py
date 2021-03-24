from django.db import models
from django.contrib.auth.models import User


class House(models.Model):

    STATUS_CHOICES =(
        ('RENT','rent'),
        ('SALE','sale'),
    )
    
    name=models.CharField(max_length=25,null=False)
    price=models.IntegerField(null=False)
    bedrooms=models.IntegerField(null=False)
    garages=models.IntegerField(null=False)
    toilets=models.IntegerField(null=False)
    bathrooms=models.IntegerField(null=False)
    space=models.IntegerField(null=False)
    description=models.TextField(null=False)
    location=models.CharField(max_length=25,null=False)
    image1=models.ImageField(upload_to='houses',default='default.jpeg')
    image2=models.ImageField(upload_to='houses',default='default.jpeg')
    image3=models.ImageField(upload_to='houses',default='default.jpeg')
    image4=models.ImageField(upload_to='houses',default='default.jpeg')
    status=models.CharField(max_length=25,choices=STATUS_CHOICES,default='SALE')
    created=models.DateTimeField(auto_now_add=True)
    agent=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"<House {self.name}>"

class WareHouse(models.Model):
    STATUS_CHOICES =(
        ('RENT','rent'),
        ('SALE','sale'),
    )
    
    name=models.CharField(max_length=25,null=False)
    price=models.IntegerField(null=False)
    location=models.CharField(max_length=25,null=False)
    space=models.IntegerField(null=False)
    description=models.TextField(null=False)
    status=models.CharField(max_length=25,choices=STATUS_CHOICES,default='SALE')
    image1=models.ImageField(upload_to='houses',default='default.jpeg')
    image2=models.ImageField(upload_to='houses',default='default.jpeg')
    image3=models.ImageField(upload_to='houses',default='default.jpeg')
    image4=models.ImageField(upload_to='houses',default='default.jpeg')
    agent=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"<WareHouse {self.name}>"
 

class Land(models.Model):
    name = models.CharField(max_length=45)
    price=models.IntegerField(null=False)
    location=models.CharField(max_length=25,null=False)
    space =models.IntegerField(null=False)
    description = models.TextField(null=False)
    image1=models.ImageField(upload_to='houses',default='default.jpeg')
    image2=models.ImageField(upload_to='houses',default='default.jpeg')
    image3=models.ImageField(upload_to='houses',default='default.jpeg')
    image4=models.ImageField(upload_to='houses',default='default.jpeg')
    agent=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"<Land plot {self.name} >"

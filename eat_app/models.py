from django.db import models

# Create your models here.


class regimodel(models.Model):
    name=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField()
    psw=models.CharField(max_length=20)
    def __str__(self):
        return self.name +self.email

class profilmodel(models.Model):
    dishname = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.CharField(max_length=50)
    card = models.FileField(upload_to='eat_app/static')

    def __str__(self):
        return self.dishname + self.description

class cartmodel(models.Model):
    pro_id=models.IntegerField()
    dishname = models.CharField(max_length=30)
    price = models.IntegerField()
    # quantity = models.IntegerField()
    card = models.FileField(upload_to='eat_app/static')
    def __str__(self):
        return self.dishname

class adddetailsmodel(models.Model):
    fname=models.CharField(max_length=40)
    lname=models.CharField(max_length=40)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=50)
    def __str__(self):
        return self.fname + self.email

class paymentmodel(models.Model):
    num=models.IntegerField()
    expir=models.DateField()
    cvv=models.IntegerField()
    name=models.CharField(max_length=40)
    def __str__(self):
        return self.num + self.name

class grav(models.Model):
    gravyname=models.CharField(max_length=30)
    pri= models.IntegerField()
    des = models.CharField(max_length=50)
    im = models.FileField(upload_to='eat_app/static')
    def __str__(self):
        return self.gravyname + self.des

class rice(models.Model):
    ricename = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.CharField(max_length=50)
    img = models.FileField(upload_to='eat_app/static')
    def __str__(self):
        return self.ricename + self.description

class bfmodel(models.Model):
    bfname = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.CharField(max_length=50)
    img = models.FileField(upload_to='eat_app/static')
    def __str__(self):
        return self.bfname + self.description

class icemodel(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.CharField(max_length=50)
    img = models.FileField(upload_to='eat_app/static')
    def __str__(self):
        return self.name + self.description
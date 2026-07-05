from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    userType = models.CharField(max_length=29)


class Customer(models.Model):
    name = models.CharField(max_length=50)
    lname = models.CharField(max_length=50,null=True)
    contact = models.CharField(max_length=20)
    email = models.EmailField()
    district = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    pin = models.CharField(max_length=100,null=True)
    houseno = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=100,null=True)
    dob = models.DateField(null=True)   
    address = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status=models.BooleanField(default=True) 



class Content(models.Model):
    name = models.CharField(max_length=50)
    lname = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=20)
    email = models.EmailField()
    district = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    pin = models.CharField(max_length=100, null=True)
    houseno = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=100, null=True)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    

class MakeUp(models.Model):
    name = models.CharField(max_length=50)
    lname = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=20)
    email = models.EmailField()
    district = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    pin = models.CharField(max_length=100, null=True)
    houseno = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=100, null=True)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Photo(models.Model):
    name = models.CharField(max_length=50)
    lname = models.CharField(max_length=50, null=True)
    contact = models.CharField(max_length=20)
    email = models.EmailField()
    district = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    pin = models.CharField(max_length=100, null=True)
    houseno = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=100, null=True)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)



class Portfolio(models.Model):
    name = models.CharField(max_length=20)
    progress = models.CharField(max_length=200)
    status = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    l_date =  models.DateField()
    file = models.FileField(null=True)
    price = models.CharField(max_length=20,null=True)
    desc = models.CharField(max_length=20,null=True)
    userid = models.ForeignKey(Customer, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    makeup = models.ForeignKey(MakeUp, on_delete=models.CASCADE)
    concre = models.ForeignKey(Content, on_delete=models.CASCADE)
    p_title = models.CharField(max_length=50, default='student')  # Customer's professional title or position
    email = models.EmailField(default='null@gmail.com')  # Email address
    contact = models.CharField(max_length=15, default='9876566767')  # Phone number
    pic = models.CharField(max_length=200, default='pic.png')  # Profile picture
    bio = models.TextField(null=True)  # Bio/About Me
    



class Payment(models.Model):
    totamt =models.IntegerField()
    conamt =models.IntegerField()
    photoamt =models.IntegerField()
    makeupamt =models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    makeup = models.ForeignKey(MakeUp, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)


class Card(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    card_no = models.CharField(max_length=255)
    Name = models.CharField(max_length=20)
    exp_date = models.CharField(max_length=20)


class Feedback(models.Model):
    feed = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)


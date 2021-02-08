from django.db import models

# Create your models here.
class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100,null=True)
    lname = models.CharField(max_length=100)
    email=models.EmailField(max_length=70)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class item(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    status=models.IntegerField()
    date=models.DateField()
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)



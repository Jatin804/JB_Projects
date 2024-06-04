from django.db import models

# Create your models here.

class Users(models.Model):
    email = models.EmailField(max_length=225, primary_key=True, null=False)
    password = models.CharField(max_length=125, unique=True)


class Review(models.Model):
    review = models.CharField(max_length=1000)
    email = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateField(null=False)

    
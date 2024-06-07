from django.db import models

# Create your models here.


# for reviews which will hold reviews 
class Users(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    review = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.username


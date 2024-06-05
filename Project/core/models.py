from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=225, unique=True, null=True)
    password = models.CharField(max_length=125, primary_key=True, null=False)
    review = models.CharField(max_length=1000, null=True)
    # date = models.DateField(null=True)


    class Meta:
        db_table = "user"

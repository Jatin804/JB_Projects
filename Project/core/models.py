from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=225, unique=True, null=True)
    password = models.CharField(max_length=125, null=False)
    review = models.TextField(max_length=1000, null=True)
    # date = models.DateField(null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

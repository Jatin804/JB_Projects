# Generated by Django 5.0.2 on 2024-06-06 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_userprofile_delete_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='review',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
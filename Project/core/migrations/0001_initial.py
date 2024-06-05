# Generated by Django 5.0.2 on 2024-06-05 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('username', models.CharField(max_length=225, null=True, unique=True)),
                ('password', models.CharField(max_length=125, primary_key=True, serialize=False)),
                ('review', models.CharField(max_length=1000, null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]

# Generated by Django 4.0.5 on 2022-07-01 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]

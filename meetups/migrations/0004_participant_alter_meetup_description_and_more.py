# Generated by Django 4.0.5 on 2022-07-01 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0003_location_meetup_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='meetup',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='meetup',
            name='participant',
            field=models.ManyToManyField(blank=True, null=True, to='meetups.participant'),
        ),
    ]

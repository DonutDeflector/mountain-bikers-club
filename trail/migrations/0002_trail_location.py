# Generated by Django 2.1 on 2018-08-27 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trail',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Location'),
        ),
    ]

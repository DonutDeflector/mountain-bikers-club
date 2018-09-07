# Generated by Django 2.1.1 on 2018-09-07 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20180902_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'unique': 'A user with that email address already exists.'}, help_text='Required. No bullshit, I promise.', max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
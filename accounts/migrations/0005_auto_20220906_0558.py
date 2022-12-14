# Generated by Django 3.2 on 2022-09-06 05:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_users_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='first_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='last_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Surname'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2 on 2022-09-06 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20220906_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='phone_number',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]

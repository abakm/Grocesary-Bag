# Generated by Django 3.1 on 2021-02-08 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.CharField(max_length=100),
        ),
    ]

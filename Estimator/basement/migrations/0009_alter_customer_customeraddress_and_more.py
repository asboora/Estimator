# Generated by Django 4.0.4 on 2022-04-27 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basement', '0008_alter_customer_customername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customerAddress',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customerContact',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

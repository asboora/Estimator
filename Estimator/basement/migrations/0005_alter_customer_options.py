# Generated by Django 4.0.4 on 2022-04-24 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basement', '0004_customer_dumpster_customer_electrical_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['customerContact']},
        ),
    ]

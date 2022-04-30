# Generated by Django 4.0.4 on 2022-04-30 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basement', '0012_alter_customer_drywall_sqft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Ceiling_Texture',
            field=models.CharField(choices=[('1', 'Knockdown'), ('2', 'Others'), ('3', 'None')], default=3, max_length=20),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Panel_Location',
            field=models.CharField(choices=[('1', 'Basement'), ('2', 'Garage')], default=1, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Wall_Texture',
            field=models.CharField(choices=[('1', 'Orange Peel'), ('2', 'Others'), ('3', 'None')], default=3, max_length=20),
        ),
    ]

# Generated by Django 2.2 on 2019-04-23 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='avg_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]

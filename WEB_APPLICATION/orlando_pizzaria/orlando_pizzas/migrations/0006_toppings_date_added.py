# Generated by Django 4.2 on 2023-04-21 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orlando_pizzas', '0005_remove_toppings_date_added_toppings_toppping_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='toppings',
            name='date_added',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
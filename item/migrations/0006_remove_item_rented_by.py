# Generated by Django 5.0.1 on 2024-01-13 21:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("item", "0005_remove_item_count_item_rented_by"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="rented_by",
        ),
    ]

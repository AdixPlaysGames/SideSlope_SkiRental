# Generated by Django 5.0.1 on 2024-01-13 19:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("item", "0003_category_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="count",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
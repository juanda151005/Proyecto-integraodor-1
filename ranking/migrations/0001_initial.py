# Generated by Django 5.0.7 on 2024-09-06 17:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("city", "0002_remove_city_ranking"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ranking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rank", models.PositiveIntegerField()),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="city.city"
                    ),
                ),
            ],
        ),
    ]

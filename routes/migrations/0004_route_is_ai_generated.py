# Generated by Django 5.1 on 2024-10-13 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0003_alter_route_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='is_ai_generated',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 5.0.7 on 2024-10-10 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
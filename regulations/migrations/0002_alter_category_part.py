# Generated by Django 4.1.1 on 2022-10-17 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("regulations", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="part",
            field=models.IntegerField(null=True),
        ),
    ]
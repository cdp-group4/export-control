# Generated by Django 4.1.1 on 2022-10-31 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0008_extendedflatpage_title_no"),
    ]

    operations = [
        migrations.AddField(
            model_name="extendedflatpage",
            name="sidebar_title",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="extendedflatpage",
            name="sidebar_title_no",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]

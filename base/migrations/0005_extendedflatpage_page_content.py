# Generated by Django 4.1.1 on 2022-10-24 19:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0004_extendedflatpage_sidebar_text_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="extendedflatpage",
            name="page_content",
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
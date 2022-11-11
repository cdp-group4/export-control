# Generated by Django 4.1.1 on 2022-11-11 00:55

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=128, verbose_name="Navn")),
                ("email", models.EmailField(max_length=254, verbose_name="Epost")),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, null=True, region=None, verbose_name="Telefonnummer"
                    ),
                ),
                ("message", models.TextField(verbose_name="Melding")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("new", "Ny"),
                            ("in_progress", "Aktiv"),
                            ("resolved", "Løst"),
                            ("canceled", "Kansellert"),
                        ],
                        default="new",
                        max_length=30,
                        verbose_name="Status",
                    ),
                ),
                ("archived", models.BooleanField(default=False, verbose_name="Arkivert")),
                ("date_created", models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Opprettet")),
                ("date_updated", models.DateTimeField(auto_now=True, db_index=True, verbose_name="Sist oppdatert")),
            ],
        ),
    ]

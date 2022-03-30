# Generated by Django 4.0.2 on 2022-03-26 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("recycle", "0001_initial"),
        ("reuse", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="NGOLocation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("items_accepted", models.TextField(null=True)),
                ("email", models.EmailField(max_length=254, null=True)),
                ("phone", models.CharField(max_length=17, null=True)),
                ("street_address", models.TextField()),
                (
                    "zip_code",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recycle.zipcode",
                    ),
                ),
            ],
        ),
    ]

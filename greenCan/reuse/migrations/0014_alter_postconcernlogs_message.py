# Generated by Django 4.0.2 on 2022-05-07 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reuse", "0013_postconcernlogs_checked"),
    ]

    operations = [
        migrations.AlterField(
            model_name="postconcernlogs",
            name="message",
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
# Generated by Django 4.0.1 on 2022-04-26 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("moderation", "0004_alter_volunteerlogs_approved"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="volunteerlogs",
            name="post",
        ),
        migrations.AddField(
            model_name="volunteerlogs",
            name="content_type",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="contenttypes.contenttype",
            ),
            preserve_default=False,
        ),
    ]

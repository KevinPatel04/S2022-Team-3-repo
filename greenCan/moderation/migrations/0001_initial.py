# Generated by Django 4.0.1 on 2022-04-19 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reuse', '0009_remove_image_approved_alter_post_approved'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('reason', models.CharField(max_length=250)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reuse.post')),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-05 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_media', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

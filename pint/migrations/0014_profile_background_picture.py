# Generated by Django 4.2.2 on 2023-08-08 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pint', '0013_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='background_picture',
            field=models.ImageField(null=True, upload_to='background_picture'),
        ),
    ]

# Generated by Django 4.2.2 on 2023-08-18 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pint', '0026_alter_profile_bio_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='profile_picture'),
        ),
    ]

# Generated by Django 4.2.2 on 2023-09-17 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pint', '0027_alter_profile_bio_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='No bio', max_length=150, null=True),
        ),
    ]

# Generated by Django 4.2.2 on 2023-09-17 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pint', '0029_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='profile_picture/no-dp.png', null=True, upload_to='profile_picture'),
        ),
    ]

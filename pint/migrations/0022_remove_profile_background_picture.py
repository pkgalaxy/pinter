# Generated by Django 4.2.2 on 2023-08-13 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pint', '0021_rename_post_related_comment_related'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='background_picture',
        ),
    ]

# Generated by Django 4.2.2 on 2023-07-07 08:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pint', '0002_post_author_post_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(null=True, related_name='blog', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 4.2.2 on 2023-08-09 15:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pint', '0014_profile_background_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 15, 55, 48, 72753, tzinfo=datetime.timezone.utc)),
        ),
    ]

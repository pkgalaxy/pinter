# Generated by Django 4.2.2 on 2023-08-09 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pint', '0018_rename_post_comment_post_related'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

# Generated by Django 3.0.7 on 2020-06-23 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200623_1305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='humiditysensor',
            old_name='s_name_id',
            new_name='s_name',
        ),
    ]

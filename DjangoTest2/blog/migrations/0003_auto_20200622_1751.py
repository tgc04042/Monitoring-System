# Generated by Django 3.0.7 on 2020-06-22 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200619_1737'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensor',
            old_name='name',
            new_name='s_name',
        ),
    ]

# Generated by Django 5.0.5 on 2024-06-19 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regions_a15', '0002_fieldevent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='region',
            old_name='slugname',
            new_name='slug',
        ),
    ]

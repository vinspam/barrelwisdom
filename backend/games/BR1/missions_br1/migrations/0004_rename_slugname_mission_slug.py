# Generated by Django 5.0.5 on 2024-06-19 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('missions_br1', '0003_mission_character'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mission',
            old_name='slugname',
            new_name='slug',
        ),
    ]

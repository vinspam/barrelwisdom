# Generated by Django 5.0.5 on 2024-06-19 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items_a22', '0014_alter_item_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='slugname',
            new_name='slug',
        ),
    ]

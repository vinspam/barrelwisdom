# Generated by Django 5.0.2 on 2024-02-20 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items_a25', '0015_item_gbl_recipepage_gbl_latestupdategbl'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='val2_bad',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='val2_good',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]

# Generated by Django 5.0.5 on 2024-09-17 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chara_a25', '0016_passive_val2_passive_val3_passive_val4'),
    ]

    operations = [
        migrations.AddField(
            model_name='passive',
            name='num',
            field=models.IntegerField(default=3),
        ),
    ]

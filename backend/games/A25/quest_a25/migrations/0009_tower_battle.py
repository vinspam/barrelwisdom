# Generated by Django 5.0.2 on 2024-02-24 04:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quest_a25', '0008_dungeonfloor_q_id_scorebattledifficulties_q_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tower',
            name='battle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quest_a25.battle'),
        ),
    ]

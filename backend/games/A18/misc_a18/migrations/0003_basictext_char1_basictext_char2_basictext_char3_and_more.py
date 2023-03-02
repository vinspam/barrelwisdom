# Generated by Django 4.1.4 on 2023-03-01 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('misc_a18', '0002_basictext'),
    ]

    operations = [
        migrations.AddField(
            model_name='basictext',
            name='char1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='char1', to='misc_a18.character'),
        ),
        migrations.AddField(
            model_name='basictext',
            name='char2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='char2', to='misc_a18.character'),
        ),
        migrations.AddField(
            model_name='basictext',
            name='char3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='char3', to='misc_a18.character'),
        ),
        migrations.AddField(
            model_name='basictext',
            name='char4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='char4', to='misc_a18.character'),
        ),
    ]

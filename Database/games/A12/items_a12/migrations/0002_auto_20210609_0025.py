# Generated by Django 3.0.6 on 2021-06-09 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('traits_a12', '0001_initial'),
        ('items_a12', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='traits',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='traits_a12.Trait'),
        ),
    ]

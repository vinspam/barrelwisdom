# Generated by Django 3.2.9 on 2021-12-05 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demons_brsl', '0005_alter_demon_warp'),
        ('regions_brsl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemonArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('once', models.BooleanField(default=False)),
                ('demon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demons_brsl.demon')),
            ],
        ),
        migrations.AlterField(
            model_name='area',
            name='demons',
            field=models.ManyToManyField(to='regions_brsl.DemonArea'),
        ),
    ]

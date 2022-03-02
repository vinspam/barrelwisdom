# Generated by Django 4.0.2 on 2022-03-01 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdvData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attTag0', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('actTag0', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('min_1_0', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('max_1_0', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('min_2_0', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('max_2_0', models.CharField(blank=True, default='', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Effect_en',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Effect_ja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Effect_ko',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Effect_sc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Effect_tc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('index', models.IntegerField()),
                ('advanced', models.ManyToManyField(to='effects_a23.AdvData')),
                ('eff_en', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='effects_a23.effect_en')),
                ('eff_ja', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='effects_a23.effect_ja')),
                ('eff_ko', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='effects_a23.effect_ko')),
                ('eff_sc', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='effects_a23.effect_sc')),
                ('eff_tc', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='effects_a23.effect_tc')),
            ],
            options={
                'ordering': ['index'],
            },
        ),
    ]

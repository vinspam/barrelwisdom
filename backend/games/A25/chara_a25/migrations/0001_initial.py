# Generated by Django 4.2.5 on 2023-10-06 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('misc_a25', '0006_alter_name_text_en'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rarity', models.IntegerField()),
                ('hp', models.IntegerField()),
                ('spd', models.IntegerField()),
                ('patk', models.IntegerField()),
                ('pdfn', models.IntegerField()),
                ('matk', models.IntegerField()),
                ('mdfn', models.IntegerField()),
                ('rate_hp', models.IntegerField()),
                ('rate_patk', models.IntegerField()),
                ('rate_pdfn', models.IntegerField()),
                ('rate_matk', models.IntegerField()),
                ('rate_mdfn', models.IntegerField()),
                ('res_ice', models.IntegerField(default=0)),
                ('res_fir', models.IntegerField(default=0)),
                ('res_imp', models.IntegerField(default=0)),
                ('res_ltn', models.IntegerField(default=0)),
                ('res_pie', models.IntegerField(default=0)),
                ('res_sla', models.IntegerField(default=0)),
                ('res_wnd', models.IntegerField(default=0)),
                ('color1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='char_color1', to='misc_a25.filterable')),
                ('color2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='char_color2', to='misc_a25.filterable')),
                ('elem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chara_elem', to='misc_a25.filterable')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misc_a25.name')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misc_a25.filterable')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chara_title', to='misc_a25.name')),
                ('trait1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chara_trait1', to='misc_a25.trait')),
                ('trait2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chara_trait2', to='misc_a25.trait')),
                ('trait3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chara_trait3', to='misc_a25.trait')),
            ],
            options={
                'ordering': ['-rarity', 'role', 'name__text_en'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wt', models.IntegerField(default=0)),
                ('val1', models.IntegerField()),
                ('val2', models.IntegerField()),
                ('pow1', models.IntegerField()),
                ('pow2', models.IntegerField()),
                ('pow3', models.IntegerField()),
                ('pow4', models.IntegerField()),
                ('pow5', models.IntegerField()),
                ('break1', models.IntegerField()),
                ('break2', models.IntegerField()),
                ('break3', models.IntegerField()),
                ('break4', models.IntegerField()),
                ('break5', models.IntegerField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_area', to='misc_a25.name')),
                ('char', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chara_a25.character')),
                ('desc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misc_a25.desc')),
                ('elem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misc_a25.filterable')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misc_a25.name')),
            ],
        ),
        migrations.CreateModel(
            name='Passive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('val', models.IntegerField()),
                ('char', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chara_a25.character')),
                ('desc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misc_a25.desc')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misc_a25.name')),
            ],
        ),
        migrations.CreateModel(
            name='Memoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rarity', models.IntegerField()),
                ('lv1', models.IntegerField()),
                ('lv2', models.IntegerField()),
                ('lv3', models.IntegerField()),
                ('lv4', models.IntegerField()),
                ('lv5', models.IntegerField()),
                ('hp1', models.IntegerField()),
                ('hp30', models.IntegerField()),
                ('spd1', models.IntegerField()),
                ('spd30', models.IntegerField()),
                ('patk1', models.IntegerField()),
                ('patk30', models.IntegerField()),
                ('matk1', models.IntegerField()),
                ('matk30', models.IntegerField()),
                ('pdef1', models.IntegerField()),
                ('pdef30', models.IntegerField()),
                ('mdef1', models.IntegerField()),
                ('mdef30', models.IntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misc_a25.name')),
                ('skill_desc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='misc_a25.desc')),
                ('skill_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memoria_skill', to='misc_a25.name')),
            ],
            options={
                'ordering': ['-rarity', 'name__text_en'],
            },
        ),
        migrations.AddConstraint(
            model_name='character',
            constraint=models.UniqueConstraint(fields=('name', 'title'), name='gacha-char'),
        ),
    ]

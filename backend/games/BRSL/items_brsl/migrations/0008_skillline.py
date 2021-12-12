# Generated by Django 3.2.9 on 2021-12-05 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items_brsl', '0007_auto_20211205_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effect1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eff1', to='items_brsl.effect')),
                ('effect2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eff2', to='items_brsl.effect')),
                ('effect3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eff3', to='items_brsl.effect')),
                ('items', models.ManyToManyField(to='items_brsl.Item')),
                ('linename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items_brsl.linename')),
            ],
            options={
                'ordering': ['linename'],
            },
        ),
    ]

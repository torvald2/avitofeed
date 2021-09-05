# Generated by Django 3.2.7 on 2021-09-04 04:49

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cellName', models.TextField()),
                ('info', models.TextField()),
                ('xmlValue', models.TextField()),
                ('dataType', models.IntegerField(choices=[(1, 'Число'), (2, 'Текст'), (3, 'Несколько значений'), (3, 'Дата'), (4, 'Логическое')])),
                ('values', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
                ('max_len', models.IntegerField()),
                ('valueForDisplay', models.TextField()),
                ('fieldForDisplay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.cell')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.table')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('Description', models.TextField()),
                ('XML_Value', models.TextField()),
                ('Parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.category')),
                ('Platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.platform')),
                ('Table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.table')),
            ],
        ),
    ]
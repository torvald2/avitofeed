# Generated by Django 3.2.7 on 2021-09-08 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_auto_20210908_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='feed.category'),
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-13 04:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xglass', '0002_alter_prodect_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodect',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='xglass.category'),
        ),
    ]

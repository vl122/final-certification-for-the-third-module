# Generated by Django 5.0.1 on 2024-02-28 16:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='rate',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)]),
            preserve_default=False,
        ),
    ]

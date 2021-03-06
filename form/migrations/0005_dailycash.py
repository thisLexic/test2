# Generated by Django 2.2.5 on 2019-12-29 14:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_auto_20191228_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyCash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('actual_income', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(0)])),
                ('theoretical_income', models.FloatField()),
                ('difference_value', models.FloatField()),
                ('difference_percent', models.FloatField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dailyincome', to='form.Branch')),
            ],
        ),
    ]

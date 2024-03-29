# Generated by Django 5.0.2 on 2024-02-24 07:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=144)),
                ('email', models.EmailField(max_length=254)),
                ('sub_state', models.BooleanField(default=True)),
                ('frequency', models.CharField(choices=[('weekly', 'Weekly'), ('monthly', 'Monthly')], default='weekly', max_length=10)),
                ('last_sent', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]

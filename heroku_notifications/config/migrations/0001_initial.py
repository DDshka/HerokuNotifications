# Generated by Django 3.1.3 on 2020-11-14 11:31

import django.contrib.postgres.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationConfig',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, unique=True)),
                ('provider_name', models.CharField(choices=[], max_length=128)),
                ('provider_args', models.JSONField(null=True)),
                ('secret', models.CharField(max_length=1024)),
                ('entities', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32), size=None)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

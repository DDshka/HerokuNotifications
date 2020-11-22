# Generated by Django 3.1.3 on 2020-11-14 16:17

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramConfig',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('chat_ids', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), size=None)),
                ('config', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='telegram', to='config.notificationconfig')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
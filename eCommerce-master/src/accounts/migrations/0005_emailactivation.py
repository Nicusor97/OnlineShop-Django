# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_user_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailActivation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('key', models.CharField(blank=True, max_length=120, null=True)),
                ('activated', models.BooleanField(default=False)),
                ('forced_expired', models.BooleanField(default=False)),
                ('expires', models.IntegerField(default=7)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20171025_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='billing_address_final',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address_final',
            field=models.TextField(blank=True, null=True),
        ),
    ]

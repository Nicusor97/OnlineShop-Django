# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20171108_0028'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductPurchaseManager',
        ),
    ]

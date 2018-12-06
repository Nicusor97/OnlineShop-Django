# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0002_marketingpreference_mailchimp_subscribed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marketingpreference',
            old_name='update',
            new_name='updated',
        ),
    ]

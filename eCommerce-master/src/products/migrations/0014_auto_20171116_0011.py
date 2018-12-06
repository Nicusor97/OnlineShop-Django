# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import products.models
import storages.backends.s3boto3


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20171109_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productfile',
            name='file',
            field=models.FileField(storage=storages.backends.s3boto3.S3Boto3Storage(location='protected'), upload_to=products.models.upload_product_file_loc),
        ),
    ]

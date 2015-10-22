# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storehouse', '0006_storehouse_geography_point'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storehouse',
            name='geography_point',
        ),
        migrations.DeleteModel(
            name='StoreHouse',
        ),
    ]

# Generated by Django 4.1 on 2022-08-31 14:53

import Expenses_tracker.web.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/', validators=[Expenses_tracker.web.validators.MaxSizeInMB(5)]),
        ),
    ]

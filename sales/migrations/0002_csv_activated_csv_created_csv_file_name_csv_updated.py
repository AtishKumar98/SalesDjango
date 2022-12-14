# Generated by Django 4.0.4 on 2022-04-28 03:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='csv',
            name='activated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='csv',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 4, 28, 3, 35, 21, 43881, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='csv',
            name='file_name',
            field=models.FileField(default='NO_CSV.csv', upload_to='csvs'),
        ),
        migrations.AddField(
            model_name='csv',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

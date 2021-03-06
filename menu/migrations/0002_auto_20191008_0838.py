# Generated by Django 2.2.6 on 2019-10-08 13:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='icecream',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='base',
            field=models.CharField(choices=[('vanilla', 'Vanilla'), ('chocolate', 'Chocolate')], max_length=20),
        ),
        migrations.AlterField(
            model_name='icecream',
            name='date_churned',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 8, 13, 38, 46, 255447, tzinfo=utc), verbose_name='date published'),
        ),
    ]

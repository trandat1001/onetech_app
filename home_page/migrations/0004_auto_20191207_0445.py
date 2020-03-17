# Generated by Django 2.2.7 on 2019-12-07 04:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0003_blog_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_best_rate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='is_feature',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='is_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='blog',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2019, 12, 7, 4, 45, 13, 958453)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2019, 12, 7, 4, 45, 13, 959159)),
        ),
    ]
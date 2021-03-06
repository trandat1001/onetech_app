# Generated by Django 2.2.7 on 2019-11-23 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('made_in', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('release_date', models.DateField()),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home_page.Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home_page.Category')),
            ],
        ),
    ]

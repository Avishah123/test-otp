# Generated by Django 3.1.1 on 2020-09-16 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20200916_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('mobile_number', models.CharField(blank=True, max_length=12)),
                ('email_id', models.EmailField(max_length=254)),
                ('Blood_type', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('Sample_text', models.CharField(max_length=100)),
                ('date_day', models.DateField()),
                ('otp', models.CharField(blank=True, max_length=6)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]

# Generated by Django 3.1.1 on 2020-09-15 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20200916_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mobile_number',
            field=models.CharField(max_length=11),
        ),
    ]

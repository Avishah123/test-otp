# Generated by Django 3.1.1 on 2020-09-17 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_delete_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact1',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-25 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20201125_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='description',
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-25 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0011_auto_20201125_2306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer',
            new_name='title',
        ),
    ]

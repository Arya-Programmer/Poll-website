# Generated by Django 3.1.3 on 2020-11-25 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20201125_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
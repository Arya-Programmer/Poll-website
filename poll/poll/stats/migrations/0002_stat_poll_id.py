# Generated by Django 3.1.3 on 2020-11-25 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stat',
            name='poll_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
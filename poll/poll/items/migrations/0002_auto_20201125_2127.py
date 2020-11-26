# Generated by Django 3.1.3 on 2020-11-25 18:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='form',
            name='description',
            field=models.TextField(default='human rights'),
            preserve_default=False,
        ),
    ]

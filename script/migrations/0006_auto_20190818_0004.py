# Generated by Django 2.2.4 on 2019-08-18 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('script', '0005_auto_20190817_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='script',
            name='id',
        ),
        migrations.AddField(
            model_name='script',
            name='script_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.2.4 on 2019-08-14 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('script', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='script',
            old_name='script_id',
            new_name='_id',
        ),
    ]

# Generated by Django 2.1.3 on 2018-12-11 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_command_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='command',
            name='name',
        ),
    ]
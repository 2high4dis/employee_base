# Generated by Django 4.2 on 2023-04-06 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_base_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='boss',
            new_name='parent',
        ),
    ]

# Generated by Django 3.0.3 on 2020-02-27 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='createad_on',
            new_name='created_on',
        ),
    ]

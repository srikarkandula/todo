# Generated by Django 3.1.4 on 2021-02-05 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_name',
            new_name='name',
        ),
    ]

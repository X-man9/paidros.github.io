# Generated by Django 3.2.7 on 2022-10-12 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20221012_0608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='image3',
            new_name='image',
        ),
    ]
# Generated by Django 3.2.2 on 2021-05-15 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Foto',
            new_name='Picture',
        ),
        migrations.RenameModel(
            old_name='Places',
            new_name='Place',
        ),
    ]

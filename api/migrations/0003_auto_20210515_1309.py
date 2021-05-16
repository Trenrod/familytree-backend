# Generated by Django 3.2.2 on 2021-05-15 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210515_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='children',
        ),
        migrations.AlterField(
            model_name='person',
            name='marriages',
            field=models.ManyToManyField(null=True, related_name='_api_person_marriages_+', to='api.Person'),
        ),
        migrations.AlterField(
            model_name='person',
            name='parents',
            field=models.ManyToManyField(null=True, to='api.Person'),
        ),
    ]
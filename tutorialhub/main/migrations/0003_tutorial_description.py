# Generated by Django 3.1.1 on 2020-09-16 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_tutorial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='description',
            field=models.TextField(default='Default description for tutorial'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.1 on 2020-09-16 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_tutorial_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorial',
            name='description',
        ),
        migrations.AddField(
            model_name='subject',
            name='description',
            field=models.TextField(default='Default description for subject'),
            preserve_default=False,
        ),
    ]
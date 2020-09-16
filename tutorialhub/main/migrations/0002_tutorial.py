# Generated by Django 3.1.1 on 2020-09-13 06:45

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to=main.models.tutorial_upload_path_handler)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutorials', to='main.subject')),
            ],
        ),
    ]
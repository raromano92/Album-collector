# Generated by Django 4.0.6 on 2022-07-21 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_tracklist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracklist',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]
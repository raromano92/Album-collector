# Generated by Django 4.0.6 on 2022-07-21 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_tracklist_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracklist',
            name='track',
            field=models.CharField(max_length=100, verbose_name='Song'),
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-21 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_tracklist_track'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracklist',
            name='single',
            field=models.BooleanField(choices=[('True', 'Yes'), ('False', 'No')], default=False),
        ),
    ]
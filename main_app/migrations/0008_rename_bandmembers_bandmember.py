# Generated by Django 4.0.6 on 2022-07-21 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_bandmembers_alter_tracklist_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BandMembers',
            new_name='BandMember',
        ),
    ]
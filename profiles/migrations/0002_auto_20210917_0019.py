# Generated by Django 3.2.6 on 2021-09-17 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='country',
            new_name='default_country',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='county',
            new_name='default_county',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='phone_number',
            new_name='default_phone_number',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='postcode',
            new_name='default_postcode',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='street_address1',
            new_name='default_street_address1',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='street_address2',
            new_name='default_street_address2',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='town_or_city',
            new_name='default_town_or_city',
        ),
    ]

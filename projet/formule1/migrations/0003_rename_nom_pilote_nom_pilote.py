# Generated by Django 4.0.3 on 2022-05-04 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formule1', '0002_pilote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pilote',
            old_name='nom',
            new_name='nom_pilote',
        ),
    ]

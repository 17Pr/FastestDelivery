# Generated by Django 4.1.1 on 2022-09-19 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interns', '0002_distrubuter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='distrubuter',
            old_name='services',
            new_name='mode',
        ),
    ]
# Generated by Django 4.1.1 on 2022-09-19 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interns', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='distrubuter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('placeofpickup', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('services', models.CharField(max_length=15)),
                ('typeofproduct', models.CharField(max_length=15)),
            ],
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-15 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.CharField(max_length=80)),
                ('phno', models.CharField(max_length=80)),
                ('college', models.CharField(max_length=100)),
                ('skills', models.CharField(max_length=500)),
            ],
        ),
    ]

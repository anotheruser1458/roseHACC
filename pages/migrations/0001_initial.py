# Generated by Django 3.2.8 on 2021-11-08 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hike_name', models.CharField(max_length=50)),
                ('hike_difficulty', models.IntegerField(default=3)),
                ('hike_rating', models.IntegerField(default=4)),
                ('hike_images', models.CharField(default='', max_length=50)),
                ('hike_description', models.CharField(default='', max_length=500)),
                ('hike_location', models.CharField(default='', max_length=50)),
                ('hike_route', models.CharField(default='', max_length=500)),
                ('hike_length', models.FloatField(default=2)),
                ('hike_elevation', models.IntegerField(default=100)),
                ('hike_duration', models.IntegerField()),
                ('hike_attributes', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Traffic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hikeID', models.IntegerField(default=0)),
                ('date', models.IntegerField(default=0)),
                ('num_people_1', models.IntegerField(default=0)),
                ('num_people_2', models.IntegerField(default=0)),
                ('num_people_3', models.IntegerField(default=0)),
                ('num_people_4', models.IntegerField(default=0)),
                ('num_people_5', models.IntegerField(default=0)),
                ('num_people_6', models.IntegerField(default=0)),
            ],
        ),
    ]

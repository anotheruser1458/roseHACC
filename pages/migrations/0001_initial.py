# Generated by Django 3.2.8 on 2021-11-07 00:40

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
            ],
        ),
    ]
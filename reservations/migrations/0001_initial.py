# Generated by Django 3.2.8 on 2021-11-07 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('number_of_people', models.IntegerField()),
                ('hike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.hike')),
            ],
        ),
    ]

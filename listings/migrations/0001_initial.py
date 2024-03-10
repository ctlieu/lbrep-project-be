# Generated by Django 4.2.8 on 2023-12-09 22:54

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, null=True)),
                ('area', models.CharField(blank=True, choices=[('Calgary', 'Calgary'), ('Inner London', 'Inner London'), ('Outer London', 'Outer London')], max_length=20, null=True)),
                ('borough', models.CharField(blank=True, max_length=50, null=True)),
                ('listing_type', models.CharField(choices=[('Condo', 'Condo'), ('House', 'House'), ('Apartment', 'Apartment'), ('Office', 'Office')], max_length=20)),
                ('property_status', models.CharField(blank=True, choices=[('Sale', 'Sale'), ('Rent', 'Rent')], max_length=20, null=True)),
                ('price', models.DecimalField(decimal_places=0, max_digits=50)),
                ('rental_frequency', models.CharField(blank=True, choices=[('Month', 'Month'), ('Week', 'Week'), ('Day', 'Day')], max_length=20, null=True)),
                ('rooms', models.IntegerField(blank=True, null=True)),
                ('furnished', models.BooleanField(default=False)),
                ('pool', models.BooleanField(default=False)),
                ('elevator', models.BooleanField(default=False)),
                ('cctv', models.BooleanField(default=False)),
                ('parking', models.BooleanField(default=False)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('picture1', models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/')),
                ('picture2', models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/')),
                ('picture3', models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/')),
                ('picture4', models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/')),
                ('picture5', models.ImageField(blank=True, null=True, upload_to='pictures/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Poi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('type', models.CharField(choices=[('University', 'University'), ('Hospital', 'Hospital'), ('Stadium', 'Stadium'), ('PublicSchool', 'PublicSchool')], max_length=50)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
            ],
        ),
    ]

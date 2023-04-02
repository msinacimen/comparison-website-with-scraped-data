# Generated by Django 4.1.2 on 2022-10-15 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('brand', models.CharField(blank=True, max_length=50, null=True)),
                ('model', models.TextField(blank=True, null=True)),
                ('operating_system', models.CharField(blank=True, max_length=50, null=True)),
                ('cpu', models.CharField(blank=True, max_length=50, null=True)),
                ('gpu', models.CharField(blank=True, max_length=50, null=True)),
                ('ram', models.IntegerField(blank=True, null=True)),
                ('disk', models.IntegerField(blank=True, null=True)),
                ('disk_type', models.CharField(blank=True, max_length=50, null=True)),
                ('screen_size', models.FloatField(blank=True, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('site', models.CharField(blank=True, max_length=50, null=True)),
                ('site_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]

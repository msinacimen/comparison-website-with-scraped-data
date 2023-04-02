# Generated by Django 4.1.2 on 2022-10-05 16:00

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
                ('isim', models.CharField(max_length=1000)),
                ('marka', models.CharField(max_length=50)),
                ('model_adi', models.TextField()),
                ('model_no', models.CharField(max_length=50)),
                ('isletim_sistemi', models.CharField(max_length=50)),
                ('islemci_tipi', models.CharField(max_length=50)),
                ('islemci_nesli', models.IntegerField()),
                ('ram', models.IntegerField()),
                ('disk_boyutu', models.IntegerField()),
                ('disk_turu', models.CharField(max_length=50)),
                ('ekran_boyutu', models.FloatField()),
                ('puani', models.FloatField()),
                ('fiyat', models.FloatField()),
                ('site_ismi', models.CharField(max_length=50)),
            ],
        ),
    ]
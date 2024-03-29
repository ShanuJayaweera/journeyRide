# Generated by Django 2.2.3 on 2019-07-28 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('driverName', models.CharField(max_length=100)),
                ('DOB', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('NIC', models.CharField(max_length=100)),
                ('licenseNO', models.CharField(max_length=100)),
                ('profilePicUrl', models.ImageField(upload_to='')),
                ('drivingLicenseUrl', models.ImageField(upload_to='')),
                ('createdDate', models.DateField(auto_now_add=True)),
                ('updateDate', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('passengerName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('country', models.CharField(max_length=100)),
                ('profilePicUrl', models.ImageField(upload_to='')),
                ('telNo', models.CharField(max_length=20)),
                ('createdDate', models.DateField(auto_now_add=True)),
                ('updateDate', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('vehicleImage1', models.ImageField(upload_to='')),
                ('vehicleImage2', models.ImageField(upload_to='')),
                ('vehicleImage3', models.ImageField(upload_to='')),
                ('regNo', models.CharField(max_length=100)),
                ('ownerName', models.CharField(max_length=100)),
                ('ownerAddress', models.CharField(max_length=100)),
                ('numberOfPassenger', models.IntegerField()),
                ('acCondition', models.BinaryField()),
                ('insExpDate', models.DateField()),
                ('createdDate', models.DateField(auto_now_add=True)),
                ('updateDate', models.DateField(auto_now=True)),
            ],
        ),
    ]

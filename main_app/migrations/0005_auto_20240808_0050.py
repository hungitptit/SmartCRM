# Generated by Django 3.2.25 on 2024-08-07 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20240806_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('districtID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='departmentID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.department'),
        ),
        migrations.CreateModel(
            name='EmployeeDistrict',
            fields=[
                ('employeeDistrictID', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('districtID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.district')),
                ('employeeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.employee')),
            ],
        ),
    ]
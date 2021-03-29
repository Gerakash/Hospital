# Generated by Django 3.1.7 on 2021-03-23 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hospitals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('hospitals', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospitals.hospital')),
            ],
        ),
    ]

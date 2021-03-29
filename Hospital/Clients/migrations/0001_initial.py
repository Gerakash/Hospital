# Generated by Django 3.1.7 on 2021-03-25 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone_number', models.PositiveIntegerField(blank=True, default=0)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-25 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0032_auto_20210625_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='famehousenewmonform',
            name='type',
            field=models.CharField(default='Email/Chat Other', max_length=50),
        ),
        migrations.AlterField(
            model_name='chatmonitoringformeva',
            name='process',
            field=models.CharField(default='Noom Eva', max_length=50),
        ),
        migrations.AlterField(
            model_name='chatmonitoringformpodfather',
            name='process',
            field=models.CharField(default='Noom POD', max_length=50),
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-11 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0020_auto_20210311_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='process',
            field=models.CharField(choices=[('Fame House', 'Fame House'), ('CTS', 'CTS')], max_length=100),
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-21 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0019_superplaymonform_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='danielwellinchatemailmonform',
            name='type',
            field=models.CharField(default='Email - Chat', max_length=50),
        ),
        migrations.AlterField(
            model_name='danielwellinchatemailmonform',
            name='process',
            field=models.CharField(default='Daniel Wellington - Chat - Email', max_length=50),
        ),
    ]
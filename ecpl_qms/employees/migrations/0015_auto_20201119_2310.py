# Generated by Django 3.1.3 on 2020-11-19 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0014_inboundmonitoringform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='test@ecpl.com', max_length=254, null=True),
        ),
    ]

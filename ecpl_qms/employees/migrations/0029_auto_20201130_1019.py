# Generated by Django 3.1.3 on 2020-11-30 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0028_auto_20201130_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmonitorinform',
            name='emp_comments',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='emailmonitoringform',
            name='emp_comments',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='inboundmonitoringform',
            name='emp_comments',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='outboundmonitoringform',
            name='emp_comments',
            field=models.TextField(null=True),
        ),
    ]

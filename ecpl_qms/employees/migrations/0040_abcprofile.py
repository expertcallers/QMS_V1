# Generated by Django 3.2.4 on 2021-07-02 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0039_hiveincubatoremailmonform_medtechgroupemailmonform_rainbowdiagnosticsemailmonform'),
    ]

    operations = [
        migrations.CreateModel(
            name='ABCprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('manager', models.CharField(max_length=100)),
                ('am', models.CharField(max_length=100)),
                ('tl', models.CharField(max_length=100)),
            ],
        ),
    ]
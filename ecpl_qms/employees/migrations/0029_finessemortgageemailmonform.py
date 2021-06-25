# Generated by Django 3.2.4 on 2021-06-25 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0028_clearviewemailmonform'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinesseMortgageEmailMonForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process', models.CharField(default='Finesse Mortgage Email', max_length=50)),
                ('type', models.CharField(default='Email - Chat', max_length=50)),
                ('emp_id', models.IntegerField()),
                ('associate_name', models.CharField(max_length=50)),
                ('qa', models.CharField(max_length=50)),
                ('team_lead', models.CharField(max_length=50)),
                ('customer_name', models.CharField(max_length=50)),
                ('customer_contact', models.CharField(max_length=100)),
                ('trans_date', models.DateField()),
                ('audit_date', models.DateField()),
                ('campaign', models.CharField(max_length=100)),
                ('zone', models.CharField(max_length=50)),
                ('concept', models.CharField(max_length=60)),
                ('duration', models.IntegerField()),
                ('manager', models.CharField(max_length=50)),
                ('manager_id', models.IntegerField()),
                ('category', models.CharField(max_length=20)),
                ('ce_1', models.IntegerField()),
                ('ce_2', models.IntegerField()),
                ('ce_3', models.IntegerField()),
                ('ce_4', models.IntegerField()),
                ('ce_5', models.IntegerField()),
                ('ce_6', models.IntegerField()),
                ('ce_7', models.IntegerField()),
                ('ce_8', models.IntegerField()),
                ('ce_9', models.IntegerField()),
                ('ce_10', models.IntegerField()),
                ('ce_11', models.IntegerField()),
                ('business_1', models.IntegerField()),
                ('business_2', models.IntegerField()),
                ('compliance_1', models.IntegerField()),
                ('compliance_2', models.IntegerField()),
                ('compliance_3', models.IntegerField()),
                ('compliance_4', models.IntegerField()),
                ('compliance_5', models.IntegerField()),
                ('areas_improvement', models.TextField()),
                ('positives', models.TextField()),
                ('comments', models.TextField()),
                ('added_by', models.CharField(max_length=30)),
                ('status', models.BooleanField(default=False)),
                ('closed_date', models.DateTimeField(null=True)),
                ('emp_comments', models.TextField(null=True)),
                ('ce_total', models.IntegerField(null=True)),
                ('business_total', models.IntegerField(null=True)),
                ('compliance_total', models.IntegerField(null=True)),
                ('overall_score', models.IntegerField(null=True)),
                ('am', models.CharField(max_length=50, null=True)),
                ('week', models.CharField(max_length=20, null=True)),
                ('fatal', models.BooleanField(default=False)),
                ('fatal_count', models.IntegerField(default=0)),
                ('disput_status', models.BooleanField(default=False)),
            ],
        ),
    ]

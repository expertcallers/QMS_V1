from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    team_list = (
        ('Noom','Noom'),('Aadya Solutions','Aadya Solutions'),('UPS CLP','UPS CLP'),('Gardening Express','Gardening Express'),
        ('Maxwell Properties','Maxwell Properties'),('Gubagoo','Gubagoo'),('Digital Swiss Gold','Digital Swiss Gold'),
        ('Digital Signage','Digital Signage'),('Success Systems','Success Systems'),('Advancement Consulting ','Advancement Consulting'),
        ('Insalvage','Insalvage'),('Medicare','Medicare'),('Printerpix','Printerpix'),('Printerpix Training','Printerpix Training'),
        ('First Look Appraisal','First Look Appraisal'),('TCA Counseling Group','TCA Counseling Group'),('Advit Sahdev Marketing','Advit Sahdev Marketing'),
        ('AKDY','AKDY'),('AKDY Training','AKDY Training'),('Monster Lead Group','Monster Lead Group'),('Fame House','Fame House'),
        ('Lecanto Green coffee','Lecanto Green coffee'),('Micro Distributing','Micro Distributing'),('Aditya Birla','Aditya Birla'),
        ('Aditya Birla Cellulose','Aditya Birla Cellulose'),('Aditya Birla Cellulose Training','Aditya Birla Cellulose Training'),
        ('City Security Services','City Security Services'),('Active Sports Club','Active Sports Club'),('Aditya Birla Sampling Team','Aditya Birla Sampling Team'),
        ('Aditya Birla Sampling Team Trainig','Aditya Birla Sampling Team Trainig'),('Bigo - IMO Group Chat','Bigo - IMO Group Chat'),
        ('Bigo Monitor Team','Bigo Monitor Team'),('Daniel Wellington','Daniel Wellington'),('Option Matrix','Option Matrix'),
        ('Info Think LLC','Info Think LLC'),('MT Cosmetics','MT Cosmetics'),("Something's Brewing","Something's Brewing"),
        ('WIT Digital','WIT Digital'),('Sync Treasury LLC','Sync Treasury LLC'),('SANA GAMING CONSULTING','SANA GAMING CONSULTING'),
        ('GrayStone LLC','GrayStone LLC'),('Kaapi Machines','Kaapi Machines'),('Richmond Assets & Holdings','Richmond Assets & Holdings'),
        ('US Home Exterior','US Home Exterior'),('Pre Management Leicester LTD','Pre Management Leicester LTD'),('American Income Life','American Income Life'),
        ('Life Alarm Services','Life Alarm Services'),('ERI Global','ERI Global'),('Allen Consulting group','Allen Consulting group'),
        ('Jeffery Tan ','Jeffery Tan '),('Student Life','Student Life'),('Career Transition Specialist','Career Transition Specialist'),
        ('Golden Eye Tech CCTV','Golden Eye Tech CCTV'),('MOVEMENT INSURANCE','MOVEMENT INSURANCE'),('Nucleus Media','Nucleus Media'),
        ('PSECU','PSECU'),('Tentamus','Tentamus'),('L&D','L&D'),('Get A Rate','Get A Rate'),('Mayfair Acct and Wealth','Mayfair Acct and Wealth'),
        ('Superking','Superking'),('Millionaires Group','Millionaires Group'),('PROTOSTAR','PROTOSTAR'),('MESSE FRANKFURT','MESSE FRANKFURT'),
        ('System 4','System 4'),('Naffa Innovations Pvt Ltd','Naffa Innovations Pvt Ltd'),('Support Staff','Support Staff'),
        ('Quality Team', 'Quality Team')

                    )

    emp_desi_list=(
        ('CRO','CRO'),('Patrolling officer','Patrolling officer'),('AM','AM'),('Trainer','Trainer'),
        ('AD','AD'),('Manager','Manager'),('Service Delivery Manager','Service Delivery Manager'),
        ('CC Team','CC Team'),('BD','BD'),('MIS','MIS'),('Data Analyst','Data Analyst'),('Team Leader','Team Leader'),('QA','QA'),
        ('ATL','ATL'),('SME','SME')

                   )

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    emp_name = models.CharField(max_length=30)
    emp_id=models.IntegerField()
    emp_desi=models.CharField(max_length=50,choices=emp_desi_list)
    team=models.CharField(max_length=50,null=True)
    email=models.EmailField(default='emp@ecpl.com',null=True)

    process = models.CharField(max_length=100,null=True)
    team_lead = models.CharField(max_length=50)
    manager = models.CharField(max_length=50)
    am = models.CharField(max_length=50)


    def __str__(self):
        return self.emp_name

class ProfileCreatedByManagers(models.Model):
    emp_name = models.CharField(max_length=200)
    emp_id = models.CharField(max_length=200)
    created_by = models.CharField(max_length=200)
    created_date = models.CharField(max_length=200,null=True)


class Team(models.Model):

    team_list = (
        ('Noom', 'Noom'), ('Aadya Solutions', 'Aadya Solutions'), ('UPS CLP', 'UPS CLP'),
        ('Gardening Express', 'Gardening Express'),
        ('Maxwell Properties', 'Maxwell Properties'), ('Gubagoo', 'Gubagoo'),
        ('Digital Swiss Gold', 'Digital Swiss Gold'),
        ('Digital Signage', 'Digital Signage'), ('Success Systems', 'Success Systems'),
        ('Advancement Consulting ', 'Advancement Consulting'),
        ('Insalvage', 'Insalvage'), ('Medicare', 'Medicare'), ('Printerpix', 'Printerpix'),
        ('Printerpix Training', 'Printerpix Training'),
        ('First Look Appraisal', 'First Look Appraisal'), ('TCA Counseling Group', 'TCA Counseling Group'),
        ('Advit Sahdev Marketing', 'Advit Sahdev Marketing'),
        ('AKDY', 'AKDY'), ('AKDY Training', 'AKDY Training'), ('Monster Lead Group', 'Monster Lead Group'),
        ('Fame House', 'Fame House'),
        ('Lecanto Green coffee', 'Lecanto Green coffee'), ('Micro Distributing', 'Micro Distributing'),
        ('Aditya Birla', 'Aditya Birla'),
        ('Aditya Birla Cellulose', 'Aditya Birla Cellulose'),
        ('Aditya Birla Cellulose Training', 'Aditya Birla Cellulose Training'),
        ('City Security Services', 'City Security Services'), ('Active Sports Club', 'Active Sports Club'),
        ('Aditya Birla Sampling Team', 'Aditya Birla Sampling Team'),
        ('Aditya Birla Sampling Team Trainig', 'Aditya Birla Sampling Team Trainig'),
        ('Bigo - IMO Group Chat', 'Bigo - IMO Group Chat'),
        ('Bigo Monitor Team', 'Bigo Monitor Team'), ('Daniel Wellington', 'Daniel Wellington'),
        ('Option Matrix', 'Option Matrix'),
        ('Info Think LLC', 'Info Think LLC'), ('MT Cosmetics', 'MT Cosmetics'),
        ("Something's Brewing", "Something's Brewing"),
        ('WIT Digital', 'WIT Digital'), ('Sync Treasury LLC', 'Sync Treasury LLC'),
        ('SANA GAMING CONSULTING', 'SANA GAMING CONSULTING'),
        ('GrayStone LLC', 'GrayStone LLC'), ('Kaapi Machines', 'Kaapi Machines'),
        ('Richmond Assets & Holdings', 'Richmond Assets & Holdings'),
        ('US Home Exterior', 'US Home Exterior'), ('Pre Management Leicester LTD', 'Pre Management Leicester LTD'),
        ('American Income Life', 'American Income Life'),
        ('Life Alarm Services', 'Life Alarm Services'), ('ERI Global', 'ERI Global'),
        ('Allen Consulting group', 'Allen Consulting group'),
        ('Jeffery Tan ', 'Jeffery Tan '), ('Student Life', 'Student Life'),
        ('Career Transition Specialist', 'Career Transition Specialist'),
        ('Golden Eye Tech CCTV', 'Golden Eye Tech CCTV'), ('MOVEMENT INSURANCE', 'MOVEMENT INSURANCE'),
        ('Nucleus Media', 'Nucleus Media'),
        ('PSECU', 'PSECU'), ('Tentamus', 'Tentamus'), ('L&D', 'L&D'), ('Get A Rate', 'Get A Rate'),
        ('Mayfair Acct and Wealth', 'Mayfair Acct and Wealth'),
        ('Superking', 'Superking'), ('Millionaires Group', 'Millionaires Group'), ('PROTOSTAR', 'PROTOSTAR'),
        ('MESSE FRANKFURT', 'MESSE FRANKFURT'),
        ('System 4', 'System 4'), ('Naffa Innovations Pvt Ltd', 'Naffa Innovations Pvt Ltd'),
        ('Support Staff', 'Support Staff'),('Quality Team','Quality Team')

    )

    name=models.CharField(max_length=50,choices=team_list)
    #qa = models.ForeignKey(User,on_delete=models.CASCADE,related_name='qa',null=True)
    #manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='manager', null=True)
    #tl = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tl', null=True)

    def __str__(self):
        return self.name

class Process(models.Model):

    process_name=models.CharField(max_length=200)
    team=models.ForeignKey(Team,on_delete=models.CASCADE)


class Campaigns(models.Model):
    name = models.CharField(max_length=200,null=True)
    type = models.CharField(max_length=10,null=True)
    def __str__(self):
        return self.name


# Final Forms ----------------------- #

######## OUTBOUND #####################

class MonitoringFormLeadsAadhyaSolution(models.Model):
    process = models.CharField(default='AAdya', max_length=50)
    type = models.CharField(default='Outbound',max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.IntegerField()
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'





class AccutimeMonForm(models.Model):
    process = models.CharField(default='Accutime', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.IntegerField()
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'



class MonitoringFormLeadsAdvanceConsultants(models.Model):
    process = models.CharField(default='Advance Consultants', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class MonitoringFormLeadsAllenConsulting(models.Model):
    process = models.CharField(default='Allen Consulting', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'



class CamIndustrialMonForm(models.Model):
    process = models.CharField(default='Cam Industrial', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class CitizenCapitalMonForm(models.Model):
    process = models.CharField(default='Citizen Capital', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)
    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class MonitoringFormLeadsCitySecurity(models.Model):
    process = models.CharField(default='City Security', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'


class MonitoringFormLeadsCTS(models.Model):
    process = models.CharField(default='CTS', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)
    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'


class EmbassyLuxuryMonForm(models.Model):
    process = models.CharField(default='Embassy Luxury', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class MonitoringFormLeadsGetARates(models.Model):
    process = models.CharField(default='Get A Rates', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class GlydeAppMonForm(models.Model):
    process = models.CharField(default='Glyde App', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class GoldenEastMonForm(models.Model):
    process = models.CharField(default='Golden East', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'


class IbizMonForm(models.Model):
    process = models.CharField(default='Ibiz', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class IIBMonForm(models.Model):
    process = models.CharField(default='IIB', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class MonitoringFormLeadsInfothinkLLC(models.Model):
    process = models.CharField(default='Info Think LLC', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class MonitoringFormLeadsInsalvage(models.Model):
    process = models.CharField(default='Insalvage', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class JJStudioMonForm(models.Model):
    process = models.CharField(default='JJ Studio', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class KalkiFashions(models.Model):
    process = models.CharField(default='Kalki Fashions', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class MonitoringFormLeadsLouisville(models.Model):
    process = models.CharField(default='Louisville', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class MonitoringFormLeadsMedicare(models.Model):
    process = models.CharField(default='Medicare', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class MicroDistributingMonForm(models.Model):
    process = models.CharField(default='Micro Distributing', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class MillenniumScientificMonForm(models.Model):
    process = models.CharField(default='Millennium Scientific', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class MTCosmeticsMonForm(models.Model):
    process = models.CharField(default='MT Cosmetic', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class NavigatorBioMonForm(models.Model):
    process = models.CharField(default='Navigator Bio', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class OptimalStudentLoanMonForm(models.Model):
    process = models.CharField(default='Optimal Student Loan', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class ProtostarMonForm(models.Model):
    process = models.CharField(default='Protostar', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class MonitoringFormLeadsPSECU(models.Model):
    process = models.CharField(default='PSECU', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class QBIQMonForm(models.Model):
    process = models.CharField(default='QBIQ', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class RestaurentSolMonForm(models.Model):
    process = models.CharField(default='Restaurant Solution Group', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class RitBrainMonForm(models.Model):
    process = models.CharField(default='Ri8Brain', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class RoofWellMonForm(models.Model):
    process = models.CharField(default='Roof Well', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class ScalaMonForm(models.Model):
    process = models.CharField(default='Scala', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class SolarCampaignMonForm(models.Model):
    process = models.CharField(default='Solar Campaign', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class StandSpotMonForm(models.Model):
    process = models.CharField(default='Stand Spot', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class MonitoringFormLeadsSystem4(models.Model):
    process = models.CharField(default='System4', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class MonitoringFormLeadsTentamusFood(models.Model):
    process = models.CharField(default='Tentamus Food', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class MonitoringFormLeadsTentamusPet(models.Model):
    process = models.CharField(default='Tentamus Pet', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)


    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class TerraceoLeadMonForm(models.Model):
    process = models.CharField(default='Terraceo - Lead', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class UpfrontOnlineLLCMonform(models.Model):
    process = models.CharField(default='Upfront Online LLC', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class WTUMonForm(models.Model):
    process = models.CharField(default='WTU', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    softskill_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class YesHealthMolinaMonForm(models.Model):
    process = models.CharField(default='Yes Health Molina', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.IntegerField()

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class ZeroStressMarketingMonForm(models.Model):

    process = models.CharField(default='Zero Stress Marketing', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()

    # SoftSkills

    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()

    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class ABHindalcoOutboundMonForm(models.Model):

    process = models.CharField(default='AB Hindalco Outbound', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class AdityaBirlaOutboundMonForm(models.Model):

    process = models.CharField(default='Aditya Birla Outbound', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class AmerisaveoutboundMonForm(models.Model):

    process = models.CharField(default='Amerisave Outbound', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class BhagyaLakshmiOutbound(models.Model):

    process = models.CharField(default='BhagyaLakshmi Outbound', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'


class ClearViewOutboundMonForm(models.Model):

    process = models.CharField(default='Clear View Outbound', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class DanielWellingtonOutboundMonForm(models.Model):

    process = models.CharField(default='Daniel Wellington Outbound', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class DigitalSwissGoldOutboundMonForm(models.Model):

    process = models.CharField(default='Digital Swiss Gold Outbound', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'


class HealthyplusOutboundMonForm(models.Model):

    process = models.CharField(default='Healthyplus Outbound', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'


class MaxwellPropertiesOutboundMonForm(models.Model):

    process = models.CharField(default='Maxwell Properties', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class MovementofInsuranceOutboundMonForm(models.Model):

    process = models.CharField(default='Movement of Insurance', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class SterlingStrategiesOutboundMonForm(models.Model):

    process = models.CharField(default='Sterling Strategies', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class TonnCoaOutboundMonForm(models.Model):

    process = models.CharField(default='Tonn Coa Outbound', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'


class WitDigitalOutboundMonForm(models.Model):

    process = models.CharField(default='Wit Digital', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class PosTechOutboundMonForm(models.Model):

    process = models.CharField(default='PosTech', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class SchindlerMediaOutboundMonForm(models.Model):

    process = models.CharField(default='Schindler Media', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class UPSOutboundMonForm(models.Model):

    process = models.CharField(default='UPS', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class PickPackDeliveriesMonForm(models.Model):
    process = models.CharField(default='Pick Pack Deliveries', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class MarceloPerezMonForm(models.Model):
    process = models.CharField(default='Marcelo Perez', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class MedTechGroupOutboundMonForm(models.Model):
    process = models.CharField(default='MedTech Group Outbound', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class DigitalSignageOutboundMonForm(models.Model):
    process = models.CharField(default='Digital Signage', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'


class HiveIncubatorsOutboundMonForm(models.Model):
    process = models.CharField(default='Hive Incubators Outbound', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class KaapiMachinesOutboundMonForm(models.Model):
    process = models.CharField(default='Kaapi Machines Outbound', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class SomethingsBrewingOutboundMonForm(models.Model):
    process = models.CharField(default='Somethings Brewing Outbound', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class NaffaOutboundMonForm(models.Model):
    process = models.CharField(default='Naffa Outbound', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'


class JBNOutboundMonForm(models.Model):
    process = models.CharField(default='JBN', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'


class QuickAutoPartsOutboundMonForm(models.Model):
    process = models.CharField(default='Quick Auto Parts', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'


class ApexCommunicationsOutboundMonForm(models.Model):
    process = models.CharField(default='Apex Communications Inc', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class LawOfficesOutboundMonForm(models.Model):
    process = models.CharField(default='Law Offices of Robert and Geller', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class WokeUpEnergyOutboundMonForm(models.Model):
    process = models.CharField(default='Woke Up Energy', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class FinnesseMortgageOutboundMonForm(models.Model):
    process = models.CharField(default='Finnesse Mortgage Outbound', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class UnitedMortgageOutboundMonForm(models.Model):
    process = models.CharField(default='United Mortgage Outbound', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class CleanLivingHealthWellnessOutboundMonForm(models.Model):
    process = models.CharField(default='Clean-Living Health and Wellness', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class PractoOutboundMonForm(models.Model):
    process = models.CharField(default='Practo Outbound', max_length=50)
    type = models.CharField(default='Outbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.CharField(max_length=20)
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Opening and Closing
    oc_1 = models.IntegerField()
    oc_2 = models.IntegerField()
    oc_3 = models.IntegerField()
    # SoftSkills
    softskill_1 = models.IntegerField()
    softskill_2 = models.IntegerField()
    softskill_3 = models.IntegerField()
    softskill_4 = models.IntegerField()
    softskill_5 = models.IntegerField()
    # Business and Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    softskill_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

####################################
##############################################
##############################################
############### inbound ######################

class MasterMonitoringFormTonnCoaInboundCalls(models.Model):
    process = models.CharField(default='Tonn Coa Inbound', max_length=50)
    type = models.CharField(default='Inbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.IntegerField()
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'


class SomethingsBrewingInbound(models.Model):
    process = models.CharField(default='Somethings Brewing', max_length=50)
    type = models.CharField(default='Inbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration=models.IntegerField()
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class PrinterPixMasterMonitoringFormInboundCalls(models.Model):
    process = models.CharField(default='Printer Pix Inbound', max_length=50)
    type = models.CharField(default='Inbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'


class NuclusInboundCalls(models.Model):
    process = models.CharField(default='Nucleus Media', max_length=50)
    type = models.CharField(default='Inbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class NaffaInnovationsInboundCalls(models.Model):
    process = models.CharField(default='Naffa Innovations', max_length=50)
    type = models.CharField(default='Inbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'



class KappimachineInboundCalls(models.Model):
    process = models.CharField(default='Kappi machine', max_length=50)
    type = models.CharField(default='Inbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class HealthyplusInboundMonForm(models.Model):
    process = models.CharField(default='Healthyplus Inbound', max_length=50)
    type = models.CharField(default='Inbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class FinesseMortgageInboundMonForm(models.Model):
    process = models.CharField(default='Finesse Mortgage Inbound', max_length=50)
    type = models.CharField(default='Inbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'


class DigitalSwissGoldInboundMonForm(models.Model):
    process = models.CharField(default='Digital Swiss Gold Inbound', max_length=50)
    type = models.CharField(default='Inbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class DanielwellingtoInboundMonForm(models.Model):
    process = models.CharField(default='Daniel Wellington Inbound', max_length=50)
    type = models.CharField(default='Inbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'


class BhagyaLakshmiInboundMonForm(models.Model):
    process = models.CharField(default='BhagyaLakshmi Inbound', max_length=50)
    type = models.CharField(default='Inbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'


class AKDYInboundMonFormNew(models.Model):
    process = models.CharField(default='AKDY Inbound', max_length=50)
    type = models.CharField(default='Inbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'


class AdityaBirlainboundMonForm(models.Model):
    process = models.CharField(default='Aditya Birla Inbound', max_length=50)
    type = models.CharField(default='Inbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class ABHindalcoInboundMonForm(models.Model):
    process = models.CharField(default='AB Hindalco Inbound', max_length=50)
    type = models.CharField(default='Inbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'


class RainbowDiagnosticsInboundMonForm(models.Model):
    process = models.CharField(default='Rainbow Diagnostics', max_length=50)
    type = models.CharField(default='Inbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'


class DecentralizedVisionLTDInboundMonForm(models.Model):
    process = models.CharField(default='Decentralized Vision LTD', max_length=50)
    type = models.CharField(default='Inbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'


class IEDHHInboundMonForm(models.Model):
    process = models.CharField(default='IEDHH', max_length=50)
    type = models.CharField(default='Inbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'


class AmerisaveInboundMonForm(models.Model):
    process = models.CharField(default='Amerisave Inbound', max_length=50)
    type = models.CharField(default='Inbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class ClearViewInboundMonForms(models.Model):
    process = models.CharField(default='Clear View IT Inbound', max_length=50)
    type = models.CharField(default='Inbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'


class QuickAutoPartsInboundMonForms(models.Model):
    process = models.CharField(default='Quick Auto Parts Inbound', max_length=50)
    type = models.CharField(default='Inbound', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    call_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    call_duration = models.IntegerField()
    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

######################################################
############## Email/CHat ############################


class SuperPlayMonForm(models.Model):
    process = models.CharField(default='Super Play', max_length=50)
    type = models.CharField(default='Email - Chat', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration=models.IntegerField()
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'


class DanielWellinChatEmailMonForm(models.Model):
    process = models.CharField(default='Daniel Wellington - Chat - Email', max_length=50)
    type = models.CharField(default='Email - Chat', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone=models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration=models.IntegerField()
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total=models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class TerraceoChatEmailMonForm(models.Model):
    process = models.CharField(default='Terraceo - Chat - Email', max_length=50)
    type = models.CharField(default='Email - Chat', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration = models.IntegerField()
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class TonnChatsEmailNewMonForm(models.Model):
    process = models.CharField(default='Tonn Coa Chat Email', max_length=50)
    type = models.CharField(default='Email - Chat', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration = models.IntegerField()
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class PrinterPixMasterMonitoringFormChatsEmail(models.Model):
    process = models.CharField(default='Printer Pix Chat Email', max_length=50)
    type = models.CharField(default='Email - Chat', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration = models.IntegerField()
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name
    def snippet(self):
        return self.comments[:100] + '...'

class PractoMonForm(models.Model):
    process = models.CharField(default='Practo', max_length=50)
    type = models.CharField(default='Email - Chat', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration = models.IntegerField()
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class FurBabyMonForm(models.Model):
    process = models.CharField(default='Fur Baby', max_length=50)
    type = models.CharField(default='Email - Chat', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration = models.IntegerField()
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'



class AKDYEmailMonForm(models.Model):
    process = models.CharField(default='AKDY - Email', max_length=50)
    type = models.CharField(default='Email - Chat', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration = models.IntegerField()
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class AmerisaveEmailMonForm(models.Model):
    process = models.CharField(default='Amerisave Email', max_length=50)
    type = models.CharField(default='Email - Chat', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration = models.IntegerField()
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class ClearViewEmailMonForm(models.Model):
    process = models.CharField(default='Clear View Email', max_length=50)
    type = models.CharField(default='Email - Chat', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration = models.IntegerField()
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class FinesseMortgageEmailMonForm(models.Model):
    process = models.CharField(default='Finesse Mortgage Email', max_length=50)
    type = models.CharField(default='Email - Chat', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration = models.IntegerField()
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class DigitalSwissGoldEmailChatMonForm(models.Model):
    process = models.CharField(default='Digital Swiss Gold Email - Chat', max_length=50)
    type = models.CharField(default='Email - Chat', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration = models.IntegerField()
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class RainbowDiagnosticsEmailMonForm(models.Model):
    process = models.CharField(default='Rainbow Diagnostics Email', max_length=50)
    type = models.CharField(default='Email - Chat', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration = models.IntegerField()
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class HiveIncubatorEmailMonForm(models.Model):
    process = models.CharField(default='Hive Incubator', max_length=50)
    type = models.CharField(default='Email - Chat', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration = models.IntegerField()
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class MedTechGroupEmailMonForm(models.Model):
    process = models.CharField(default='MedTech Group Email', max_length=50)
    type = models.CharField(default='Email - Chat', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration = models.IntegerField()
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class Ri8BrainEmailMonForm(models.Model):
    process = models.CharField(default='Ri8 Brain Email', max_length=50)
    type = models.CharField(default='Email - Chat', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration = models.IntegerField()
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class ScalaEmailMonForm(models.Model):
    process = models.CharField(default='Scala Email', max_length=50)
    type = models.CharField(default='Email - Chat', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration = models.IntegerField()
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class KalkiFashionEmailMonForm(models.Model):
    process = models.CharField(default='kalki Fashion Email', max_length=50)
    type = models.CharField(default='Email - Chat', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration = models.IntegerField()
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'


class MaxwellEmailMonForm(models.Model):
    process = models.CharField(default='Maxwell Email', max_length=50)
    type = models.CharField(default='Email - Chat', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration = models.IntegerField()
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class TanaorJewelryEmailMonForm(models.Model):
    process = models.CharField(default='Tanaor Jewelry', max_length=50)
    type = models.CharField(default='Email - Chat', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration = models.IntegerField()
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class DecentralizedVisionEmailChatMonForm(models.Model):
    process = models.CharField(default='Decentralized Vision Email Chat', max_length=50)
    type = models.CharField(default='Email - Chat', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    customer_name = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration = models.IntegerField()
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()
    ce_5 = models.IntegerField()
    ce_6 = models.IntegerField()
    ce_7 = models.IntegerField()
    ce_8 = models.IntegerField()
    ce_9 = models.IntegerField()
    ce_10 = models.IntegerField()
    ce_11 = models.IntegerField()
    # Business
    business_1 = models.IntegerField()
    business_2 = models.IntegerField()
    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    ce_total = models.IntegerField(null=True)
    business_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

############################################################
#####  Noom Eva Noom POD ###################################

class ChatMonitoringFormEva(models.Model):
    process=models.CharField(default='Noom Eva',max_length=50)
    type = models.CharField(default='Email/Chat Other', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    ticket_no = models.CharField(max_length=50)
    trans_date = models.DateField()
    audit_date = models.DateField()

    campaign = models.CharField(max_length=100)
    evaluator = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)

    # mgt
    manager=models.CharField(max_length=50)
    manager_id=models.IntegerField()

    category = models.CharField(max_length=20)

    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()

    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)

    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class ChatMonitoringFormPodFather(models.Model):
    process = models.CharField(default='Noom POD', max_length=50)
    type = models.CharField(default='Email/Chat Other', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    ticket_no = models.CharField(max_length=50)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    evaluator = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)

    # mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Customer Experience
    ce_1 = models.IntegerField()
    ce_2 = models.IntegerField()
    ce_3 = models.IntegerField()
    ce_4 = models.IntegerField()

    # Compliance
    compliance_1 = models.IntegerField()
    compliance_2 = models.IntegerField()
    compliance_3 = models.IntegerField()
    compliance_4 = models.IntegerField()
    compliance_5 = models.IntegerField()
    compliance_6 = models.IntegerField()

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    ce_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)
    overall_score = models.IntegerField(null=True)

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

#############################################
############# FameHouse New #################

class FameHouseNewMonForm(models.Model):
    process = models.CharField(default='Fame House', max_length=50)
    type = models.CharField(default='Email/Chat Other', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    ticket_no = models.CharField(max_length=50)
    ticket_type = models.CharField(max_length=50)

    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)

    # Mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Immediate fails:
    compliance_1 = models.IntegerField(null=True)
    compliance_2 = models.IntegerField(null=True)
    compliance_3 = models.IntegerField(null=True)
    compliance_4 = models.IntegerField(null=True)
    compliance_5 = models.IntegerField(null=True)
    compliance_6 = models.IntegerField(null=True)

    #Opening
    opening_1 = models.CharField(max_length=10,null=True)
    opening_2 = models.CharField(max_length=10,null=True)
    opening_3 = models.CharField(max_length=10,null=True)

    #Customer Issue Resolution

    cir_1 = models.CharField(max_length=10,null=True)
    cir_2 = models.CharField(max_length=10,null=True)
    cir_3 = models.CharField(max_length=10,null=True)
    cir_4 = models.CharField(max_length=10,null=True)
    cir_5 = models.CharField(max_length=10,null=True)

    #Macro Usage
    macro_1 = models.CharField(max_length=10,null=True)
    macro_2 = models.CharField(max_length=10,null=True)

    #Formatting
    formatting_1 = models.CharField(max_length=10,null=True)
    formatting_2 = models.CharField(max_length=10,null=True)
    formatting_3 = models.CharField(max_length=10,null=True)

    #Documentation
    doc_1 = models.CharField(max_length=10,null=True)
    doc_2 = models.CharField(max_length=10,null=True)
    doc_3 = models.CharField(max_length=10,null=True)
    doc_4 = models.CharField(max_length=10,null=True)

    #Etiquette
    et_1 = models.CharField(max_length=10,null=True)
    et_2 = models.CharField(max_length=10,null=True)
    et_3 = models.CharField(max_length=10,null=True)
    et_4 = models.CharField(max_length=10,null=True)

    #Closing
    closing_1 = models.CharField(max_length=10,null=True)
    closing_2 = models.CharField(max_length=10,null=True)

    closing_total = models.IntegerField(null=True)
    et_total = models.IntegerField(null=True)
    doc_total = models.IntegerField(null=True)
    formatting_total = models.IntegerField(null=True)
    macro_total = models.IntegerField(null=True)
    cir_total = models.IntegerField(null=True)
    opening_total = models.IntegerField(null=True)
    compliance_total = models.IntegerField(null=True)

    overall_score = models.IntegerField(null=True)

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    am = models.CharField(max_length=50,null=True)
    week=models.CharField(max_length=20,null=True)
    ##############
    fatal=models.BooleanField(default=False)
    fatal_count=models.IntegerField(default=0)

    disput_status=models.BooleanField(default=False)


    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

#############################################
############### FLA #########################

class FLAMonitoringForm(models.Model):
    process = models.CharField(default='FLA', max_length=50)
    type = models.CharField(default='FLA', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    order_id = models.CharField(max_length=50)
    check_list = models.CharField(max_length=400)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    service = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)

    # Mgt
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    category = models.CharField(max_length=20)

    # Checklist
    checklist_1 = models.IntegerField()

    reason_for_failure = models.TextField()
    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()

    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)

    overall_score = models.IntegerField()

    am = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=20,null=True)
    ##############
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'



############### Practo New Version1.1 #################

class PractoNewVersion(models.Model):
    process = models.CharField(default='Practo', max_length=50)
    type = models.CharField(default='Practo', max_length=50)
    emp_id = models.IntegerField()
    associate_name = models.CharField(max_length=50)
    qa = models.CharField(max_length=50)
    team_lead = models.CharField(max_length=50)
    conversation_id = models.CharField(max_length=50)
    customer_contact = models.CharField(max_length=100)
    trans_date = models.DateField()
    audit_date = models.DateField()
    campaign = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    concept = models.CharField(max_length=60)
    duration = models.IntegerField()
    manager = models.CharField(max_length=50)
    manager_id = models.IntegerField()
    category = models.CharField(max_length=20)
    # Customer Experience
    p_1 = models.IntegerField()
    p_2 = models.IntegerField()
    p_3 = models.IntegerField()
    p_4 = models.IntegerField()
    p_5 = models.IntegerField()
    p_6 = models.IntegerField()
    p_7 = models.IntegerField()
    p_8 = models.IntegerField()
    p_9 = models.IntegerField()
    p_10 = models.IntegerField()
    p_11 = models.IntegerField()
    p_12 = models.IntegerField()
    p_13 = models.IntegerField()
    p_14 = models.IntegerField()
    p_15 = models.IntegerField()
    p_16 = models.IntegerField()
    p_17 = models.IntegerField()
    p_18 = models.IntegerField()
    p_19 = models.IntegerField()

    compliance_1 = models.CharField(max_length=30)
    compliance_2 = models.CharField(max_length=30)

    areas_improvement = models.TextField()
    positives = models.TextField()
    comments = models.TextField()
    added_by = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    # Training >> only for practo Now
    training = models.CharField(max_length=20, default='No')

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'

class GubagooAuditForm(models.Model):

    process = models.CharField(default='Gubagoo', max_length=50)
    type = models.CharField(default='Gubagoo', max_length=50)
    emp_id = models.IntegerField(null=True)
    associate_name = models.CharField(max_length=50, null=True)
    qa = models.CharField(max_length=50, null=True)
    team_lead = models.CharField(max_length=50, null=True)
    trans_date = models.DateField(null=True)
    audit_date = models.DateField(null=True)
    campaign = models.CharField(max_length=100, null=True)
    zone = models.CharField(max_length=50, null=True)
    concept = models.CharField(max_length=60, null=True)
    manager = models.CharField(max_length=50, null=True)
    manager_id = models.IntegerField(null=True)
    category = models.CharField(max_length=20, null=True)

    chat1_id = models.CharField(max_length=50, null=True)
    chat2_id = models.CharField(max_length=50, null=True)
    chat3_id = models.CharField(max_length=50, null=True)
    chat4_id = models.CharField(max_length=50, null=True)
    chat5_id = models.CharField(max_length=50, null=True)
    chat6_id = models.CharField(max_length=50, null=True)

    cat1chat1 = models.CharField(max_length=10, null=True)
    cat1chat2 = models.CharField(max_length=10, null=True)
    cat1chat3 = models.CharField(max_length=10, null=True)
    cat1chat4 = models.CharField(max_length=10, null=True)
    cat1chat5 = models.CharField(max_length=10, null=True)
    cat1chat6 = models.CharField(max_length=10, null=True)

    cat2chat1 = models.CharField(max_length=10, null=True)
    cat2chat2 = models.CharField(max_length=10, null=True)
    cat2chat3 = models.CharField(max_length=10, null=True)
    cat2chat4 = models.CharField(max_length=10, null=True)
    cat2chat5 = models.CharField(max_length=10, null=True)
    cat2chat6 = models.CharField(max_length=10, null=True)

    cat3chat1 = models.CharField(max_length=10, null=True)
    cat3chat2 = models.CharField(max_length=10, null=True)
    cat3chat3 = models.CharField(max_length=10, null=True)
    cat3chat4 = models.CharField(max_length=10, null=True)
    cat3chat5 = models.CharField(max_length=10, null=True)
    cat3chat6 = models.CharField(max_length=10, null=True)

    cat4chat1 = models.CharField(max_length=10, null=True)
    cat4chat2 = models.CharField(max_length=10, null=True)
    cat4chat3 = models.CharField(max_length=10, null=True)
    cat4chat4 = models.CharField(max_length=10, null=True)
    cat4chat5 = models.CharField(max_length=10, null=True)
    cat4chat6 = models.CharField(max_length=10, null=True)

    cat5chat1 = models.CharField(max_length=10, null=True)
    cat5chat2 = models.CharField(max_length=10, null=True)
    cat5chat3 = models.CharField(max_length=10, null=True)
    cat5chat4 = models.CharField(max_length=10, null=True)
    cat5chat5 = models.CharField(max_length=10, null=True)
    cat5chat6 = models.CharField(max_length=10, null=True)

    cat6chat1 = models.CharField(max_length=10, null=True)
    cat6chat2 = models.CharField(max_length=10, null=True)
    cat6chat3 = models.CharField(max_length=10, null=True)
    cat6chat4 = models.CharField(max_length=10, null=True)
    cat6chat5 = models.CharField(max_length=10, null=True)
    cat6chat6 = models.CharField(max_length=10, null=True)

    cat7chat1 = models.CharField(max_length=10, null=True)
    cat7chat2 = models.CharField(max_length=10, null=True)
    cat7chat3 = models.CharField(max_length=10, null=True)
    cat7chat4 = models.CharField(max_length=10, null=True)
    cat7chat5 = models.CharField(max_length=10, null=True)
    cat7chat6 = models.CharField(max_length=10, null=True)

    cat8chat1 = models.CharField(max_length=10, null=True)
    cat8chat2 = models.CharField(max_length=10, null=True)
    cat8chat3 = models.CharField(max_length=10, null=True)
    cat8chat4 = models.CharField(max_length=10, null=True)
    cat8chat5 = models.CharField(max_length=10, null=True)
    cat8chat6 = models.CharField(max_length=10, null=True)

    cat9chat1 = models.CharField(max_length=10, null=True)
    cat9chat2 = models.CharField(max_length=10, null=True)
    cat9chat3 = models.CharField(max_length=10, null=True)
    cat9chat4 = models.CharField(max_length=10, null=True)
    cat9chat5 = models.CharField(max_length=10, null=True)
    cat9chat6 = models.CharField(max_length=10, null=True)

    cat10chat1 = models.CharField(max_length=10, null=True)
    cat10chat2 = models.CharField(max_length=10, null=True)
    cat10chat3 = models.CharField(max_length=10, null=True)
    cat10chat4 = models.CharField(max_length=10, null=True)
    cat10chat5 = models.CharField(max_length=10, null=True)
    cat10chat6 = models.CharField(max_length=10, null=True)

    cat11chat1 = models.CharField(max_length=10, null=True)
    cat11chat2 = models.CharField(max_length=10, null=True)
    cat11chat3 = models.CharField(max_length=10, null=True)
    cat11chat4 = models.CharField(max_length=10, null=True)
    cat11chat5 = models.CharField(max_length=10, null=True)
    cat11chat6 = models.CharField(max_length=10, null=True)

    cat12chat1 = models.CharField(max_length=10, null=True)
    cat12chat2 = models.CharField(max_length=10, null=True)
    cat12chat3 = models.CharField(max_length=10, null=True)
    cat12chat4 = models.CharField(max_length=10, null=True)
    cat12chat5 = models.CharField(max_length=10, null=True)
    cat12chat6 = models.CharField(max_length=10, null=True)

    cat13chat1 = models.CharField(max_length=10, null=True)
    cat13chat2 = models.CharField(max_length=10, null=True)
    cat13chat3 = models.CharField(max_length=10, null=True)
    cat13chat4 = models.CharField(max_length=10, null=True)
    cat13chat5 = models.CharField(max_length=10, null=True)
    cat13chat6 = models.CharField(max_length=10, null=True)

    cat14chat1 = models.CharField(max_length=10, null=True)
    cat14chat2 = models.CharField(max_length=10, null=True)
    cat14chat3 = models.CharField(max_length=10, null=True)
    cat14chat4 = models.CharField(max_length=10, null=True)
    cat14chat5 = models.CharField(max_length=10, null=True)
    cat14chat6 = models.CharField(max_length=10, null=True)

    cat15chat1 = models.CharField(max_length=10, null=True)
    cat15chat2 = models.CharField(max_length=10, null=True)
    cat15chat3 = models.CharField(max_length=10, null=True)
    cat15chat4 = models.CharField(max_length=10, null=True)
    cat15chat5 = models.CharField(max_length=10, null=True)
    cat15chat6 = models.CharField(max_length=10, null=True)

    cat16chat1 = models.CharField(max_length=10, null=True)
    cat16chat2 = models.CharField(max_length=10, null=True)
    cat16chat3 = models.CharField(max_length=10, null=True)
    cat16chat4 = models.CharField(max_length=10, null=True)
    cat16chat5 = models.CharField(max_length=10, null=True)
    cat16chat6 = models.CharField(max_length=10, null=True)

    cat1fscore = models.FloatField(null=True)
    cat2fscore = models.FloatField(null=True)
    cat3fscore = models.FloatField(null=True)
    cat4fscore = models.FloatField(null=True)
    cat5fscore = models.FloatField(null=True)
    cat6fscore = models.FloatField(null=True)
    cat7fscore = models.FloatField(null=True)
    cat8fscore = models.FloatField(null=True)
    cat9fscore = models.FloatField(null=True)
    cat10fscore = models.FloatField(null=True)
    cat11fscore = models.FloatField(null=True)
    cat13fscore = models.FloatField(null=True)
    cat14fscore = models.FloatField(null=True)
    cat15fscore = models.FloatField(null=True)

    total_failing_score = models.FloatField(null=True)

    cat1score = models.FloatField(null=True)
    cat2score = models.FloatField(null=True)
    cat3score = models.FloatField(null=True)
    cat4score = models.FloatField(null=True)
    cat5score = models.FloatField(null=True)
    cat6score = models.FloatField(null=True)
    cat7score = models.FloatField(null=True)
    cat8score = models.FloatField(null=True)
    cat9score = models.FloatField(null=True)
    cat10score = models.FloatField(null=True)
    cat11score = models.FloatField(null=True)
    cat12score = models.FloatField(null=True)
    cat13score = models.FloatField(null=True)
    cat14score = models.FloatField(null=True)
    cat15score = models.FloatField(null=True)

    cat1chat1cs = models.TextField(null=True)
    cat1chat2cs = models.TextField(null=True)
    cat1chat3cs = models.TextField(null=True)
    cat1chat4cs = models.TextField(null=True)
    cat1chat5cs = models.TextField(null=True)
    cat1chat6cs = models.TextField(null=True)

    cat1chat1cy = models.TextField(null=True)
    cat1chat2cy = models.TextField(null=True)
    cat1chat3cy = models.TextField(null=True)
    cat1chat4cy = models.TextField(null=True)
    cat1chat5cy = models.TextField(null=True)
    cat1chat6cy = models.TextField(null=True)

    cat2chat1cs = models.TextField(null=True)
    cat2chat2cs = models.TextField(null=True)
    cat2chat3cs = models.TextField(null=True)
    cat2chat4cs = models.TextField(null=True)
    cat2chat5cs = models.TextField(null=True)
    cat2chat6cs = models.TextField(null=True)

    cat2chat1cy = models.TextField(null=True)
    cat2chat2cy = models.TextField(null=True)
    cat2chat3cy = models.TextField(null=True)
    cat2chat4cy = models.TextField(null=True)
    cat2chat5cy = models.TextField(null=True)
    cat2chat6cy = models.TextField(null=True)

    cat3chat1cs = models.TextField(null=True)
    cat3chat2cs = models.TextField(null=True)
    cat3chat3cs = models.TextField(null=True)
    cat3chat4cs = models.TextField(null=True)
    cat3chat5cs = models.TextField(null=True)
    cat3chat6cs = models.TextField(null=True)

    cat3chat1cy = models.TextField(null=True)
    cat3chat2cy = models.TextField(null=True)
    cat3chat3cy = models.TextField(null=True)
    cat3chat4cy = models.TextField(null=True)
    cat3chat5cy = models.TextField(null=True)
    cat3chat6cy = models.TextField(null=True)

    cat4chat1cs = models.TextField(null=True)
    cat4chat2cs = models.TextField(null=True)
    cat4chat3cs = models.TextField(null=True)
    cat4chat4cs = models.TextField(null=True)
    cat4chat5cs = models.TextField(null=True)
    cat4chat6cs = models.TextField(null=True)

    cat4chat1cy = models.TextField(null=True)
    cat4chat2cy = models.TextField(null=True)
    cat4chat3cy = models.TextField(null=True)
    cat4chat4cy = models.TextField(null=True)
    cat4chat5cy = models.TextField(null=True)
    cat4chat6cy = models.TextField(null=True)

    cat5chat1cs = models.TextField(null=True)
    cat5chat2cs = models.TextField(null=True)
    cat5chat3cs = models.TextField(null=True)
    cat5chat4cs = models.TextField(null=True)
    cat5chat5cs = models.TextField(null=True)
    cat5chat6cs = models.TextField(null=True)

    cat5chat1cy = models.TextField(null=True)
    cat5chat2cy = models.TextField(null=True)
    cat5chat3cy = models.TextField(null=True)
    cat5chat4cy = models.TextField(null=True)
    cat5chat5cy = models.TextField(null=True)
    cat5chat6cy = models.TextField(null=True)

    cat6chat1cs = models.TextField(null=True)
    cat6chat2cs = models.TextField(null=True)
    cat6chat3cs = models.TextField(null=True)
    cat6chat4cs = models.TextField(null=True)
    cat6chat5cs = models.TextField(null=True)
    cat6chat6cs = models.TextField(null=True)

    cat6chat1cy = models.TextField(null=True)
    cat6chat2cy = models.TextField(null=True)
    cat6chat3cy = models.TextField(null=True)
    cat6chat4cy = models.TextField(null=True)
    cat6chat5cy = models.TextField(null=True)
    cat6chat6cy = models.TextField(null=True)

    cat7chat1cs = models.TextField(null=True)
    cat7chat2cs = models.TextField(null=True)
    cat7chat3cs = models.TextField(null=True)
    cat7chat4cs = models.TextField(null=True)
    cat7chat5cs = models.TextField(null=True)
    cat7chat6cs = models.TextField(null=True)

    cat7chat1cy = models.TextField(null=True)
    cat7chat2cy = models.TextField(null=True)
    cat7chat3cy = models.TextField(null=True)
    cat7chat4cy = models.TextField(null=True)
    cat7chat5cy = models.TextField(null=True)
    cat7chat6cy = models.TextField(null=True)

    cat8chat1cs = models.TextField(null=True)
    cat8chat2cs = models.TextField(null=True)
    cat8chat3cs = models.TextField(null=True)
    cat8chat4cs = models.TextField(null=True)
    cat8chat5cs = models.TextField(null=True)
    cat8chat6cs = models.TextField(null=True)

    cat8chat1cy = models.TextField(null=True)
    cat8chat2cy = models.TextField(null=True)
    cat8chat3cy = models.TextField(null=True)
    cat8chat4cy = models.TextField(null=True)
    cat8chat5cy = models.TextField(null=True)
    cat8chat6cy = models.TextField(null=True)

    cat9chat1cs = models.TextField(null=True)
    cat9chat2cs = models.TextField(null=True)
    cat9chat3cs = models.TextField(null=True)
    cat9chat4cs = models.TextField(null=True)
    cat9chat5cs = models.TextField(null=True)
    cat9chat6cs = models.TextField(null=True)

    cat9chat1cy = models.TextField(null=True)
    cat9chat2cy = models.TextField(null=True)
    cat9chat3cy = models.TextField(null=True)
    cat9chat4cy = models.TextField(null=True)
    cat9chat5cy = models.TextField(null=True)
    cat9chat6cy = models.TextField(null=True)

    cat10chat1cs = models.TextField(null=True)
    cat10chat2cs = models.TextField(null=True)
    cat10chat3cs = models.TextField(null=True)
    cat10chat4cs = models.TextField(null=True)
    cat10chat5cs = models.TextField(null=True)
    cat10chat6cs = models.TextField(null=True)

    cat10chat1cy = models.TextField(null=True)
    cat10chat2cy = models.TextField(null=True)
    cat10chat3cy = models.TextField(null=True)
    cat10chat4cy = models.TextField(null=True)
    cat10chat5cy = models.TextField(null=True)
    cat10chat6cy = models.TextField(null=True)

    cat11chat1cs = models.TextField(null=True)
    cat11chat2cs = models.TextField(null=True)
    cat11chat3cs = models.TextField(null=True)
    cat11chat4cs = models.TextField(null=True)
    cat11chat5cs = models.TextField(null=True)
    cat11chat6cs = models.TextField(null=True)

    cat11chat1cy = models.TextField(null=True)
    cat11chat2cy = models.TextField(null=True)
    cat11chat3cy = models.TextField(null=True)
    cat11chat4cy = models.TextField(null=True)
    cat11chat5cy = models.TextField(null=True)
    cat11chat6cy = models.TextField(null=True)

    cat12chat1cs = models.TextField(null=True)
    cat12chat2cs = models.TextField(null=True)
    cat12chat3cs = models.TextField(null=True)
    cat12chat4cs = models.TextField(null=True)
    cat12chat5cs = models.TextField(null=True)
    cat12chat6cs = models.TextField(null=True)

    cat12chat1cy = models.TextField(null=True)
    cat12chat2cy = models.TextField(null=True)
    cat12chat3cy = models.TextField(null=True)
    cat12chat4cy = models.TextField(null=True)
    cat12chat5cy = models.TextField(null=True)
    cat12chat6cy = models.TextField(null=True)

    cat13chat1cs = models.TextField(null=True)
    cat13chat2cs = models.TextField(null=True)
    cat13chat3cs = models.TextField(null=True)
    cat13chat4cs = models.TextField(null=True)
    cat13chat5cs = models.TextField(null=True)
    cat13chat6cs = models.TextField(null=True)

    cat13chat1cy = models.TextField(null=True)
    cat13chat2cy = models.TextField(null=True)
    cat13chat3cy = models.TextField(null=True)
    cat13chat4cy = models.TextField(null=True)
    cat13chat5cy = models.TextField(null=True)
    cat13chat6cy = models.TextField(null=True)

    cat14chat1cs = models.TextField(null=True)
    cat14chat2cs = models.TextField(null=True)
    cat14chat3cs = models.TextField(null=True)
    cat14chat4cs = models.TextField(null=True)
    cat14chat5cs = models.TextField(null=True)
    cat14chat6cs = models.TextField(null=True)

    cat14chat1cy = models.TextField(null=True)
    cat14chat2cy = models.TextField(null=True)
    cat14chat3cy = models.TextField(null=True)
    cat14chat4cy = models.TextField(null=True)
    cat14chat5cy = models.TextField(null=True)
    cat14chat6cy = models.TextField(null=True)

    cat15chat1cs = models.TextField(null=True)
    cat15chat2cs = models.TextField(null=True)
    cat15chat3cs = models.TextField(null=True)
    cat15chat4cs = models.TextField(null=True)
    cat15chat5cs = models.TextField(null=True)
    cat15chat6cs = models.TextField(null=True)

    cat15chat1cy = models.TextField(null=True)
    cat15chat2cy = models.TextField(null=True)
    cat15chat3cy = models.TextField(null=True)
    cat15chat4cy = models.TextField(null=True)
    cat15chat5cy = models.TextField(null=True)
    cat15chat6cy = models.TextField(null=True)

    cat16chat1cs = models.TextField(null=True)
    cat16chat2cs = models.TextField(null=True)
    cat16chat3cs = models.TextField(null=True)
    cat16chat4cs = models.TextField(null=True)
    cat16chat5cs = models.TextField(null=True)
    cat16chat6cs = models.TextField(null=True)

    cat16chat1cy = models.TextField(null=True)
    cat16chat2cy = models.TextField(null=True)
    cat16chat3cy = models.TextField(null=True)
    cat16chat4cy = models.TextField(null=True)
    cat16chat5cy = models.TextField(null=True)
    cat16chat6cy = models.TextField(null=True)

    chat1_total_score = models.IntegerField(null=True)
    chat2_total_score = models.IntegerField(null=True)
    chat3_total_score = models.IntegerField(null=True)
    chat4_total_score = models.IntegerField(null=True)
    chat5_total_score = models.IntegerField(null=True)
    chat6_total_score = models.IntegerField(null=True)

    total_failing_perc = models.IntegerField(null=True)
    added_by = models.CharField(max_length=30,null=True)
    status = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True)
    emp_comments = models.TextField(null=True)
    overall_score = models.IntegerField(null=True)
    am = models.CharField(max_length=50, null=True)
    week = models.CharField(max_length=20, null=True)
    fatal = models.BooleanField(default=False)
    fatal_count = models.IntegerField(default=0)
    disput_status = models.BooleanField(default=False)

    def __str__(self):
        return self.associate_name

    def snippet(self):
        return self.comments[:100] + '...'



############# End of Forms ##############################

class Empdata(models.Model):
    uid=models.IntegerField(unique=True)
    username=models.IntegerField()
    password=models.CharField(max_length=30)


class ProfileNewtoAddUserandProfile(models.Model):
    username = models.IntegerField()
    password = models.CharField(max_length=30)
    emp_name = models.CharField(max_length=30)
    emp_id = models.IntegerField()
    emp_desi = models.CharField(max_length=50)
    team = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    process = models.CharField(max_length=100)
    team_lead = models.CharField(max_length=50)
    manager = models.CharField(max_length=50)
    am = models.CharField(max_length=50)

    def __str__(self):
        return self.emp_name





class latest(models.Model):
    ser = models.IntegerField()

class ABCprofile(models.Model):
    emp_id = models.IntegerField()
    manager = models.CharField(max_length=100)
    am = models.CharField(max_length=100)
    tl = models.CharField(max_length=100)
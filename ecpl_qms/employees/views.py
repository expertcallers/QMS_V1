from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.template.loader import get_template
import django_pivot.pivot
from django.core.mail import send_mail, EmailMessage
from django.db.models import Count,Avg,Sum
import xlwt
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from . import forms

list_of_monforms = [ # OutBound
                        MonitoringFormLeadsAadhyaSolution,AccutimeMonForm,MonitoringFormLeadsAdvanceConsultants,
                        MonitoringFormLeadsAllenConsulting,CamIndustrialMonForm,CitizenCapitalMonForm,MonitoringFormLeadsCitySecurity,
                        MonitoringFormLeadsCTS,EmbassyLuxuryMonForm,MonitoringFormLeadsGetARates,GlydeAppMonForm,GoldenEastMonForm,IbizMonForm,
                        IIBMonForm,MonitoringFormLeadsInfothinkLLC,MonitoringFormLeadsInsalvage,JJStudioMonForm,KalkiFashions,MonitoringFormLeadsLouisville,
                        MonitoringFormLeadsMedicare,MicroDistributingMonForm,MillenniumScientificMonForm,MTCosmeticsMonForm,NavigatorBioMonForm,OptimalStudentLoanMonForm,
                        ProtostarMonForm,MonitoringFormLeadsPSECU,QBIQMonForm,RestaurentSolMonForm,RitBrainMonForm,
                        RoofWellMonForm,ScalaMonForm,SolarCampaignMonForm,StandSpotMonForm,MonitoringFormLeadsSystem4,MonitoringFormLeadsTentamusFood,MonitoringFormLeadsTentamusPet,
                        TerraceoLeadMonForm,UpfrontOnlineLLCMonform,WTUMonForm,YesHealthMolinaMonForm,ZeroStressMarketingMonForm,
                        ABHindalcoOutboundMonForm,AdityaBirlaOutboundMonForm,AmerisaveoutboundMonForm,BhagyaLakshmiOutbound,
                        ClearViewOutboundMonForm,DanielWellingtonOutboundMonForm,DigitalSwissGoldOutboundMonForm,HealthyplusOutboundMonForm,
                        MaxwellPropertiesOutboundMonForm,MovementofInsuranceOutboundMonForm,SterlingStrategiesOutboundMonForm,TonnCoaOutboundMonForm,WitDigitalOutboundMonForm,
                        PosTechOutboundMonForm,SchindlerMediaOutboundMonForm,UPSOutboundMonForm,
                        PickPackDeliveriesMonForm,MarceloPerezMonForm,MedTechGroupOutboundMonForm,DigitalSignageOutboundMonForm,
                        HiveIncubatorsOutboundMonForm,KaapiMachinesOutboundMonForm,SomethingsBrewingOutboundMonForm,NaffaOutboundMonForm,JBNOutboundMonForm,
                        QuickAutoPartsOutboundMonForm,
                        ApexCommunicationsOutboundMonForm,LawOfficesOutboundMonForm,WokeUpEnergyOutboundMonForm,
                        FinnesseMortgageOutboundMonForm,
                        UnitedMortgageOutboundMonForm,

                        # Inbound
                        MasterMonitoringFormTonnCoaInboundCalls,SomethingsBrewingInbound,PrinterPixMasterMonitoringFormInboundCalls,
                        NuclusInboundCalls,NaffaInnovationsInboundCalls,KappimachineInboundCalls,HealthyplusInboundMonForm,
                        FinesseMortgageInboundMonForm,DigitalSwissGoldInboundMonForm,DanielwellingtoInboundMonForm,BhagyaLakshmiInboundMonForm,
                        AKDYInboundMonFormNew,AdityaBirlainboundMonForm,ABHindalcoInboundMonForm,
                        RainbowDiagnosticsInboundMonForm,DecentralizedVisionLTDInboundMonForm,
                        AmerisaveInboundMonForm,IEDHHInboundMonForm,ClearViewInboundMonForms,QuickAutoPartsInboundMonForms,

                        # Email/CHat
                        SuperPlayMonForm,DanielWellinChatEmailMonForm,TerraceoChatEmailMonForm,TonnChatsEmailNewMonForm,
                        PrinterPixMasterMonitoringFormChatsEmail,PractoMonForm,FurBabyMonForm,AKDYEmailMonForm,AmerisaveEmailMonForm,
                        ClearViewEmailMonForm,FinesseMortgageEmailMonForm,DigitalSwissGoldEmailChatMonForm,
                        RainbowDiagnosticsEmailMonForm,HiveIncubatorEmailMonForm,MedTechGroupEmailMonForm,
                        Ri8BrainEmailMonForm,ScalaEmailMonForm,KalkiFashionEmailMonForm,MaxwellEmailMonForm,
                        TanaorJewelryEmailMonForm,DecentralizedVisionEmailChatMonForm,

                        #FLA
                        FLAMonitoringForm,

                        #Noom
                        ChatMonitoringFormEva,ChatMonitoringFormPodFather,

                        #FameHouse
                        FameHouseNewMonForm

                        ]


#Index
def index(request):
    return render(request,'index.html')
#Okay

#Guidelines
def outboundGuidelines(request):
    return render(request,'guidelines/outbound.html')
def inboundGuidelines(request):
    return render(request,'guidelines/inbound.html')
def chatGuidelines(request):
    return render(request,'guidelines/chat.html')
def emailGuidelines(request):
    return render(request,'guidelines/email.html')
#Okay

# Reistration, Sign up, Login, Logout, Change Password

def signup(request):
    team_leaders=Profile.objects.filter(emp_desi='Team Leader')
    managers=Profile.objects.filter(emp_desi='Manager')
    ams = Profile.objects.filter(emp_desi='AM')

    if request.method == 'POST':
        admin_id = request.POST['admin-id']
        admin_pwd = request.POST['admin-pwd']

        form = UserCreationForm(request.POST)  # form to create user
        profile_form = forms.ProfileCreation(request.POST, request.FILES)

        if form.is_valid() and profile_form.is_valid():
            # Admin ID PWD validation
            if admin_id=='ecpl-qms' and admin_pwd=='500199':

                manager=request.POST['manager']
                team_lead=request.POST['team-leader']
                am=request.POST['am']

                user = form.save()
                profile = profile_form.save(commit=False)

                profile.user = user
                profile.manager=manager
                profile.team_lead=team_lead
                profile.am=am

                profile.save()
                # login(request,user)
                return render(request,'index.html')
            else:
                messages.info(request, 'Invalid Admin Credentials !')
                return render(request,'sign-up.html',{'form': form, 'profile_form': profile_form})
    else:
        form = UserCreationForm()
        profile_form = forms.ProfileCreation()

    return render(request, 'sign-up.html', {'form': form, 'profile_form': profile_form,
                                            'team_leaders':team_leaders,'managers':managers,'ams':ams
                                            })

#Okay

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)  # Login form
        if form.is_valid():

            # login the user
            user = form.get_user()
            login(request, user)

            # redirecting
            if user.profile.emp_desi=='QA':
                return redirect('/employees/qahome')
            elif user.profile.emp_desi=='Manager' or user.profile.emp_desi=='AM' or user.profile.emp_desi=='Trainer' or user.profile.emp_id==224 or user.profile.emp_id==6479 or user.profile.emp_desi=='Team Leader':
                return redirect('/employees/manager-home')
            # Special Access ##########
            elif user.profile.emp_id==3495 or user.profile.emp_id== 2922:
                return redirect('/employees/manager-home')
            elif user.profile.emp_desi=='CRO' or user.profile.emp_desi=='Patrolling officer':
                return redirect('/employees/agenthome')
            else:
                form = AuthenticationForm()
                messages.info(request, 'Please Contact Admin !')
                return render(request, 'login.html', {'form': form})

        else:
            form = AuthenticationForm()
            messages.info(request,'Invalid Credentials !')
            return render(request,'login.html',{'form':form})
    else:
        logout(request)
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
#Okay
def logout_view(request):
    logout(request)
    return redirect('/employees/login')
#Okay

# Password Reset
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            logout(request)
            return render(request,'login.html')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})


def updateEmailAddress(request,pk):

    if request.method=='POST':
        emp_id=pk
        email_1=request.POST['email1']
        email_2 = request.POST['email2']
        if email_1 == email_2 :
            profile_obj=Profile.objects.get(emp_id=emp_id)
            profile_obj.email=email_2
            profile_obj.save()
            messages.success(request,'Email Address Updated Successfully ! Please login back')
            return redirect('/logout')
        else:
            messages.error(request,'Email Address Mismatching')
            return render(request, 'update-email.html')
    else:
        return render(request,'update-email.html')

#Done


def employeeWiseReport(request):

    if request.method == 'POST':

        currentMonth = request.POST['month']
        currentYear = request.POST['year']
        emp_id = request.POST['emp_id']
        profile=Profile.objects.get(emp_id=emp_id)
        # Mon Form List
        associate_data=[]
        associate_data_fatal=[]
        associate_data_errors=[]

        #### Avg Score Overall ####

        avgs = []

        def avgScoreTotal(monform):
            avg_score_all = monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,
                                                   emp_id=emp_id).aggregate(davg=Avg('overall_score'))
            if avg_score_all['davg'] != None:
                avgs.append(avg_score_all['davg'])

        for i in list_of_monforms:
            avgScoreTotal(i)
        if len(avgs)>0:
            total_score = sum(avgs) / len(avgs)
        else:
            total_score = 100
        avg_score = round(total_score, 2)

        # Score in All forms
        for i in list_of_monforms:
            coaching = i.objects.filter(emp_id=emp_id, audit_date__year=currentYear,
                                        audit_date__month=currentMonth)
            if coaching.count() > 0:

                emp_wise = i.objects.filter(emp_id=emp_id,audit_date__year=currentYear, audit_date__month=currentMonth).values(
                    'process').annotate(dcount=Count('associate_name')).annotate(
                    davg=Avg('overall_score'))
                emp_wise_fatal = i.objects.filter(emp_id=emp_id, audit_date__year=currentYear,
                                            audit_date__month=currentMonth,fatal=True).values(
                    'process').annotate(dsum=Sum('fatal_count'))

                emp_wise_errors = i.objects.filter(emp_id=emp_id, audit_date__year=currentYear,
                                                  audit_date__month=currentMonth,overall_score__lt=100).values(
                    'process').annotate(dcount=Count('process'))

                associate_data.append(emp_wise)
                associate_data_fatal.append(emp_wise_fatal)
                associate_data_errors.append(emp_wise_errors)

        data = {'profile':profile,'associate_data':associate_data,
                'associate_data_fatal':associate_data_fatal,
                'associate_data_errors':associate_data_errors,
                'avg_score':avg_score,
                }


        return render(request,'employee-wise-report.html',data)

def managerWiseReport(request):

    if request.method == 'POST':

        currentMonth = request.POST['month']
        currentYear = request.POST['year']
        manager_emp_id=request.POST['emp_id']
        profile=Profile.objects.get(emp_id=manager_emp_id)
        manager_name=profile.emp_name
        # Mon Form List
        category = request.POST['category']

        associate_data = []
        associate_data_fatal = []
        associate_data_errors = []

        if category == 'manager':

            # Score in All forms
            for i in list_of_monforms:
                coaching = i.objects.filter(manager_id=manager_emp_id, audit_date__year=currentYear,
                                            audit_date__month=currentMonth)
                if coaching.count() > 0:

                    emp_wise = i.objects.filter(manager_id=manager_emp_id, audit_date__year=currentYear,
                                                audit_date__month=currentMonth).values(
                        'process').annotate(dcount=Count('associate_name')).annotate(
                        davg=Avg('overall_score'))
                    emp_wise_fatal = i.objects.filter(manager_id=manager_emp_id, audit_date__year=currentYear,
                                                      audit_date__month=currentMonth).values(
                        'process').annotate(dsum=Sum('fatal_count'))

                    emp_wise_errors = i.objects.filter(manager_id=manager_emp_id, audit_date__year=currentYear,
                                                       audit_date__month=currentMonth, overall_score__lt=100).values(
                        'process').annotate(dcount=Count('process'))

                    associate_data.append(emp_wise)
                    associate_data_fatal.append(emp_wise_fatal)
                    associate_data_errors.append(emp_wise_errors)
                else:
                    pass

        elif category == 'qa':

            # Score in All forms
            for i in list_of_monforms:
                coaching = i.objects.filter(qa=manager_name, audit_date__year=currentYear,
                                            audit_date__month=currentMonth)
                if coaching.count() > 0:

                    emp_wise = i.objects.filter(qa=manager_name, audit_date__year=currentYear,
                                                audit_date__month=currentMonth).values(
                        'process').annotate(dcount=Count('associate_name')).annotate(
                        davg=Avg('overall_score'))
                    emp_wise_fatal = i.objects.filter(qa=manager_name, audit_date__year=currentYear,
                                                      audit_date__month=currentMonth).values(
                        'process').annotate(dsum=Sum('fatal_count'))

                    emp_wise_errors = i.objects.filter(qa=manager_name, audit_date__year=currentYear,
                                                       audit_date__month=currentMonth, overall_score__lt=100).values(
                        'process').annotate(dcount=Count('process'))

                    associate_data.append(emp_wise)
                    associate_data_fatal.append(emp_wise_fatal)
                    associate_data_errors.append(emp_wise_errors)
                else:
                    pass

        elif category == 'tl':
            # Score in All forms
            for i in list_of_monforms:
                coaching = i.objects.filter(team_lead=manager_name, audit_date__year=currentYear,
                                            audit_date__month=currentMonth)
                if coaching.count() > 0:

                    emp_wise = i.objects.filter(team_lead=manager_name, audit_date__year=currentYear,
                                                audit_date__month=currentMonth).values(
                        'process').annotate(dcount=Count('associate_name')).annotate(
                        davg=Avg('overall_score'))
                    emp_wise_fatal = i.objects.filter(team_lead=manager_name, audit_date__year=currentYear,
                                                      audit_date__month=currentMonth).values(
                        'process').annotate(dsum=Sum('fatal_count'))

                    emp_wise_errors = i.objects.filter(team_lead=manager_name, audit_date__year=currentYear,
                                                       audit_date__month=currentMonth, overall_score__lt=100).values(
                        'process').annotate(dcount=Count('process'))

                    associate_data.append(emp_wise)
                    associate_data_fatal.append(emp_wise_fatal)
                    associate_data_errors.append(emp_wise_errors)
                else:
                    pass

        elif category == 'am':
            # Score in All forms
            for i in list_of_monforms:
                coaching = i.objects.filter(am=manager_name, audit_date__year=currentYear,
                                            audit_date__month=currentMonth)
                if coaching.count() > 0:

                    emp_wise = i.objects.filter(am=manager_name, audit_date__year=currentYear,
                                                audit_date__month=currentMonth).values(
                        'process').annotate(dcount=Count('associate_name')).annotate(
                        davg=Avg('overall_score'))
                    emp_wise_fatal = i.objects.filter(am=manager_name, audit_date__year=currentYear,
                                                      audit_date__month=currentMonth).values(
                        'process').annotate(dsum=Sum('fatal_count'))

                    emp_wise_errors = i.objects.filter(am=manager_name, audit_date__year=currentYear,
                                                       audit_date__month=currentMonth, overall_score__lt=100).values(
                        'process').annotate(dcount=Count('process'))

                    associate_data.append(emp_wise)
                    associate_data_fatal.append(emp_wise_fatal)
                    associate_data_errors.append(emp_wise_errors)
                else:
                    pass

        data = {'profile': profile, 'associate_data': associate_data,
                'associate_data_fatal': associate_data_fatal,
                'associate_data_errors': associate_data_errors,
                }

        return render(request,'manager-wise-report.html',data)

def qualityDashboardMgt(request):
    from django.db.models import Avg
    campaigns = Campaigns.objects.all()
    import datetime
    employees = Profile.objects.exclude(emp_desi__in=['AM','Manager','Team Leader','Trainer','QA']).order_by('emp_name')
    managers = Profile.objects.filter(emp_desi='Manager')
    ams = Profile.objects.filter(emp_desi='AM')
    tls = Profile.objects.filter(emp_desi='Team Leader')
    qas = Profile.objects.filter(emp_desi='QA')

    teams = Team.objects.all()

    # Date Time
    if request.method=='POST':

        month =request.POST['month']
        year = request.POST['year']

        outbound_avg_list = []
        inbound_avg_list = []
        email_chat_avg_list = []

        camp_wise_tot = []
        for i in list_of_monforms:
            camp_wise_total = i.objects.filter(audit_date__year=year, audit_date__month=month).values(
                'process').annotate(dcount=Count('process')).annotate(davg=Avg('overall_score'))
            camp_wise_tot.append(camp_wise_total)

            outbound_score = i.objects.filter(type='Outbound',audit_date__year=year, audit_date__month=month).aggregate(davg=Avg('overall_score'))
            if outbound_score['davg']:
                outbound_avg_list.append(outbound_score['davg'])

            inbound_score = i.objects.filter(type='Inbound',audit_date__year=year, audit_date__month=month).aggregate(davg=Avg('overall_score'))
            if inbound_score['davg']:
                inbound_avg_list.append(inbound_score['davg'])

            email_chat_score = i.objects.filter(type='Email - Chat',audit_date__year=year, audit_date__month=month).aggregate(davg=Avg('overall_score'))
            if email_chat_score['davg']:
                email_chat_avg_list.append(email_chat_score['davg'])

        if len(outbound_avg_list) > 0:
            outbound_avg = sum(outbound_avg_list) / len(outbound_avg_list)
        else:
            outbound_avg = 100
        if len(inbound_avg_list) > 0:
            inbound_avg = sum(inbound_avg_list) / len(inbound_avg_list)
        else:
            inbound_avg = 100
        if len(email_chat_avg_list) > 0:
            email_chat_avg = sum(email_chat_avg_list) / len(email_chat_avg_list)
        else:
            email_chat_avg = 100
        #
        data = {'employees': employees, 'managers': managers, 'campaigns': campaigns,
                'teams': teams, 'camp_total': camp_wise_tot,
                'outbound_avg': outbound_avg,
                'inbound_avg': inbound_avg,
                'email_chat_avg': email_chat_avg,
                'ams':ams,
                'tls':tls,
                'qas':qas,
                }

        return render(request, 'quality-dashboard-management.html', data)

    else:

        d = datetime.datetime.now()
        month = d.strftime("%m")
        year = d.strftime("%Y")

        outbound_avg_list = []
        inbound_avg_list = []
        email_chat_avg_list = []

        camp_wise_tot = []
        for i in list_of_monforms:
            camp_wise_total = i.objects.filter(audit_date__year=year, audit_date__month=month).values(
                'process').annotate(dcount=Count('process')).annotate(davg=Avg('overall_score'))
            camp_wise_tot.append(camp_wise_total)

            outbound_score = i.objects.filter(type='Outbound',audit_date__year=year, audit_date__month=month).aggregate(davg=Avg('overall_score'))
            if outbound_score['davg']:
                outbound_avg_list.append(outbound_score['davg'])

            inbound_score = i.objects.filter(type='Inbound',audit_date__year=year, audit_date__month=month).aggregate(davg=Avg('overall_score'))
            if inbound_score['davg']:
                inbound_avg_list.append(inbound_score['davg'])

            email_chat_score = i.objects.filter(type='Email - Chat',audit_date__year=year, audit_date__month=month).aggregate(davg=Avg('overall_score'))
            if email_chat_score['davg']:
                email_chat_avg_list.append(email_chat_score['davg'])

        if len(outbound_avg_list)>0:
            outbound_avg = sum(outbound_avg_list)/len(outbound_avg_list)
        else:
            outbound_avg = 100
        if len(inbound_avg_list)>0:
            inbound_avg = sum(inbound_avg_list) / len(inbound_avg_list)
        else:
            inbound_avg = 100
        if len(email_chat_avg_list)>0:
            email_chat_avg = sum(email_chat_avg_list) / len(email_chat_avg_list)
        else:
            email_chat_avg = 100
        #
        data = {'employees': employees, 'managers': managers, 'campaigns': campaigns,
            'teams': teams, 'camp_total': camp_wise_tot,
                'outbound_avg':outbound_avg,
                'inbound_avg':inbound_avg,
                'email_chat_avg':email_chat_avg,
                'ams': ams,
                'tls': tls,
                'qas': qas,
                }

        return render(request, 'quality-dashboard-management.html', data)



def agenthome(request):

    agent_name = request.user.profile.emp_name
    team = request.user.profile.process
    currentMonth = datetime.now().month
    currentYear = datetime.now().year

    #### Avg Score Overall ####

    avgs = []

    def avgScoreTotal(monform):
        avg_score_all = monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,
                                               associate_name=agent_name).aggregate(davg=Avg('overall_score'))
        if avg_score_all['davg'] != None:
            avgs.append(avg_score_all['davg'])

    for i in list_of_monforms:
        avgScoreTotal(i)

    if len(avgs)>0:
        total_score = sum(avgs) / len(avgs)
    else:
        total_score = 100
    avg_score = round(total_score, 2)

    ############################
    ###################  Avg Campaignwise

    avg_campaignwise = []
    campaign_wise_count = []
    for i in list_of_monforms:
        emp_wise = i.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,
                                    associate_name=agent_name).values('process').annotate(davg=Avg('overall_score'))
        camp_wise_count = i.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,
                                           associate_name=agent_name, overall_score__lt=100).values('process').annotate(
            dcount=Count('associate_name')).annotate(dfcount=Sum('fatal_count'))
        avg_campaignwise.append(emp_wise)
        campaign_wise_count.append(camp_wise_count)

    #######################################

    all_coaching_list = []
    open_coaching_list = []
    disput_list = []

    def openCampaigns(monforms):
        all_obj = monforms.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,
                                           associate_name=agent_name).order_by('-audit_date')
        open_obj = monforms.objects.filter(associate_name=agent_name, status=False, disput_status=False).order_by('-audit_date')
        disp_obj = monforms.objects.filter(associate_name=agent_name, disput_status=True).order_by('-audit_date')

        all_coaching_list.append(all_obj)
        open_coaching_list.append(open_obj)

        disput_list.append(disp_obj)

    for i in list_of_monforms:
        openCampaigns(i)

    list_of_open_count = []
    list_of_all_count = []
    for i in list_of_monforms:
        count = i.objects.filter(associate_name=agent_name, audit_date__year=currentYear,
                                 audit_date__month=currentMonth, status=False).count()
        count_all = i.objects.filter(associate_name=agent_name, audit_date__year=currentYear,
                                 audit_date__month=currentMonth).count()
        list_of_open_count.append(count)
        list_of_all_count.append(count_all)

    total_open_coachings = sum(list_of_open_count)
    total_coachings = sum(list_of_all_count)

    data = {'all_coachings': all_coaching_list,
            'open_coaching': open_coaching_list,
            'disput_coaching': disput_list,
            'total_open': total_open_coachings,
            'total_coachings':total_coachings,
            'team': team,
            'overall_score': avg_score,
            'avg_campaignwise': avg_campaignwise,
            'camp_wise_count': campaign_wise_count,
            }

    return render(request, 'agent-home.html', data)


def coachingViewAgents(request,process,pk):
    process_name = process

    ########## Outbound ##############################

    if process_name == 'AAdya':
        coaching = MonitoringFormLeadsAadhyaSolution.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'AB Hindalco Outbound':
        coaching = ABHindalcoOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Accutime':
        coaching = AccutimeMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Aditya Birla Outbound':
        coaching = AdityaBirlaOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Advance Consultants':
        coaching = MonitoringFormLeadsAdvanceConsultants.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Allen Consulting':
        coaching = MonitoringFormLeadsAllenConsulting.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Amerisave Outbound':
        coaching = AmerisaveoutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'BhagyaLakshmi Outbound':
        coaching = BhagyaLakshmiOutbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Cam Industrial':
        coaching = CamIndustrialMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Citizen Capital':
        coaching = CitizenCapitalMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'City Security':
        coaching = MonitoringFormLeadsCitySecurity.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Clear View Outbound':
        coaching = ClearViewOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'CTS':
        coaching = MonitoringFormLeadsCTS.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Daniel Wellington Outbound':
        coaching = DanielWellingtonOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Digital Swiss Gold Outbound':
        coaching = DigitalSwissGoldOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Embassy Luxury':
        coaching = EmbassyLuxuryMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Get A Rates':
        coaching = MonitoringFormLeadsGetARates.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Glyde App':
        coaching = GlydeAppMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Golden East':
        coaching = GoldenEastMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Healthyplus Outbound':
        coaching = HealthyplusOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Ibiz':
        coaching = IbizMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'IIB':
        coaching = IIBMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Info Think LLC':
        coaching = MonitoringFormLeadsInfothinkLLC.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Insalvage':
        coaching = MonitoringFormLeadsInsalvage.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'JJ Studio':
        coaching = JJStudioMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Kalki Fashions':
        coaching = KalkiFashions.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Louisville':
        coaching = MonitoringFormLeadsLouisville.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Maxwell Properties':
        coaching = MaxwellPropertiesOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Medicare':
        coaching = MonitoringFormLeadsMedicare.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Micro Distributing':
        coaching = MicroDistributingMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Millennium Scientific':
        coaching = MillenniumScientificMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Movement of Insurance':
        coaching = MovementofInsuranceOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'MT Cosmetic':
        coaching = MTCosmeticsMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Navigator Bio':
        coaching = NavigatorBioMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Optimal Student Loan':
        coaching = OptimalStudentLoanMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Protostar':
        coaching = ProtostarMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'PSECU':
        coaching = MonitoringFormLeadsPSECU.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'QBIQ':
        coaching = QBIQMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Restaurant Solution Group':
        coaching = RestaurentSolMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Ri8Brain':
        coaching = RitBrainMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Roof Well':
        coaching = RoofWellMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Scala':
        coaching = ScalaMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Solar Campaign':
        coaching = SolarCampaignMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Stand Spot':
        coaching = StandSpotMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Sterling Strategies':
        coaching = SterlingStrategiesOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'System4':
        coaching = MonitoringFormLeadsSystem4.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Tentamus Food':
        coaching = MonitoringFormLeadsTentamusFood.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Tentamus Pet':
        coaching = MonitoringFormLeadsTentamusPet.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Terraceo - Lead':
        coaching = TerraceoLeadMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Tonn Coa Outbound':
        coaching = TonnCoaOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Upfront Online LLC':
        coaching = UpfrontOnlineLLCMonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Wit Digital':
        coaching = WitDigitalOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'WTU':
        coaching = WTUMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Yes Health Molina':
        coaching = YesHealthMolinaMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Zero Stress Marketing':
        coaching = ZeroStressMarketingMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'PosTech':
        coaching = PosTechOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Schindler Media':
        coaching = SchindlerMediaOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'UPS':
        coaching = UPSOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Pick Pack Deliveries':
        coaching = PickPackDeliveriesMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Marcelo Perez':
        coaching = MarceloPerezMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'MedTech Group Outbound':
        coaching = MedTechGroupOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Digital Signage':
        coaching = DigitalSignageOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Hive Incubators Outbound':
        coaching = HiveIncubatorsOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Kaapi Machines Outbound':
        coaching = KaapiMachinesOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Somethings Brewing Outbound':
        coaching = SomethingsBrewingOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Naffa Outbound':
        coaching = NaffaOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'JBN':
        coaching = JBNOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Quick Auto Parts':
        coaching = QuickAutoPartsOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Apex Communications Inc':
        coaching = ApexCommunicationsOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Law Offices of Robert and Geller':
        coaching = LawOfficesOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Woke Up Energy':
        coaching = WokeUpEnergyOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Finnesse Mortgage Outbound':
        coaching = FinnesseMortgageOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'United Mortgage Outbound':
        coaching = UnitedMortgageOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    ########### Inbound ########################

    if process_name == 'AB Hindalco Inbound':
        coaching = ABHindalcoInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Aditya Birla Inbound':
        coaching = AdityaBirlainboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'AKDY Inbound':
        coaching = AKDYInboundMonFormNew.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'BhagyaLakshmi Inbound':
        coaching = BhagyaLakshmiInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Daniel Wellington Inbound':
        coaching = DanielwellingtoInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Digital Swiss Gold Inbound':
        coaching = DigitalSwissGoldInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Finesse Mortgage Inbound':
        coaching = FinesseMortgageInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Healthyplus Inbound':
        coaching = HealthyplusInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Kappi machine':
        coaching = KappimachineInboundCalls.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Naffa Innovations':
        coaching = NaffaInnovationsInboundCalls.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Nucleus Media':
        coaching = NuclusInboundCalls.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Printer Pix Inbound':
        coaching = PrinterPixMasterMonitoringFormInboundCalls.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Somethings Brewing':
        coaching = SomethingsBrewingInbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Tonn Coa Inbound':
        coaching = MasterMonitoringFormTonnCoaInboundCalls.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Rainbow Diagnostics':
        coaching = RainbowDiagnosticsInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Decentralized Vision LTD':
        coaching = DecentralizedVisionLTDInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'IEDHH':
        coaching = IEDHHInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Amerisave Inbound':
        coaching = AmerisaveInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Clear View IT Inbound':
        coaching = ClearViewInboundMonForms.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Quick Auto Parts Inbound':
        coaching = QuickAutoPartsInboundMonForms.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    ############# Email/Chat ##############################

    if process_name == 'AKDY - Email':
        coaching = AKDYEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    elif process_name == 'Amerisave Email':
        coaching = AmerisaveEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    elif process_name == 'Clear View Email':
        coaching = ClearViewEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    elif process_name == 'Daniel Wellington - Chat - Email':
        coaching = DanielWellinChatEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    elif process_name == 'Digital Swiss Gold Email - Chat':
        coaching = DigitalSwissGoldEmailChatMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    elif process_name == 'Finesse Mortgage Email':
        coaching = FinesseMortgageEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    elif process_name == 'Fur Baby':
        coaching = FurBabyMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    elif process_name == 'Practo':
        coaching = PractoMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    if process_name == 'Printer Pix Chat Email':
        coaching = PrinterPixMasterMonitoringFormChatsEmail.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    elif process_name == 'Super Play':
        coaching = SuperPlayMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    elif process_name == 'Terraceo - Chat - Email':
        coaching = TerraceoChatEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    elif process_name == 'Tonn Coa Chat Email':
        coaching = TonnChatsEmailNewMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    elif process_name == 'Rainbow Diagnostics Email':
        coaching = RainbowDiagnosticsEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    elif process_name == 'Hive Incubator':
        coaching = HiveIncubatorEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    elif process_name == 'MedTech Group Email':
        coaching = MedTechGroupEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    elif process_name == 'Ri8 Brain Email':
        coaching = Ri8BrainEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    elif process_name == 'Scala Email':
        coaching = ScalaEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    elif process_name == 'kalki Fashion Email':
        coaching = KalkiFashionEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    elif process_name == 'Maxwell Email':
        coaching = MaxwellEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    elif process_name == 'Tanaor Jewelry':
        coaching = TanaorJewelryEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    elif process_name == 'Decentralized Vision Email Chat':
        coaching = DecentralizedVisionEmailChatMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    ################ Others ##########################################################

    if process_name == 'Fame House':
        coaching = FameHouseNewMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-fame-house-new.html', data)

    if process_name == 'Noom Eva':
        coaching = ChatMonitoringFormEva.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-eva-chat.html', data)

    if process_name == 'Noom POD':
        coaching = ChatMonitoringFormPodFather.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-pod-chat.html', data)

    if process_name == 'FLA':
        coaching = FLAMonitoringForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-fla.html', data)

    else:
        pass


def coachingViewQaDetailed(request,process,pk):

    process_name = process

    ########## Outbound ##############################

    if process_name == 'AAdya':
        coaching = MonitoringFormLeadsAadhyaSolution.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'AB Hindalco Outbound':
        coaching = ABHindalcoOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Accutime':
        coaching = AccutimeMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Aditya Birla Outbound':
        coaching = AdityaBirlaOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Advance Consultants':
        coaching = MonitoringFormLeadsAdvanceConsultants.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Allen Consulting':
        coaching = MonitoringFormLeadsAllenConsulting.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Amerisave Outbound':
        coaching = AmerisaveoutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'BhagyaLakshmi Outbound':
        coaching = BhagyaLakshmiOutbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Cam Industrial':
        coaching = CamIndustrialMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Citizen Capital':
        coaching = CitizenCapitalMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'City Security':
        coaching = MonitoringFormLeadsCitySecurity.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Clear View Outbound':
        coaching = ClearViewOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'CTS':
        coaching = MonitoringFormLeadsCTS.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Daniel Wellington Outbound':
        coaching = DanielWellingtonOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Digital Swiss Gold Outbound':
        coaching = DigitalSwissGoldOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Embassy Luxury':
        coaching = EmbassyLuxuryMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Get A Rates':
        coaching = MonitoringFormLeadsGetARates.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Glyde App':
        coaching = GlydeAppMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Golden East':
        coaching = GoldenEastMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Healthyplus Outbound':
        coaching = HealthyplusOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Ibiz':
        coaching = IbizMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'IIB':
        coaching = IIBMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Info Think LLC':
        coaching = MonitoringFormLeadsInfothinkLLC.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Insalvage':
        coaching = MonitoringFormLeadsInsalvage.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'JJ Studio':
        coaching = JJStudioMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Kalki Fashions':
        coaching = KalkiFashions.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Louisville':
        coaching = MonitoringFormLeadsLouisville.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Maxwell Properties':
        coaching = MaxwellPropertiesOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Medicare':
        coaching = MonitoringFormLeadsMedicare.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Micro Distributing':
        coaching = MicroDistributingMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Millennium Scientific':
        coaching = MillenniumScientificMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Movement of Insurance':
        coaching = MovementofInsuranceOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'MT Cosmetic':
        coaching = MTCosmeticsMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Navigator Bio':
        coaching = NavigatorBioMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Optimal Student Loan':
        coaching = OptimalStudentLoanMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Protostar':
        coaching = ProtostarMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'PSECU':
        coaching = MonitoringFormLeadsPSECU.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'QBIQ':
        coaching = QBIQMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Restaurant Solution Group':
        coaching = RestaurentSolMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Ri8Brain':
        coaching = RitBrainMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Roof Well':
        coaching = RoofWellMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Scala':
        coaching = ScalaMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Solar Campaign':
        coaching = SolarCampaignMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Stand Spot':
        coaching = StandSpotMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Sterling Strategies':
        coaching = SterlingStrategiesOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'System4':
        coaching = MonitoringFormLeadsSystem4.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Tentamus Food':
        coaching = MonitoringFormLeadsTentamusFood.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Tentamus Pet':
        coaching = MonitoringFormLeadsTentamusPet.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Terraceo - Lead':
        coaching = TerraceoLeadMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Tonn Coa Outbound':
        coaching = TonnCoaOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Upfront Online LLC':
        coaching = UpfrontOnlineLLCMonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Wit Digital':
        coaching = WitDigitalOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'WTU':
        coaching = WTUMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Yes Health Molina':
        coaching = YesHealthMolinaMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Zero Stress Marketing':
        coaching = ZeroStressMarketingMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'PosTech':
        coaching = PosTechOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Schindler Media':
        coaching = SchindlerMediaOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'UPS':
        coaching = UPSOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Pick Pack Deliveries':
        coaching = PickPackDeliveriesMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Marcelo Perez':
        coaching = MarceloPerezMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'MedTech Group Outbound':
        coaching = MedTechGroupOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Digital Signage':
        coaching = DigitalSignageOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Hive Incubators Outbound':
        coaching = HiveIncubatorsOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Kaapi Machines Outbound':
        coaching = KaapiMachinesOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Somethings Brewing Outbound':
        coaching = SomethingsBrewingOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Naffa Outbound':
        coaching = NaffaOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'JBN':
        coaching = JBNOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Quick Auto Parts':
        coaching = QuickAutoPartsOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Apex Communications Inc':
        coaching = ApexCommunicationsOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Law Offices of Robert and Geller':
        coaching = LawOfficesOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Woke Up Energy':
        coaching = WokeUpEnergyOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Finnesse Mortgage Outbound':
        coaching = FinnesseMortgageOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'United Mortgage Outbound':
        coaching = UnitedMortgageOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)


    ########### Inbound ########################

    if process_name == 'AB Hindalco Inbound':
        coaching = ABHindalcoInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'Aditya Birla Inbound':
        coaching = AdityaBirlainboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'AKDY Inbound':
        coaching = AKDYInboundMonFormNew.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'BhagyaLakshmi Inbound':
        coaching = BhagyaLakshmiInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'Daniel Wellington Inbound':
        coaching = DanielwellingtoInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'Digital Swiss Gold Inbound':
        coaching = DigitalSwissGoldInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'Finesse Mortgage Inbound':
        coaching = FinesseMortgageInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'Healthyplus Inbound':
        coaching = HealthyplusInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'Kappi machine':
        coaching = KappimachineInboundCalls.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'Naffa Innovations':
        coaching = NaffaInnovationsInboundCalls.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'Nucleus Media':
        coaching = NuclusInboundCalls.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'Printer Pix Inbound':
        coaching = PrinterPixMasterMonitoringFormInboundCalls.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'Somethings Brewing':
        coaching = SomethingsBrewingInbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'Tonn Coa Inbound':
        coaching = MasterMonitoringFormTonnCoaInboundCalls.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'Rainbow Diagnostics':
        coaching = RainbowDiagnosticsInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'Decentralized Vision LTD':
        coaching = DecentralizedVisionLTDInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'IEDHH':
        coaching = IEDHHInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'Amerisave Inbound':
        coaching = AmerisaveInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'Clear View IT Inbound':
        coaching = ClearViewInboundMonForms.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'Quick Auto Parts Inbound':
        coaching = QuickAutoPartsInboundMonForms.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)


    ############# Email/Chat ##############################

    if process_name == 'AKDY - Email':
        coaching = AKDYEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    elif process_name == 'Amerisave Email':
        coaching = AmerisaveEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    elif process_name == 'Clear View Email':
        coaching = ClearViewEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    elif process_name == 'Daniel Wellington - Chat - Email':
        coaching = DanielWellinChatEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    elif process_name == 'Digital Swiss Gold Email - Chat':
        coaching = DigitalSwissGoldEmailChatMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    elif process_name == 'Finesse Mortgage Email':
        coaching = FinesseMortgageEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    elif process_name == 'Fur Baby':
        coaching = FurBabyMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    elif process_name == 'Practo':
        coaching = PractoMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    if process_name == 'Printer Pix Chat Email':
        coaching = PrinterPixMasterMonitoringFormChatsEmail.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    elif process_name == 'Super Play':
        coaching = SuperPlayMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    elif process_name == 'Terraceo - Chat - Email':
        coaching = TerraceoChatEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    elif process_name == 'Tonn Coa Chat Email':
        coaching = TonnChatsEmailNewMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    elif process_name == 'Rainbow Diagnostics Email':
        coaching = RainbowDiagnosticsEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    elif process_name == 'Hive Incubator':
        coaching = HiveIncubatorEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    elif process_name == 'MedTech Group Email':
        coaching = MedTechGroupEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    elif process_name == 'Ri8 Brain Email':
        coaching = Ri8BrainEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    elif process_name == 'Scala Email':
        coaching = ScalaEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    elif process_name == 'kalki Fashion Email':
        coaching = KalkiFashionEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    elif process_name == 'Maxwell Email':
        coaching = MaxwellEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    elif process_name == 'Tanaor Jewelry':
        coaching = TanaorJewelryEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    elif process_name == 'Decentralized Vision Email Chat':
        coaching = DecentralizedVisionEmailChatMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)


    ################ Others ##########################################################

    if process_name == 'Fame House':
        coaching = FameHouseNewMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-fame-house-new.html', data)

    if process_name == 'Noom Eva':
        coaching = ChatMonitoringFormEva.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-eva-chat.html', data)

    if process_name == 'Noom POD':
        coaching = ChatMonitoringFormPodFather.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-pod-chat.html', data)

    if process_name == 'FLA':
        coaching = FLAMonitoringForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-fla.html', data)

    else:
        pass


# Campaign wise coaching view - qa - manager

def campaignwiseCoachings(request):

    if request.method == 'POST':
        campaign = request.POST['campaign']
        status=request.POST['status']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        if start_date and end_date:
            if status=='all':
                coaching_list=[]
                def dateAll(monform):
                    obj=monform.objects.filter(process=campaign,audit_date__range=[start_date, end_date])
                    return obj

                for i in list_of_monforms:
                    obj=dateAll(i)
                    coaching_list.append(obj)
            else:
                coaching_list = []
                def datestatusAll(monform):
                    obj = monform.objects.filter(process=campaign,status=status,audit_date__range=[start_date, end_date])
                    return obj

                for i in list_of_monforms:
                    obj = datestatusAll(i)
                    coaching_list.append(obj)

            data={'coaching_list':coaching_list,

                 }
            return render(request,'campaign-wise-coaching-view.html',data)

        else:

            if status=='all':
                coaching_list=[]
                def dateAll(monform):
                    obj=monform.objects.filter(process=campaign)
                    return obj

                for i in list_of_monforms:
                    obj=dateAll(i)
                    coaching_list.append(obj)

            else:
                coaching_list = []
                def datestatusAll(monform):
                    obj = monform.objects.filter(process=campaign,status=status)
                    return obj

                for i in list_of_monforms:
                    obj = datestatusAll(i)
                    coaching_list.append(obj)

            data={'coaching_list':coaching_list,
                 }

            return render(request,'campaign-wise-coaching-view.html',data)
    else:
        pass


def campaignwiseCoachingsQA(request):
    if request.method == 'POST':
        campaign = request.POST['campaign']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        qa = request.POST['qa']

        coaching_list = []
        for i in list_of_monforms:
            coaching = i.objects.filter(qa=qa,process=campaign,audit_date__range=[start_date, end_date])
            coaching_list.append(coaching)
        data={'coaching_list':coaching_list}
        return render(request,'campaign-wise-coaching-view.html',data)

    else:
        pass


# Campaign wise coaching view - Agent

def campaignwiseCoachingsAgent(request):

    if request.method == 'POST':
        team_id = request.POST['team_id']
        status = request.POST['status']
        team_name = Team.objects.get(id=team_id)
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        emp_name=request.POST['emp_name']


        if start_date and end_date:

            if status == 'all':

                coaching_list = []

                def dateAll(monform):
                    obj = monform.objects.filter(campaign=team_name,associate_name=emp_name, audit_date__range=[start_date, end_date])
                    return obj

                for i in list_of_monforms:
                    obj = dateAll(i)
                    coaching_list.append(obj)

            else:

                coaching_list = []

                def datestatusAll(monform):
                    obj = monform.objects.filter(campaign=team_name,associate_name=emp_name, status=status,
                                                 audit_date__range=[start_date, end_date])
                    return obj

                for i in list_of_monforms:
                    obj = datestatusAll(i)
                    coaching_list.append(obj)

            data = {'coaching_list': coaching_list,

                    }

            return render(request, 'campaign-wise-coaching-view.html', data)


        else:

            if status == 'all':

                coaching_list = []

                def dateAll(monform):
                    obj = monform.objects.filter(campaign=team_name,associate_name=emp_name,)
                    return obj

                for i in list_of_monforms:
                    obj = dateAll(i)
                    coaching_list.append(obj)

            else:

                coaching_list = []

                def datestatusAll(monform):
                    obj = monform.objects.filter(campaign=team_name,associate_name=emp_name, status=status)
                    return obj

                for i in list_of_monforms:
                    obj = datestatusAll(i)
                    coaching_list.append(obj)

            data = {'coaching_list': coaching_list,
                    }

            return render(request, 'campaign-wise-coaching-view.html', data)

    else:
        pass


def campaignwiseDetailedReport(request,cname):

    if request.method=='POST':

        from datetime import datetime
        currentMonth = request.POST['month']
        currentYear = request.POST['year']
        campaign=cname

        def campaignWiseCalculator(monform):

            emp_wise = monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth).values(
                'associate_name').annotate(dcount=Count('associate_name')).annotate(davg=Avg('overall_score')).order_by(
                '-dcount')

            emp_wise_fatal = monform.objects.filter(fatal=True, audit_date__year=currentYear,
                                                    audit_date__month=currentMonth).values('associate_name').annotate(
                dcount=Sum('fatal_count'))
            total_errors = monform.objects.filter(overall_score__lt=100, audit_date__year=currentYear,
                                                  audit_date__month=currentMonth).count()
            total_fatal_obj = monform.objects.filter(fatal=True, audit_date__year=currentYear,
                                                     audit_date__month=currentMonth)
            total_fata_list = []

            for i in total_fatal_obj:
                total_fata_list.append(i.fatal_count)

            total_fatal = sum(total_fata_list)
            total_audit_count = monform.objects.filter(audit_date__year=currentYear,
                                                       audit_date__month=currentMonth).count()

            avg = monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth).aggregate(
                Avg('overall_score'))
            processavg = avg['overall_score__avg']

            if processavg == None:
                process_avg = 0
            else:
                process_avg = float("{:.2f}".format(processavg))

            week_wise_avg = monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth).values(
                'week').annotate(davg=Avg('overall_score')).annotate(dcount=Count('week'))

            # Parameter wise ########

            open_coaching_employee_wise = monform.objects.filter(status=False,audit_date__year=currentYear, audit_date__month=currentMonth).values('associate_name').annotate(
                dcount=Count('status'))

            dispute_coaching = monform.objects.filter(disput_status=True,audit_date__year=currentYear, audit_date__month=currentMonth).values('associate_name').annotate(
                dcount=Count('status'))


            data = {
                'total_errors': total_errors,
                'total_fatal': total_fatal,
                'total_audit_count': total_audit_count,
                'process_avg': process_avg,
                'week_wise_avg': week_wise_avg,
                'emp_wise': emp_wise,
                'emp_wise_fatal': emp_wise_fatal,
                'process': campaign,
                'emp_coaching': open_coaching_employee_wise,
                'dispute_coaching': dispute_coaching,
                'cmonth': currentMonth,
                'cyear': currentYear,

            }

            return data

        monform = None
        for i in list_of_monforms:
            obj = i.objects.all()
            if obj.count() > 0:
                if obj[0].process == campaign:
                    monform = i
                else:
                    pass
            else:
                pass
        if monform == None:
            data = {'no_data': 'No Audit Data Available'}
            return render(request, 'campaign-report/detailed-no-data.html', data)
        else:
            data = campaignWiseCalculator(monform)
        return render(request, 'campaign-report/detailed.html', data)

    else:
        from datetime import datetime

        currentMonth = datetime.now().month
        currentYear = datetime.now().year
        campaign = cname

        def campaignWiseCalculator(monform):

            emp_wise = monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth).values(
                'associate_name').annotate(dcount=Count('associate_name')).annotate(davg=Avg('overall_score')).order_by(
                '-dcount')

            emp_wise_fatal = monform.objects.filter(fatal=True, audit_date__year=currentYear,
                                                    audit_date__month=currentMonth).values('associate_name').annotate(dcount=Sum('fatal_count'))
            total_errors = monform.objects.filter(overall_score__lt=100, audit_date__year=currentYear,audit_date__month=currentMonth).count()
            total_fatal_obj = monform.objects.filter(fatal=True, audit_date__year=currentYear, audit_date__month=currentMonth)
            total_fata_list = []

            for i in total_fatal_obj:
                total_fata_list.append(i.fatal_count)

            total_fatal = sum(total_fata_list)
            total_audit_count = monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth).count()

            avg = monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth).aggregate(Avg('overall_score'))
            processavg = avg['overall_score__avg']

            if processavg == None:
                process_avg = 0
            else:
                process_avg = float("{:.2f}".format(processavg))

            week_wise_avg = monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth).values(
                'week').annotate(davg=Avg('overall_score')).annotate(dcount=Count('week'))

            # Parameter wise ########

            open_coaching_employee_wise = monform.objects.filter(status=False,audit_date__year=currentYear, audit_date__month=currentMonth).values('associate_name').annotate( dcount=Count('status'))

            dispute_coaching = monform.objects.filter(disput_status=True,audit_date__year=currentYear, audit_date__month=currentMonth).values('associate_name').annotate(dcount=Count('status'))

            data = {
                    'total_errors': total_errors,
                    'total_fatal': total_fatal,
                    'total_audit_count': total_audit_count,
                    'process_avg': process_avg,
                    'week_wise_avg': week_wise_avg,
                    'emp_wise': emp_wise,
                    'emp_wise_fatal': emp_wise_fatal,
                    'process': campaign,
                    'emp_coaching': open_coaching_employee_wise,
                    'dispute_coaching':dispute_coaching,
                    'cmonth': currentMonth,
                    'cyear': currentYear
                    }

            return data

        monform = None
        for i in list_of_monforms:
            obj = i.objects.all()
            if obj.count() > 0:
                if obj[0].process == campaign:
                    monform = i
                else:
                    pass
            else:
                pass
        if monform == None:
            data = {'no_data': 'No Audit Data Available'}
            return render(request, 'campaign-report/detailed-no-data.html', data)
        else:
            data = campaignWiseCalculator(monform)
        return render(request, 'campaign-report/detailed.html', data)


def signCoaching(request,pk):

    from datetime import date
    now = date.today()
    category=request.POST['category']
    emp_comments=request.POST['emp_comments']

    for i in list_of_monforms:
        obj = i.objects.all()
        if obj.count() >0:
            if obj[0].process == category:
                campaign = i
            else:
                pass
        else:
            pass

    coaching = campaign.objects.get(id=pk)
    coaching.status = True
    coaching.closed_date = now
    coaching.emp_comments = emp_comments
    coaching.disput_status=False
    coaching.save()
    return redirect('/employees/agenthome')


def coachingSuccess(request):

    return render(request,'coaching-success-message.html')

def coachingDispute(request,pk):
    if request.method == 'POST':
        emp_comments = request.POST['emp_comments_dispute']
        emp_name=request.user.profile.emp_name
        team = request.user.profile.process
        manager_name = request.user.profile.manager
        try:
            manager_mail=Profile.objects.get(emp_name=manager_name)
            manager_email = manager_mail.email
        except Profile.DoesNotExist:
            manager_email = 'tabassum.z@expertcallers.com'

        cid = pk
        process = request.POST['campaign']
        html_path = 'dispute-template.html'
        data = {'id': cid,'process':process,'emp_name':emp_name,'emp_comments':emp_comments}
        email_template = get_template(html_path).render(data)
        receiver_email = manager_email
        email_msg = EmailMessage('QMS - Coaching Dispute',
                                 email_template, 'qms@expertcallers.com',
                                 [receiver_email,],
                                 reply_to=['qms@expertcallers.com'])
        email_msg.content_subtype = 'html'
        email_msg.send(fail_silently=False)

        for i in list_of_monforms:
            obj = i.objects.all()
            if obj.count() > 0:
                if obj[0].process == process:
                    campaign = i
                else:
                    pass
            else:
                pass

        obj=campaign.objects.get(id=cid)
        obj.disput_status=True
        obj.emp_comments=emp_comments
        obj.save()

        data={'team':team}
        return render(request,'coaching-dispute-message.html',data)
    else:
        return redirect('/employees/agenthome')

def qahome(request):

    if request.method=='POST':

        currentMonth = request.POST['month']
        currentYear = request.POST['year']
        qa_name = request.user.profile.emp_name

        # Total NO of Coachings
        total_coaching_ids = []
        for i in list_of_monforms:
            x = i.objects.filter(added_by=qa_name,audit_date__year=currentYear,audit_date__month=currentMonth)
            for i in x:
                total_coaching_ids.append(i.id)
        total_coaching = len(total_coaching_ids)

        list_open_campaigns = []
        list_dispute_campaigns = []
        all_coachings = []
        for i in list_of_monforms:
            opn_cmp_obj = i.objects.filter(status=False, added_by=qa_name, audit_date__year=currentYear,
                                           audit_date__month=currentMonth)
            list_open_campaigns.append(opn_cmp_obj)
            disp_obj = i.objects.filter(disput_status=True, added_by=qa_name, audit_date__year=currentYear,
                                        audit_date__month=currentMonth)
            list_dispute_campaigns.append(disp_obj)
            all_coaching = i.objects.filter(added_by=qa_name, audit_date__year=currentYear,
                                            audit_date__month=currentMonth).order_by('-id')
            all_coachings.append(all_coaching)

        list_of_open_count = []
        list_of_disp_count = []
        for i in list_of_monforms:
            count = i.objects.filter(added_by=qa_name, status=False, audit_date__year=currentYear,
                                     audit_date__month=currentMonth).count()
            list_of_open_count.append(count)
            disp_count = i.objects.filter(added_by=qa_name, disput_status=True, audit_date__year=currentYear,
                                          audit_date__month=currentMonth).count()
            list_of_disp_count.append(disp_count)
        total_open_coachings = sum(list_of_open_count)
        total_disp_coachings = sum(list_of_disp_count)

        avg_campaignwise = []
        for i in list_of_monforms:
            emp_wise = i.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,
                                        qa=qa_name).values(
                'process').annotate(davg=Avg('overall_score'))
            avg_campaignwise.append(emp_wise)

        #############################################
        campaigns_from_db = Campaigns.objects.filter(type='Outbound').order_by('name')
        campaigns_inbound = Campaigns.objects.filter(type='Inbound').order_by('name')
        campaigns_email_chat = Campaigns.objects.filter(type='Email - Chat').order_by('name')
        campaigns_other = Campaigns.objects.exclude(type__in=['Outbound', 'Inbound', 'Email - Chat'])
        all_campaigns = Campaigns.objects.all().order_by('name')
        data = {
            'total_open': total_open_coachings,
            'total_dispute': total_disp_coachings,
            'total_coaching': total_coaching,
            'open_campaigns': list_open_campaigns,
            'all_coachings': all_coachings,
            'dispute_coachings': list_dispute_campaigns,
            'avg_campaignwise': avg_campaignwise,
            'campaigns': campaigns_from_db,
            'campaigns_inbound': campaigns_inbound,
            'campaigns_email_chat': campaigns_email_chat,
            'campaigns_other': campaigns_other,
            'all_campaigns': all_campaigns,
            'month': currentMonth,
            'year': currentYear,
        }

        return render(request, 'qa-home.html', data)

    else:
        qa_name = request.user.profile.emp_name
        currentMonth = datetime.now().month
        currentYear = datetime.now().year

        # Total NO of Coachings
        total_coaching_ids = []
        for i in list_of_monforms:
            x = i.objects.filter(added_by=qa_name,audit_date__year=currentYear,audit_date__month=currentMonth)
            for i in x:
                total_coaching_ids.append(i.id)
        total_coaching = len(total_coaching_ids)

        list_open_campaigns = []
        list_dispute_campaigns = []
        all_coachings = []
        for i in list_of_monforms:
            opn_cmp_obj = i.objects.filter(status=False, added_by=qa_name, audit_date__year=currentYear,audit_date__month=currentMonth)
            list_open_campaigns.append(opn_cmp_obj)
            disp_obj = i.objects.filter(disput_status=True, added_by=qa_name, audit_date__year=currentYear,audit_date__month=currentMonth)
            list_dispute_campaigns.append(disp_obj)
            all_coaching = i.objects.filter(added_by=qa_name, audit_date__year=currentYear,audit_date__month=currentMonth).order_by('-id')
            all_coachings.append(all_coaching)

        list_of_open_count = []
        list_of_disp_count = []
        for i in list_of_monforms:
            count = i.objects.filter(added_by=qa_name, status=False, audit_date__year=currentYear,audit_date__month=currentMonth).count()
            list_of_open_count.append(count)
            disp_count = i.objects.filter(added_by=qa_name, disput_status=True, audit_date__year=currentYear,
                                     audit_date__month=currentMonth).count()
            list_of_disp_count.append(disp_count)
        total_open_coachings = sum(list_of_open_count)
        total_disp_coachings = sum(list_of_disp_count)

        avg_campaignwise = []
        for i in list_of_monforms:
            emp_wise = i.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,qa=qa_name).values(
                'process').annotate(davg=Avg('overall_score'))
            avg_campaignwise.append(emp_wise)

        #############################################
        campaigns_from_db = Campaigns.objects.filter(type='Outbound').order_by('name')
        campaigns_inbound = Campaigns.objects.filter(type='Inbound').order_by('name')
        campaigns_email_chat = Campaigns.objects.filter(type='Email - Chat').order_by('name')
        campaigns_other = Campaigns.objects.exclude(type__in=['Outbound','Inbound','Email - Chat'])
        all_campaigns = Campaigns.objects.all().order_by('name')
        data = {
                'total_open': total_open_coachings,
                'total_dispute':total_disp_coachings,
                'total_coaching': total_coaching,
                'open_campaigns': list_open_campaigns,
                'all_coachings':all_coachings,
                'dispute_coachings':list_dispute_campaigns,
                'avg_campaignwise': avg_campaignwise,
                'campaigns':campaigns_from_db,
                'campaigns_inbound':campaigns_inbound,
                'campaigns_email_chat':campaigns_email_chat,
                'campaigns_other':campaigns_other,
                'all_campaigns':all_campaigns,
                'month':currentMonth,
                'year':currentYear,
                }

        return render(request, 'qa-home.html', data)


#campaign View

def campaignView(request):

    if request.method=='POST':

        campaign_id = request.POST['campaign_id']
        campaign = Campaigns.objects.get(id=campaign_id)
        agents=Profile.objects.exclude(emp_desi__in=['AM','Manager','Team Leader','Trainer','QA']).order_by('emp_name')

        data = {'campaign':campaign,'agents':agents}
        return render(request,'campaign-view.html',data)

    else:
        pass

def selectCoachingForm(request):

    if request.method == 'POST':

        import datetime
        today_date = datetime.date.today()
        new_today_date = today_date.strftime("%Y-%m-%d")
        agent_id=request.POST['agent_id']
        campaign_id=request.POST['campaign_id']
        campaign = Campaigns.objects.get(id=campaign_id)
        campaign_type = campaign.type
        agent = Profile.objects.get(emp_id=agent_id)

        if campaign_type == 'Outbound':
            data = {'agent': agent, 'campaign': campaign, 'date': new_today_date}
            return render(request, 'mon-forms/new-series-common.html', data)

        elif campaign_type == 'Inbound':
            data = {'agent': agent, 'campaign': campaign, 'date': new_today_date}
            return render(request, 'mon-forms/new-series-inbound.html', data)

        elif campaign_type == 'Email - Chat':
            data = {'agent': agent, 'campaign': campaign, 'date': new_today_date}
            return render(request, 'mon-forms/email-chat.html', data)

        elif campaign_type == 'FLA':
            data = {'agent': agent, 'campaign': campaign, 'date': new_today_date}
            return render(request, 'mon-forms/FLA-mon-form.html', data)

        elif campaign_type == 'Noom Eva':
            data = {'agent': agent, 'campaign': campaign,'date': new_today_date}
            return render(request, 'mon-forms/ECPL-EVA&NOVO-Monitoring-Form-chat.html', data)

        elif campaign_type == 'Noom POD':

            data = {'agent': agent, 'campaign': campaign,'date': new_today_date}
            return render(request, 'mon-forms/ECPL-Pod-Father-Monitoring-Form-chat.html', data)

        elif campaign_type =='Fame House':
            data = {'agent': agent, 'campaign': campaign,'date': new_today_date}
            return render(request, 'mon-forms/fame-house-new.html', data)

        elif campaign_type =='Gubagoo':
            data = {'agent': agent, 'campaign': campaign,'date': new_today_date}
            return render(request, 'mon-forms/gubagoo.html', data)




    else:
        return redirect('/employees/qahome')

def coachingSummaryView(request):
    return render(request,'coaching-summary-view.html')

def qualityDashboard(request):

    return render(request,'quality-dashboard.html')


def exportAuditReport(request):


    if request.method == 'POST':

        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        campaign = request.POST['process']

        ######  Export Function #############
        def exportAadyaseries(monform):

            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = ['process', 'empID', 'Associate Name', 'transaction date', 'Audit Date', 'overall_score',
                       'Fatal Count',
                       'qa', 'am', 'team_lead', 'manager', 'customer_name', 'customer_contact',

                       'Used Standard Opening Protocol',
                       'Introduction of Product / Branding',
                       'Call Closing as per the Protocol',

                       'Followed Hold Procedure Appropriately/Dead Air',
                       'Used Empathetic Statements whenever required',
                       'Clear Grammar & Communication',
                       'Acknowledged Appropriately',
                       'Active Listening without Interruption',

                       'Followed Policy & Procedure (Script)',
                       'Probing/Tactful finding/Rebuttal',
                       'Accurate Documentation',
                       'Disposition done correctly',
                       'Inaccurate Information',
                       'Advisor Sounding Rude / Proafinity Usage',

                       'status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = monform.objects.filter(audit_date__range=[start_date, end_date],
                                          ).values_list(
                'process', 'emp_id', 'associate_name', 'call_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager', 'customer_name', 'customer_contact',

                'oc_1',
                'oc_2',
                'oc_3',

                'softskill_1',
                'softskill_2',
                'softskill_3',
                'softskill_4',
                'softskill_5',

                'compliance_1',
                'compliance_2',
                'compliance_3',
                'compliance_4',
                'compliance_5',
                'compliance_6',

                'status', 'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response

        #######  campaigns  adya series ###########

        if campaign == 'AAdya':
            response = exportAadyaseries(MonitoringFormLeadsAadhyaSolution)
            return response

        elif campaign == 'AB Hindalco Outbound':
            response = exportAadyaseries(ABHindalcoOutboundMonForm)
            return response

        elif campaign == 'Aditya Birla Outbound':
            response = exportAadyaseries(AdityaBirlaOutboundMonForm)
            return response

        elif campaign == 'Insalvage':
            response = exportAadyaseries(MonitoringFormLeadsInsalvage)
            return response

        elif campaign == 'Medicare':
            response = exportAadyaseries(MonitoringFormLeadsMedicare)
            return response

        elif campaign == 'CTS':
            response = exportAadyaseries(MonitoringFormLeadsCTS)
            return response

        elif campaign == 'Tentamus Food':
            response = exportAadyaseries(MonitoringFormLeadsTentamusFood)
            return response

        elif campaign == 'Tentamus Pet':
            response = exportAadyaseries(MonitoringFormLeadsTentamusPet)
            return response

        elif campaign == 'City Security':
            response = exportAadyaseries(MonitoringFormLeadsCitySecurity)
            return response

        elif campaign == 'Allen Consulting':
            response = exportAadyaseries(MonitoringFormLeadsAllenConsulting)
            return response

        elif campaign == 'System4':
            response = exportAadyaseries(MonitoringFormLeadsSystem4)
            return response

        elif campaign == 'Louisville':
            response = exportAadyaseries(MonitoringFormLeadsLouisville)
            return response

        elif campaign == 'Info Think LLC':
            response = exportAadyaseries(MonitoringFormLeadsInfothinkLLC)
            return response

        elif campaign == 'PSECU':
            response = exportAadyaseries(MonitoringFormLeadsPSECU)
            return response

        elif campaign == 'Get A Rates':
            response = exportAadyaseries(MonitoringFormLeadsGetARates)
            return response

        elif campaign == 'Advance Consultants':
            response = exportAadyaseries(MonitoringFormLeadsAdvanceConsultants)
            return response

        elif campaign == 'MT Cosmetic':
            response = exportAadyaseries(MTCosmeticsMonForm)
            return response

        elif campaign == 'Upfront Online LLC':
            response = exportAadyaseries(UpfrontOnlineLLCMonform)
            return response

        elif campaign == 'Micro Distributing':
            response = exportAadyaseries(MicroDistributingMonForm)
            return response

        elif campaign == 'JJ Studio':
            response = exportAadyaseries(JJStudioMonForm)
            return response

        elif campaign == 'Zero Stress Marketing':
            response = exportAadyaseries(ZeroStressMarketingMonForm)
            return response

        elif campaign == 'WTU':
            response = exportAadyaseries(WTUMonForm)
            return response

        elif campaign == 'Roof Well':
            response = exportAadyaseries(RoofWellMonForm)
            return response

        elif campaign == 'Glyde App':
            response = exportAadyaseries(GlydeAppMonForm)
            return response

        elif campaign == 'Millennium Scientific':
            response = exportAadyaseries(MillenniumScientificMonForm)
            return response

        elif campaign == 'Stand Spot':
            response = exportAadyaseries(StandSpotMonForm)
            return response

        elif campaign == 'Cam Industrial':
            response = exportAadyaseries(CamIndustrialMonForm)
            return response

        elif campaign == 'Optimal Student Loan':
            response = exportAadyaseries(OptimalStudentLoanMonForm)
            return response

        elif campaign == 'Navigator Bio':
            response = exportAadyaseries(NavigatorBioMonForm)
            return response

        elif campaign == 'Ibiz':
            response = exportAadyaseries(IbizMonForm)
            return response

        elif campaign == 'Protostar':
            response = exportAadyaseries(ProtostarMonForm)
            return response

        elif campaign == 'Embassy Luxury':
            response = exportAadyaseries(EmbassyLuxuryMonForm)
            return response

        elif campaign == 'IIB':
            response = exportAadyaseries(IIBMonForm)
            return response

        elif campaign == 'Terraceo - Lead':
            response = exportAadyaseries(TerraceoLeadMonForm)
            return response
        elif campaign == 'Kalki Fashions':
            response = exportAadyaseries(KalkiFashions)
            return response

        if campaign == 'Scala':
            response = exportAadyaseries(ScalaMonForm)
            return response

        elif campaign == 'Citizen Capital':
            response = exportAadyaseries(CitizenCapitalMonForm)
            return response

        elif campaign == 'Golden East':
            response = exportAadyaseries(GoldenEastMonForm)
            return response

        elif campaign == 'Ri8Brain':
            response = exportAadyaseries(RitBrainMonForm)
            return response

        elif campaign == 'Restaurant Solution Group':
            response = exportAadyaseries(RestaurentSolMonForm)
            return response

        elif campaign == 'QBIQ':
            response = exportAadyaseries(QBIQMonForm)
            return response

        elif campaign == 'Accutime':
            response = exportAadyaseries(AccutimeMonForm)
            return response

        elif campaign == 'Solar Campaign':
            response = exportAadyaseries(SolarCampaignMonForm)
            return response

        elif campaign == 'Yes Health Molina':
            response = exportAadyaseries(YesHealthMolinaMonForm)
            return response

        elif campaign == 'Amerisave Outbound':
            response = exportAadyaseries(AmerisaveoutboundMonForm)
            return response
        elif campaign == 'BhagyaLakshmi Outbound':
            response = exportAadyaseries(BhagyaLakshmiOutbound)
            return response
        elif campaign == 'Clear View Outbound':
            response = exportAadyaseries(ClearViewOutboundMonForm)
            return response
        elif campaign == 'Daniel Wellington Outbound':
            response = exportAadyaseries(DanielWellingtonOutboundMonForm)
            return response
        elif campaign == 'Digital Swiss Gold Outbound':
            response = exportAadyaseries(DigitalSwissGoldOutboundMonForm)
            return response
        elif campaign == 'Healthyplus Outbound':
            response = exportAadyaseries(HealthyplusOutboundMonForm)
            return response
        elif campaign == 'Maxwell Properties':
            response = exportAadyaseries(MaxwellPropertiesOutboundMonForm)
            return response
        elif campaign == 'Movement of Insurance':
            response = exportAadyaseries(MovementofInsuranceOutboundMonForm)
            return response
        elif campaign == 'Sterling Strategies':
            response = exportAadyaseries(SterlingStrategiesOutboundMonForm)
            return response
        elif campaign == 'Tonn Coa Outbound':
            response = exportAadyaseries(TonnCoaOutboundMonForm)
            return response
        elif campaign == 'Wit Digital':
            response = exportAadyaseries(WitDigitalOutboundMonForm)
            return response

        elif campaign == 'PosTech':
            response = exportAadyaseries(PosTechOutboundMonForm)
            return response

        elif campaign == 'Schindler Media':
            response = exportAadyaseries(SchindlerMediaOutboundMonForm)
            return response

        elif campaign == 'UPS':
            response = exportAadyaseries(UPSOutboundMonForm)
            return response

        elif campaign == 'Pick Pack Deliveries':
            response = exportAadyaseries(PickPackDeliveriesMonForm)
            return response

        elif campaign == 'Marcelo Perez':
            response = exportAadyaseries(MarceloPerezMonForm)
            return response

        elif campaign == 'MedTech Group Outbound':
            response = exportAadyaseries(MedTechGroupOutboundMonForm)
            return response

        elif campaign == 'Digital Signage':
            response = exportAadyaseries(DigitalSignageOutboundMonForm)
            return response

        elif campaign == 'Hive Incubators Outbound':
            response = exportAadyaseries(HiveIncubatorsOutboundMonForm)
            return response

        elif campaign == 'Kaapi Machines Outbound':
            response = exportAadyaseries(KaapiMachinesOutboundMonForm)
            return response

        elif campaign == 'Somethings Brewing Outbound':
            response = exportAadyaseries(SomethingsBrewingOutboundMonForm)
            return response

        elif campaign == 'Naffa Outbound':
            response = exportAadyaseries(NaffaOutboundMonForm)
            return response

        elif campaign == 'JBN':
            response = exportAadyaseries(JBNOutboundMonForm)
            return response

        elif campaign == 'Quick Auto Parts':
            response = exportAadyaseries(QuickAutoPartsOutboundMonForm)
            return response

        elif campaign == 'Apex Communications Inc':
            response = exportAadyaseries(ApexCommunicationsOutboundMonForm)
            return response

        elif campaign == 'Law Offices of Robert and Geller':
            response = exportAadyaseries(LawOfficesOutboundMonForm)
            return response

        elif campaign == 'Woke Up Energy':
            response = exportAadyaseries(WokeUpEnergyOutboundMonForm)
            return response

        elif campaign == 'Finnesse Mortgage Outbound':
            response = exportAadyaseries(FinnesseMortgageOutboundMonForm)
            return response

        elif campaign == 'United Mortgage Outbound':
            response = exportAadyaseries(UnitedMortgageOutboundMonForm)
            return response

        ######## Inbound ###############################

        def exportinbound(monform):

            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = ['process', 'empID', 'Associate Name', 'transaction date', 'Audit Date', 'overall_score',
                       'Fatal Count',
                       'qa', 'am', 'team_lead', 'manager','customer_name','customer_contact',

                       'Used Standard Opening Protocol',
                       'Personalization ( Report Building, Addressing by Name)',
                       'Acknowledged Appropriately',
                       'Active Listening without Interruption / Paraphrasing',
                       'Used Empathetic Statements whenever required',
                       'Clear Grammar / Sentence Structure',
                       'Tone & Intonation / Rate of Speech',
                       'Diction/ Choice of Words / Phrase',
                       'Took Ownership on the call',
                       'Followed Hold Procedure Appropriately / Dead Air',
                       'Offered Additional Assistance & Closed Call as per Protocol',

                       'Probing / Tactful Finding / Rebuttal',
                       'Complete Information Provided',

                       'Professional / Courtesy',
                       'Verification process followed',
                       'Case Study',
                       'Process & Procedure Followed',
                       'First Call Resolution',

                       'status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = monform.objects.filter(audit_date__range=[start_date, end_date],
                                                                             ).values_list(
                'process', 'emp_id', 'associate_name', 'call_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager','customer_name','customer_contact',

                'ce_1',
                'ce_2',
                'ce_3',
                'ce_4',
                'ce_5',
                'ce_6',
                'ce_7',
                'ce_8',
                'ce_9',
                'ce_10',
                'ce_11',

                'business_1',
                'business_2',

                'compliance_1',
                'compliance_2',
                'compliance_3',
                'compliance_4',
                'compliance_5',

                'status', 'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response

        if campaign == 'Printer Pix Inbound':
            response = exportinbound(PrinterPixMasterMonitoringFormInboundCalls)
            return response
        elif campaign == 'AB Hindalco Inbound':
            response = exportinbound(ABHindalcoInboundMonForm)
            return response
        elif campaign == 'Aditya Birla Inbound':
            response = exportinbound(AdityaBirlainboundMonForm)
            return response
        elif campaign == 'AKDY Inbound':
            response = exportinbound(AKDYInboundMonFormNew)
            return response
        elif campaign == 'BhagyaLakshmi Inbound':
            response = exportinbound(BhagyaLakshmiInboundMonForm)
            return response
        elif campaign == 'Daniel Wellington Inbound':
            response = exportinbound(DanielwellingtoInboundMonForm)
            return response
        elif campaign == 'Digital Swiss Gold Inbound':
            response = exportinbound(DigitalSwissGoldInboundMonForm)
            return response
        elif campaign == 'Finesse Mortgage Inbound':
            response = exportinbound(FinesseMortgageInboundMonForm)
            return response
        elif campaign == 'Healthyplus Inbound':
            response = exportinbound(HealthyplusInboundMonForm)
            return response
        elif campaign == 'Kappi machine':
            response = exportinbound(KappimachineInboundCalls)
            return response
        elif campaign == 'Naffa Innovations':
            response = exportinbound(NaffaInnovationsInboundCalls)
            return response
        elif campaign == 'Nucleus Media':
            response = exportinbound(NuclusInboundCalls)
            return response
        elif campaign == 'Somethings Brewing':
            response = exportinbound(SomethingsBrewingInbound)
            return response
        elif campaign == 'Tonn Coa Inbound':
            response = exportinbound(MasterMonitoringFormTonnCoaInboundCalls)
            return response

        elif campaign == 'Rainbow Diagnostics':
            response = exportinbound(RainbowDiagnosticsInboundMonForm)
            return response

        elif campaign == 'Decentralized Vision LTD':
            response = exportinbound(DecentralizedVisionLTDInboundMonForm)
            return response

        elif campaign == 'IEDHH':
            response = exportinbound(IEDHHInboundMonForm)
            return response

        elif campaign == 'Amerisave Inbound':
            response = exportinbound(AmerisaveInboundMonForm)
            return response

        elif campaign == 'Clear View IT Inbound':
            response = exportinbound(ClearViewInboundMonForms)
            return response

        elif campaign == 'Quick Auto Parts Inbound':
            response = exportinbound(QuickAutoPartsInboundMonForms)
            return response

        #########    Email/CHat ##########################

        def exportEmailChat(monform):

            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = ['process', 'empID', 'Associate Name', 'transaction date', 'Audit Date', 'overall_score',
                       'Fatal Count',
                       'qa', 'am', 'team_lead', 'manager','customer_name','customer_contact',

                       'Associate used the standard greeting format',
                       'Appropriate responses ( acknowledging at the right time)',
                       'Ownership on Emails / Chat Answered within 30 Seconds',
                       'Personalization ( building a Raport, Addressing by name)',
                       'Empathy/Sympathy',
                       'Sentence structure',
                       'Punctuation (full stop, comma, and brackets, used in writing to separate sentences)',
                       'Grammar (Tense, Noun, etc.)',
                       'Probing done whenever necessary',
                       'Recap (Summarization of the conversation)',
                       'Associate used the standard closing format',

                       'Accurate Resolution/Information is provided as per the process',
                       'Worked on the Ticket Assigned / Chat Responded within 5 mins',

                       'Professional / Courtesy',
                       'Verification process followed',
                       'Case Study',
                       'Process & Procedure Followed',
                       'First Chat / Email Resolution',

                       'status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = monform.objects.filter(
                audit_date__range=[start_date, end_date],  ).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager','customer_name','customer_contact',

                'ce_1',
                'ce_2',
                'ce_3',
                'ce_4',
                'ce_5',
                'ce_6',
                'ce_7',
                'ce_8',
                'ce_9',
                'ce_10',
                'ce_11',

                'business_1',
                'business_2',

                'compliance_1',
                'compliance_2',
                'compliance_3',
                'compliance_4',
                'compliance_5',

                'status', 'closed_date', 'fatal','areas_improvement', 'positives', 'comments')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response

        if campaign == 'Printer Pix Chat Email':
            response = exportEmailChat(PrinterPixMasterMonitoringFormChatsEmail)
            return response
        elif campaign == 'AKDY - Email':
            response = exportEmailChat(AKDYEmailMonForm)
            return response
        elif campaign == 'Amerisave Email':
            response = exportEmailChat(AmerisaveEmailMonForm)
            return response
        elif campaign == 'Clear View Email':
            response = exportEmailChat(ClearViewEmailMonForm)
            return response
        elif campaign == 'Daniel Wellington - Chat - Email':
            response = exportEmailChat(DanielWellinChatEmailMonForm)
            return response
        elif campaign == 'Digital Swiss Gold Email - Chat':
            response = exportEmailChat(DigitalSwissGoldEmailChatMonForm)
            return response
        elif campaign == 'Finesse Mortgage Email':
            response = exportEmailChat(FinesseMortgageEmailMonForm)
            return response
        elif campaign == 'Fur Baby':
            response = exportEmailChat(FurBabyMonForm)
            return response
        elif campaign == 'Practo':
            response = exportEmailChat(PractoMonForm)
            return response
        elif campaign == 'Super Play':
            response = exportEmailChat(SuperPlayMonForm)
            return response
        elif campaign == 'Terraceo - Chat - Email':
            response = exportEmailChat(TerraceoChatEmailMonForm)
            return response
        elif campaign == 'Tonn Coa Chat Email':
            response = exportEmailChat(TonnChatsEmailNewMonForm)
            return response

        elif campaign == 'Rainbow Diagnostics Email':
            response = exportEmailChat(RainbowDiagnosticsEmailMonForm)
            return response

        elif campaign == 'Hive Incubator':
            response = exportEmailChat(HiveIncubatorEmailMonForm)
            return response

        elif campaign == 'MedTech Group Email':
            response = exportEmailChat(MedTechGroupEmailMonForm)
            return response

        elif campaign == 'Ri8 Brain Email':
            response = exportEmailChat(Ri8BrainEmailMonForm)
            return response

        elif campaign == 'Scala Email':
            response = exportEmailChat(ScalaEmailMonForm)
            return response

        elif campaign == 'kalki Fashion Email':
            response = exportEmailChat(KalkiFashionEmailMonForm)
            return response

        elif campaign == 'Maxwell Email':
            response = exportEmailChat(MaxwellEmailMonForm)
            return response

        elif campaign == 'Tanaor Jewelry':
            response = exportEmailChat(TanaorJewelryEmailMonForm)
            return response

        elif campaign == 'Decentralized Vision Email Chat':
            response = exportEmailChat(DecentralizedVisionEmailChatMonForm)
            return response

            ########## other campaigns ##############

        elif campaign == 'Fame House':

            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = ['process', 'empID', 'Associate Name', 'transaction date', 'Audit Date', 'overall_score',
                       'Fatal Count', 'qa', 'am', 'team_lead', 'manager', 'ticket_no', 'ticket_type',

                       'Shipping product incorrectly-wrong item, no exchange just shipping product',
                       'Responding to an escalated ticket/any ticket outside of agents skills/assignments',
                       'Overly rude to customer',
                       'Uses deragatory language or curse words',
                       'Not escalating a situation/Not following proper escalation proceedure',
                       'Double response-w/o addressing and apologizing, Sending same macro as last agent w/o edits',

                       'Agent sent response as public reply:',
                       'Agent greets customer by correct name',
                       'Agent thanked the customer for emailing our team',

                       'Agent addressed all questions asked:',
                       'Agent did not deflect/Avoid any questions/Policy unnecessarily:',
                       'Agent conveyed correct policy information to the customer:',
                       'Agent conveyed correct product information to the customer:',
                       'Agent established correct timeline to resolution :',

                       'Agent chose correct macro:',
                       "Agent tailored macro to fit the customer's question:",

                       'Agent composed email with logical flow/Does the information contained make sense?',
                       'Agent presented information with clear formatting: correct spelling and grammar throughout response',
                       'All company processes and policies were followed',

                       'Agent Correctly submitted ticket: Pending/On-Hold/Open/Solved',
                       'Agent filled out left hand side of ticket Correctly:',
                       'Agent merged tickets properly:',
                       'Agent completed all SH process correctly:',

                       'The agent was not rude, insulting, or discouraging:',
                       "Agent validated the customer's concern / questions / reason for contacting us:",
                       'Agent offered genuine, sympathetic statement for all loss or perceived loss of service at the first opportunity:',
                       'Agent did not accuse or place blame on the customer:',

                       'Agent asked the customer if they could be of additional help:',
                       'Agent used an appropriate closing:',

                       'status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = FameHouseNewMonForm.objects.filter(audit_date__range=[start_date, end_date],  ).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am', 'team_lead', 'manager', 'ticket_no', 'ticket_type',

                'compliance_1',
                'compliance_2',
                'compliance_3',
                'compliance_4',
                'compliance_5',
                'compliance_6',

                'opening_1',
                'opening_2',
                'opening_3',

                'cir_1',
                'cir_2',
                'cir_3',
                'cir_4',
                'cir_5',

                'macro_1',
                'macro_2',

                'formatting_1',
                'formatting_2',
                'formatting_3',

                'doc_1',
                'doc_2',
                'doc_3',
                'doc_4',

                'et_1',
                'et_2',
                'et_3',
                'et_4',

                'closing_1',
                'closing_2',

                'status', 'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response

        elif campaign == 'Noom POD':

            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = ['process', 'empID', 'Associate Name', 'transaction date', 'Audit Date', 'overall_score',
                       'Fatal Count',
                       'qa', 'am', 'team_lead', 'manager', 'ticket_no',

                       'If the user is missed to hit "finish" after sending the respective response. If the response is added with unwanted space and Punctuation. If the user name is miss-spelled/alphanumeric name on dashboard,we should use “Hey there!”.',
                       'If the "You last checked in" user is not sent with respective message or sent twice with the response',
                       'If the user are not assigned in spreadsheet. Ex: If the user code is not added in the spreadsheet.',
                       'If "was assigned to you" users are not hit finish',

                       "If a user's query is missed to answer and directly assigned to GS.",
                       'If the user is directly assigned without an Acknowledgement. If the user is sent with irrelevant response. If user is missed to assign to a coach while user wish to be assigned',
                       'If the response is sent with any irrelevant words or free handed messages. If the task is popped up as UU and YLCI the UU task should be our first priority',
                       'If the user has a System generated message of cancellation and CRO assigned to next GS. Negative empathy for user’s message!',
                       'If the user is missed to send the survey response and assigned directly. If the survey messages are swapped.',
                       'If the user has a question or information about Covid, that needs to addressed to coaches or Seek a help from the slack channels and then respond to it',

                       'status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = ChatMonitoringFormPodFather.objects.filter(audit_date__range=[start_date, end_date],
                                                              ).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager', 'ticket_no',

                'ce_1',
                'ce_2',
                'ce_3',
                'ce_4',

                'compliance_1',
                'compliance_2',
                'compliance_3',
                'compliance_4',
                'compliance_5',
                'compliance_6',

                'status', 'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response

        elif campaign == 'Noom Eva':

            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = ['process', 'empID', 'Associate Name', 'transaction date', 'Audit Date', 'overall_score',
                       'Fatal Count',
                       'qa', 'am', 'team_lead', 'manager', 'ticket_no',

                       'If the user is missed to hit "finish" after sending the respective response. If the response is added with unwanted space and Punctuation. If the user name is miss-spelled/alphanumeric name on dashboard,we should use “Hey there!”.',
                       'If the "You last checked in" user is not sent with respective message or sent twice with the response',
                       'If the user are not assigned in spreadsheet. Ex: If the user code is not added in the spreadsheet.',
                       'If "was assigned to you" users are not hit finish',

                       "If a user's query is missed to answer and directly assigned to GS.",
                       'If the user is directly assigned without an Acknowledgement. If the user is sent with irrelevant response. If user is missed to assign to a coach while user wish to be assigned',
                       'If the response is sent with any irrelevant words or free handed messages. If the task is popped up as UU and YLCI the UU task should be our first priority',
                       'If the user has a System generated message of cancellation and CRO assigned to next GS. Negative empathy for user’s message!',
                       'If the user is missed to send the survey response and assigned directly. If the survey messages are swapped.',
                       'If the user has a question or information about Covid, that needs to addressed to coaches or Seek a help from the slack channels and then respond to it',

                       'status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = ChatMonitoringFormEva.objects.filter(audit_date__range=[start_date, end_date],  ).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager', 'ticket_no',

                'ce_1',
                'ce_2',
                'ce_3',
                'ce_4',

                'compliance_1',
                'compliance_2',
                'compliance_3',
                'compliance_4',
                'compliance_5',
                'compliance_6',

                'status', 'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response

        ########## FLA #########################################
        elif campaign == 'FLA':

            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = ['process', 'empID', 'Associate Name', 'transaction date', 'Audit Date', 'overall_score',
                       'Fatal Count',
                       'qa', 'am', 'team_lead', 'manager',

                       'Check List Used Correctly',
                       'Reason for failure',

                       'status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = FLAMonitoringForm.objects.filter(
                audit_date__range=[start_date, end_date],  ).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager',

                'checklist_1',
                'reason_for_failure',

                'status', 'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response

        else:
            return redirect(request, 'error-pages/export-error.html')
    else:
        pass


def exportAuditReportQA(request):

    if request.method == 'POST':
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        qa = request.POST['qa']
        campaign = request.POST['process']

        ######  Export Function #############

        def exportAadyaseries(monform):

            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = ['process', 'empID', 'Associate Name', 'transaction date', 'Audit Date', 'overall_score',
                       'Fatal Count',
                       'qa', 'am', 'team_lead', 'manager', 'customer_name', 'customer_contact',

                       'Used Standard Opening Protocol',
                       'Introduction of Product / Branding',
                       'Call Closing as per the Protocol',

                       'Followed Hold Procedure Appropriately/Dead Air',
                       'Used Empathetic Statements whenever required',
                       'Clear Grammar & Communication',
                       'Acknowledged Appropriately',
                       'Active Listening without Interruption',

                       'Followed Policy & Procedure (Script)',
                       'Probing/Tactful finding/Rebuttal',
                       'Accurate Documentation',
                       'Disposition done correctly',
                       'Inaccurate Information',
                       'Advisor Sounding Rude / Proafinity Usage',

                       'status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = monform.objects.filter(audit_date__range=[start_date, end_date], qa=qa
                                          ).values_list(
                'process', 'emp_id', 'associate_name', 'call_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager', 'customer_name', 'customer_contact',

                'oc_1',
                'oc_2',
                'oc_3',

                'softskill_1',
                'softskill_2',
                'softskill_3',
                'softskill_4',
                'softskill_5',

                'compliance_1',
                'compliance_2',
                'compliance_3',
                'compliance_4',
                'compliance_5',
                'compliance_6',

                'status', 'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response

        #######  campaigns  adya series ###########

        if campaign == 'AAdya':
            response = exportAadyaseries(MonitoringFormLeadsAadhyaSolution)
            return response

        elif campaign == 'AB Hindalco Outbound':
            response = exportAadyaseries(ABHindalcoOutboundMonForm)
            return response

        elif campaign == 'Aditya Birla Outbound':
            response = exportAadyaseries(AdityaBirlaOutboundMonForm)
            return response

        elif campaign == 'Insalvage':
            response = exportAadyaseries(MonitoringFormLeadsInsalvage)
            return response

        elif campaign == 'Medicare':
            response = exportAadyaseries(MonitoringFormLeadsMedicare)
            return response

        elif campaign == 'CTS':
            response = exportAadyaseries(MonitoringFormLeadsCTS)
            return response

        elif campaign == 'Tentamus Food':
            response = exportAadyaseries(MonitoringFormLeadsTentamusFood)
            return response

        elif campaign == 'Tentamus Pet':
            response = exportAadyaseries(MonitoringFormLeadsTentamusPet)
            return response

        elif campaign == 'City Security':
            response = exportAadyaseries(MonitoringFormLeadsCitySecurity)
            return response

        elif campaign == 'Allen Consulting':
            response = exportAadyaseries(MonitoringFormLeadsAllenConsulting)
            return response

        elif campaign == 'System4':
            response = exportAadyaseries(MonitoringFormLeadsSystem4)
            return response

        elif campaign == 'Louisville':
            response = exportAadyaseries(MonitoringFormLeadsLouisville)
            return response

        elif campaign == 'Info Think LLC':
            response = exportAadyaseries(MonitoringFormLeadsInfothinkLLC)
            return response

        elif campaign == 'PSECU':
            response = exportAadyaseries(MonitoringFormLeadsPSECU)
            return response

        elif campaign == 'Get A Rates':
            response = exportAadyaseries(MonitoringFormLeadsGetARates)
            return response

        elif campaign == 'Advance Consultants':
            response = exportAadyaseries(MonitoringFormLeadsAdvanceConsultants)
            return response

        elif campaign == 'MT Cosmetic':
            response = exportAadyaseries(MTCosmeticsMonForm)
            return response

        elif campaign == 'Upfront Online LLC':
            response = exportAadyaseries(UpfrontOnlineLLCMonform)
            return response

        elif campaign == 'Micro Distributing':
            response = exportAadyaseries(MicroDistributingMonForm)
            return response

        elif campaign == 'JJ Studio':
            response = exportAadyaseries(JJStudioMonForm)
            return response

        elif campaign == 'Zero Stress Marketing':
            response = exportAadyaseries(ZeroStressMarketingMonForm)
            return response

        elif campaign == 'WTU':
            response = exportAadyaseries(WTUMonForm)
            return response

        elif campaign == 'Roof Well':
            response = exportAadyaseries(RoofWellMonForm)
            return response

        elif campaign == 'Glyde App':
            response = exportAadyaseries(GlydeAppMonForm)
            return response

        elif campaign == 'Millennium Scientific':
            response = exportAadyaseries(MillenniumScientificMonForm)
            return response

        elif campaign == 'Stand Spot':
            response = exportAadyaseries(StandSpotMonForm)
            return response

        elif campaign == 'Cam Industrial':
            response = exportAadyaseries(CamIndustrialMonForm)
            return response

        elif campaign == 'Optimal Student Loan':
            response = exportAadyaseries(OptimalStudentLoanMonForm)
            return response

        elif campaign == 'Navigator Bio':
            response = exportAadyaseries(NavigatorBioMonForm)
            return response

        elif campaign == 'Ibiz':
            response = exportAadyaseries(IbizMonForm)
            return response

        elif campaign == 'Protostar':
            response = exportAadyaseries(ProtostarMonForm)
            return response

        elif campaign == 'Embassy Luxury':
            response = exportAadyaseries(EmbassyLuxuryMonForm)
            return response

        elif campaign == 'IIB':
            response = exportAadyaseries(IIBMonForm)
            return response

        elif campaign == 'Terraceo - Lead':
            response = exportAadyaseries(TerraceoLeadMonForm)
            return response
        elif campaign == 'Kalki Fashions':
            response = exportAadyaseries(KalkiFashions)
            return response

        if campaign == 'Scala':
            response = exportAadyaseries(ScalaMonForm)
            return response

        elif campaign == 'Citizen Capital':
            response = exportAadyaseries(CitizenCapitalMonForm)
            return response

        elif campaign == 'Golden East':
            response = exportAadyaseries(GoldenEastMonForm)
            return response

        elif campaign == 'Ri8Brain':
            response = exportAadyaseries(RitBrainMonForm)
            return response

        elif campaign == 'Restaurant Solution Group':
            response = exportAadyaseries(RestaurentSolMonForm)
            return response

        elif campaign == 'QBIQ':
            response = exportAadyaseries(QBIQMonForm)
            return response

        elif campaign == 'Accutime':
            response = exportAadyaseries(AccutimeMonForm)
            return response

        elif campaign == 'Solar Campaign':
            response = exportAadyaseries(SolarCampaignMonForm)
            return response

        elif campaign == 'Yes Health Molina':
            response = exportAadyaseries(YesHealthMolinaMonForm)
            return response

        elif campaign == 'Amerisave Outbound':
            response = exportAadyaseries(AmerisaveoutboundMonForm)
            return response
        elif campaign == 'BhagyaLakshmi Outbound':
            response = exportAadyaseries(BhagyaLakshmiOutbound)
            return response
        elif campaign == 'Clear View Outbound':
            response = exportAadyaseries(ClearViewOutboundMonForm)
            return response
        elif campaign == 'Daniel Wellington Outbound':
            response = exportAadyaseries(DanielWellingtonOutboundMonForm)
            return response
        elif campaign == 'Digital Swiss Gold Outbound':
            response = exportAadyaseries(DigitalSwissGoldOutboundMonForm)
            return response
        elif campaign == 'Healthyplus Outbound':
            response = exportAadyaseries(HealthyplusOutboundMonForm)
            return response
        elif campaign == 'Maxwell Properties':
            response = exportAadyaseries(MaxwellPropertiesOutboundMonForm)
            return response
        elif campaign == 'Movement of Insurance':
            response = exportAadyaseries(MovementofInsuranceOutboundMonForm)
            return response
        elif campaign == 'Sterling Strategies':
            response = exportAadyaseries(SterlingStrategiesOutboundMonForm)
            return response
        elif campaign == 'Tonn Coa Outbound':
            response = exportAadyaseries(TonnCoaOutboundMonForm)
            return response
        elif campaign == 'Wit Digital':
            response = exportAadyaseries(WitDigitalOutboundMonForm)
            return response

        elif campaign == 'PosTech':
            response = exportAadyaseries(PosTechOutboundMonForm)
            return response

        elif campaign == 'Schindler Media':
            response = exportAadyaseries(SchindlerMediaOutboundMonForm)
            return response

        elif campaign == 'UPS':
            response = exportAadyaseries(UPSOutboundMonForm)
            return response

        elif campaign == 'Pick Pack Deliveries':
            response = exportAadyaseries(PickPackDeliveriesMonForm)
            return response

        elif campaign == 'Marcelo Perez':
            response = exportAadyaseries(MarceloPerezMonForm)
            return response

        elif campaign == 'MedTech Group Outbound':
            response = exportAadyaseries(MedTechGroupOutboundMonForm)
            return response

        elif campaign == 'Digital Signage':
            response = exportAadyaseries(DigitalSignageOutboundMonForm)
            return response

        elif campaign == 'Hive Incubators Outbound':
            response = exportAadyaseries(HiveIncubatorsOutboundMonForm)
            return response

        elif campaign == 'Kaapi Machines Outbound':
            response = exportAadyaseries(KaapiMachinesOutboundMonForm)
            return response

        elif campaign == 'Somethings Brewing Outbound':
            response = exportAadyaseries(SomethingsBrewingOutboundMonForm)
            return response

        elif campaign == 'Naffa Outbound':
            response = exportAadyaseries(NaffaOutboundMonForm)
            return response

        elif campaign == 'JBN':
            response = exportAadyaseries(JBNOutboundMonForm)
            return response

        elif campaign == 'Quick Auto Parts':
            response = exportAadyaseries(QuickAutoPartsOutboundMonForm)
            return response

        elif campaign == 'Apex Communications Inc':
            response = exportAadyaseries(ApexCommunicationsOutboundMonForm)
            return response

        elif campaign == 'Law Offices of Robert and Geller':
            response = exportAadyaseries(LawOfficesOutboundMonForm)
            return response

        elif campaign == 'Woke Up Energy':
            response = exportAadyaseries(WokeUpEnergyOutboundMonForm)
            return response

        elif campaign == 'Finnesse Mortgage Outbound':
            response = exportAadyaseries(FinnesseMortgageOutboundMonForm)
            return response

        elif campaign == 'United Mortgage Outbound':
            response = exportAadyaseries(UnitedMortgageOutboundMonForm)
            return response


        ######## Inbound ###############################

        def exportinbound(monform):

            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = ['process', 'empID', 'Associate Name', 'transaction date', 'Audit Date', 'overall_score',
                       'Fatal Count',
                       'qa', 'am', 'team_lead', 'manager','customer_name','customer_contact',

                       'Used Standard Opening Protocol',
                       'Personalization ( Report Building, Addressing by Name)',
                       'Acknowledged Appropriately',
                       'Active Listening without Interruption / Paraphrasing',
                       'Used Empathetic Statements whenever required',
                       'Clear Grammar / Sentence Structure',
                       'Tone & Intonation / Rate of Speech',
                       'Diction/ Choice of Words / Phrase',
                       'Took Ownership on the call',
                       'Followed Hold Procedure Appropriately / Dead Air',
                       'Offered Additional Assistance & Closed Call as per Protocol',

                       'Probing / Tactful Finding / Rebuttal',
                       'Complete Information Provided',

                       'Professional / Courtesy',
                       'Verification process followed',
                       'Case Study',
                       'Process & Procedure Followed',
                       'First Call Resolution',

                       'status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = monform.objects.filter(audit_date__range=[start_date, end_date], qa=qa
                                                                             ).values_list(
                'process', 'emp_id', 'associate_name', 'call_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager','customer_name','customer_contact',

                'ce_1',
                'ce_2',
                'ce_3',
                'ce_4',
                'ce_5',
                'ce_6',
                'ce_7',
                'ce_8',
                'ce_9',
                'ce_10',
                'ce_11',

                'business_1',
                'business_2',

                'compliance_1',
                'compliance_2',
                'compliance_3',
                'compliance_4',
                'compliance_5',

                'status', 'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response

        if campaign == 'Printer Pix Inbound':
            response = exportinbound(PrinterPixMasterMonitoringFormInboundCalls)
            return response
        elif campaign == 'AB Hindalco Inbound':
            response = exportinbound(ABHindalcoInboundMonForm)
            return response
        elif campaign == 'Aditya Birla Inbound':
            response = exportinbound(AdityaBirlainboundMonForm)
            return response
        elif campaign == 'AKDY Inbound':
            response = exportinbound(AKDYInboundMonFormNew)
            return response
        elif campaign == 'BhagyaLakshmi Inbound':
            response = exportinbound(BhagyaLakshmiInboundMonForm)
            return response
        elif campaign == 'Daniel Wellington Inbound':
            response = exportinbound(DanielwellingtoInboundMonForm)
            return response
        elif campaign == 'Digital Swiss Gold Inbound':
            response = exportinbound(DigitalSwissGoldInboundMonForm)
            return response
        elif campaign == 'Finesse Mortgage Inbound':
            response = exportinbound(FinesseMortgageInboundMonForm)
            return response
        elif campaign == 'Healthyplus Inbound':
            response = exportinbound(HealthyplusInboundMonForm)
            return response
        elif campaign == 'Kappi machine':
            response = exportinbound(KappimachineInboundCalls)
            return response
        elif campaign == 'Naffa Innovations':
            response = exportinbound(NaffaInnovationsInboundCalls)
            return response
        elif campaign == 'Nucleus Media':
            response = exportinbound(NuclusInboundCalls)
            return response
        elif campaign == 'Somethings Brewing':
            response = exportinbound(SomethingsBrewingInbound)
            return response
        elif campaign == 'Tonn Coa Inbound':
            response = exportinbound(MasterMonitoringFormTonnCoaInboundCalls)
            return response

        elif campaign == 'Rainbow Diagnostics':
            response = exportinbound(RainbowDiagnosticsInboundMonForm)
            return response

        elif campaign == 'Decentralized Vision LTD':
            response = exportinbound(DecentralizedVisionLTDInboundMonForm)
            return response

        elif campaign == 'IEDHH':
            response = exportinbound(IEDHHInboundMonForm)
            return response

        elif campaign == 'Amerisave Inbound':
            response = exportinbound(AmerisaveInboundMonForm)
            return response

        elif campaign == 'Clear View IT Inbound':
            response = exportinbound(ClearViewInboundMonForms)
            return response

        elif campaign == 'Quick Auto Parts Inbound':
            response = exportinbound(QuickAutoPartsInboundMonForms)
            return response

        #########    Email/CHat ##########################

        def exportEmailChat(monform):

            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = ['process', 'empID', 'Associate Name', 'transaction date', 'Audit Date', 'overall_score',
                       'Fatal Count',
                       'qa', 'am', 'team_lead', 'manager','customer_name','customer_contact',

                       'Associate used the standard greeting format',
                       'Appropriate responses ( acknowledging at the right time)',
                       'Ownership on Emails / Chat Answered within 30 Seconds',
                       'Personalization ( building a Raport, Addressing by name)',
                       'Empathy/Sympathy',
                       'Sentence structure',
                       'Punctuation (full stop, comma, and brackets, used in writing to separate sentences)',
                       'Grammar (Tense, Noun, etc.)',
                       'Probing done whenever necessary',
                       'Recap (Summarization of the conversation)',
                       'Associate used the standard closing format',

                       'Accurate Resolution/Information is provided as per the process',
                       'Worked on the Ticket Assigned / Chat Responded within 5 mins',

                       'Professional / Courtesy',
                       'Verification process followed',
                       'Case Study',
                       'Process & Procedure Followed',
                       'First Chat / Email Resolution',

                       'status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = monform.objects.filter(
                audit_date__range=[start_date, end_date], qa=qa).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager','customer_name','customer_contact',

                'ce_1',
                'ce_2',
                'ce_3',
                'ce_4',
                'ce_5',
                'ce_6',
                'ce_7',
                'ce_8',
                'ce_9',
                'ce_10',
                'ce_11',

                'business_1',
                'business_2',

                'compliance_1',
                'compliance_2',
                'compliance_3',
                'compliance_4',
                'compliance_5',

                'status', 'closed_date', 'fatal','areas_improvement', 'positives', 'comments')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response

        if campaign == 'Printer Pix Chat Email':
            response = exportEmailChat(PrinterPixMasterMonitoringFormChatsEmail)
            return response
        elif campaign == 'AKDY - Email':
            response = exportEmailChat(AKDYEmailMonForm)
            return response
        elif campaign == 'Amerisave Email':
            response = exportEmailChat(AmerisaveEmailMonForm)
            return response
        elif campaign == 'Clear View Email':
            response = exportEmailChat(ClearViewEmailMonForm)
            return response
        elif campaign == 'Daniel Wellington - Chat - Email':
            response = exportEmailChat(DanielWellinChatEmailMonForm)
            return response
        elif campaign == 'Digital Swiss Gold Email - Chat':
            response = exportEmailChat(DigitalSwissGoldEmailChatMonForm)
            return response
        elif campaign == 'Finesse Mortgage Email':
            response = exportEmailChat(FinesseMortgageEmailMonForm)
            return response
        elif campaign == 'Fur Baby':
            response = exportEmailChat(FurBabyMonForm)
            return response
        elif campaign == 'Practo':
            response = exportEmailChat(PractoMonForm)
            return response
        elif campaign == 'Super Play':
            response = exportEmailChat(SuperPlayMonForm)
            return response
        elif campaign == 'Terraceo - Chat - Email':
            response = exportEmailChat(TerraceoChatEmailMonForm)
            return response
        elif campaign == 'Tonn Coa Chat Email':
            response = exportEmailChat(TonnChatsEmailNewMonForm)
            return response

        elif campaign == 'Rainbow Diagnostics Email':
            response = exportEmailChat(RainbowDiagnosticsEmailMonForm)
            return response

        elif campaign == 'Hive Incubator':
            response = exportEmailChat(HiveIncubatorEmailMonForm)
            return response

        elif campaign == 'MedTech Group Email':
            response = exportEmailChat(MedTechGroupEmailMonForm)
            return response

        elif campaign == 'Ri8 Brain Email':
            response = exportEmailChat(Ri8BrainEmailMonForm)
            return response

        elif campaign == 'Scala Email':
            response = exportEmailChat(ScalaEmailMonForm)
            return response

        elif campaign == 'kalki Fashion Email':
            response = exportEmailChat(KalkiFashionEmailMonForm)
            return response

        elif campaign == 'Maxwell Email':
            response = exportEmailChat(MaxwellEmailMonForm)
            return response

        elif campaign == 'Tanaor Jewelry':
            response = exportEmailChat(TanaorJewelryEmailMonForm)
            return response

        elif campaign == 'Decentralized Vision Email Chat':
            response = exportEmailChat(DecentralizedVisionEmailChatMonForm)
            return response


            ########## other campaigns ##############

        elif campaign == 'Fame House':

            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = ['process', 'empID', 'Associate Name', 'transaction date', 'Audit Date', 'overall_score',
                       'Fatal Count', 'qa', 'am', 'team_lead', 'manager', 'ticket_no', 'ticket_type',

                       'Shipping product incorrectly-wrong item, no exchange just shipping product',
                       'Responding to an escalated ticket/any ticket outside of agents skills/assignments',
                       'Overly rude to customer',
                       'Uses deragatory language or curse words',
                       'Not escalating a situation/Not following proper escalation proceedure',
                       'Double response-w/o addressing and apologizing, Sending same macro as last agent w/o edits',

                       'Agent sent response as public reply:',
                       'Agent greets customer by correct name',
                       'Agent thanked the customer for emailing our team',

                       'Agent addressed all questions asked:',
                       'Agent did not deflect/Avoid any questions/Policy unnecessarily:',
                       'Agent conveyed correct policy information to the customer:',
                       'Agent conveyed correct product information to the customer:',
                       'Agent established correct timeline to resolution :',

                       'Agent chose correct macro:',
                       "Agent tailored macro to fit the customer's question:",

                       'Agent composed email with logical flow/Does the information contained make sense?',
                       'Agent presented information with clear formatting: correct spelling and grammar throughout response',
                       'All company processes and policies were followed',

                       'Agent Correctly submitted ticket: Pending/On-Hold/Open/Solved',
                       'Agent filled out left hand side of ticket Correctly:',
                       'Agent merged tickets properly:',
                       'Agent completed all SH process correctly:',

                       'The agent was not rude, insulting, or discouraging:',
                       "Agent validated the customer's concern / questions / reason for contacting us:",
                       'Agent offered genuine, sympathetic statement for all loss or perceived loss of service at the first opportunity:',
                       'Agent did not accuse or place blame on the customer:',

                       'Agent asked the customer if they could be of additional help:',
                       'Agent used an appropriate closing:',

                       'status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = FameHouseNewMonForm.objects.filter(audit_date__range=[start_date, end_date], qa=qa).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am', 'team_lead', 'manager', 'ticket_no', 'ticket_type',

                'compliance_1',
                'compliance_2',
                'compliance_3',
                'compliance_4',
                'compliance_5',
                'compliance_6',

                'opening_1',
                'opening_2',
                'opening_3',

                'cir_1',
                'cir_2',
                'cir_3',
                'cir_4',
                'cir_5',

                'macro_1',
                'macro_2',

                'formatting_1',
                'formatting_2',
                'formatting_3',

                'doc_1',
                'doc_2',
                'doc_3',
                'doc_4',

                'et_1',
                'et_2',
                'et_3',
                'et_4',

                'closing_1',
                'closing_2',

                'status', 'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response

        elif campaign == 'Noom POD':

            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = ['process', 'empID', 'Associate Name', 'transaction date', 'Audit Date', 'overall_score',
                       'Fatal Count',
                       'qa', 'am', 'team_lead', 'manager', 'ticket_no',

                       'If the user is missed to hit "finish" after sending the respective response. If the response is added with unwanted space and Punctuation. If the user name is miss-spelled/alphanumeric name on dashboard,we should use “Hey there!”.',
                       'If the "You last checked in" user is not sent with respective message or sent twice with the response',
                       'If the user are not assigned in spreadsheet. Ex: If the user code is not added in the spreadsheet.',
                       'If "was assigned to you" users are not hit finish',

                       "If a user's query is missed to answer and directly assigned to GS.",
                       'If the user is directly assigned without an Acknowledgement. If the user is sent with irrelevant response. If user is missed to assign to a coach while user wish to be assigned',
                       'If the response is sent with any irrelevant words or free handed messages. If the task is popped up as UU and YLCI the UU task should be our first priority',
                       'If the user has a System generated message of cancellation and CRO assigned to next GS. Negative empathy for user’s message!',
                       'If the user is missed to send the survey response and assigned directly. If the survey messages are swapped.',
                       'If the user has a question or information about Covid, that needs to addressed to coaches or Seek a help from the slack channels and then respond to it',

                       'status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = ChatMonitoringFormPodFather.objects.filter(audit_date__range=[start_date, end_date], qa=qa
                                                              ).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager', 'ticket_no',

                'ce_1',
                'ce_2',
                'ce_3',
                'ce_4',

                'compliance_1',
                'compliance_2',
                'compliance_3',
                'compliance_4',
                'compliance_5',
                'compliance_6',

                'status', 'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response

        elif campaign == 'Noom Eva':

            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = ['process', 'empID', 'Associate Name', 'transaction date', 'Audit Date', 'overall_score',
                       'Fatal Count',
                       'qa', 'am', 'team_lead', 'manager', 'ticket_no',

                       'If the user is missed to hit "finish" after sending the respective response. If the response is added with unwanted space and Punctuation. If the user name is miss-spelled/alphanumeric name on dashboard,we should use “Hey there!”.',
                       'If the "You last checked in" user is not sent with respective message or sent twice with the response',
                       'If the user are not assigned in spreadsheet. Ex: If the user code is not added in the spreadsheet.',
                       'If "was assigned to you" users are not hit finish',

                       "If a user's query is missed to answer and directly assigned to GS.",
                       'If the user is directly assigned without an Acknowledgement. If the user is sent with irrelevant response. If user is missed to assign to a coach while user wish to be assigned',
                       'If the response is sent with any irrelevant words or free handed messages. If the task is popped up as UU and YLCI the UU task should be our first priority',
                       'If the user has a System generated message of cancellation and CRO assigned to next GS. Negative empathy for user’s message!',
                       'If the user is missed to send the survey response and assigned directly. If the survey messages are swapped.',
                       'If the user has a question or information about Covid, that needs to addressed to coaches or Seek a help from the slack channels and then respond to it',

                       'status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = ChatMonitoringFormEva.objects.filter(audit_date__range=[start_date, end_date], qa=qa).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager', 'ticket_no',

                'ce_1',
                'ce_2',
                'ce_3',
                'ce_4',

                'compliance_1',
                'compliance_2',
                'compliance_3',
                'compliance_4',
                'compliance_5',
                'compliance_6',

                'status', 'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response

        ########## FLA #########################################
        elif campaign == 'FLA':

            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = ['process', 'empID', 'Associate Name', 'transaction date', 'Audit Date', 'overall_score',
                       'Fatal Count',
                       'qa', 'am', 'team_lead', 'manager',

                       'Check List Used Correctly',
                       'Reason for failure',

                       'status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = FLAMonitoringForm.objects.filter(
                audit_date__range=[start_date, end_date], qa=qa).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager',

                'checklist_1',
                'reason_for_failure',

                'status', 'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response

        else:
            return redirect(request, 'error-pages/export-error.html')

    else:
        pass

#------------------ New Series MonForms ----------------copy Aadya---------#

def newSeriesMonForms(request):

    if request.method == 'POST':
        campaign_name = request.POST['campaign']
        def newseriesAddCoaching(monform):

            category='Outbound'
            associate_name = request.POST['empname']
            emp_id = request.POST['empid']
            qa = request.POST['qa']
            team_lead = request.POST['tl']
            customer_name=request.POST['customer']
            customer_contact=request.POST['customercontact']
            call_date = request.POST['calldate']
            audit_date = request.POST['auditdate']
            campaign = request.POST['campaign']
            concept = request.POST['concept']
            zone=request.POST['zone']
            call_duration=(int(request.POST['durationh'])*3600)+(int(request.POST['durationm'])*60)+int(request.POST['durations'])

            #######################################
            prof_obj = Profile.objects.get(emp_id=emp_id)
            manager = prof_obj.manager

            manager_emp_id_obj = Profile.objects.get(emp_name=manager)

            manager_emp_id = manager_emp_id_obj.emp_id
            manager_name = manager
            # Opening and Closing
            oc_1 = int(request.POST['oc_1'])
            oc_2 = int(request.POST['oc_2'])
            oc_3 = int(request.POST['oc_3'])

            oc_total = oc_1 + oc_2 + oc_3
            # Softskills
            softskill_1 = int(request.POST['softskill_1'])
            softskill_2 = int(request.POST['softskill_2'])
            softskill_3 = int(request.POST['softskill_3'])
            softskill_4 = int(request.POST['softskill_4'])
            softskill_5 = int(request.POST['softskill_5'])

            softskill_total = softskill_1 + softskill_2+ softskill_3+ softskill_4+softskill_5
            # Compliance
            compliance_1 = int(request.POST['compliance_1'])
            compliance_2 = int(request.POST['compliance_2'])
            compliance_3 = int(request.POST['compliance_3'])
            compliance_4 = int(request.POST['compliance_4'])
            compliance_5 = int(request.POST['compliance_5'])
            compliance_6 = int(request.POST['compliance_6'])

            compliance_total = compliance_1 + compliance_2 + compliance_3+compliance_4+compliance_5+compliance_6

            fatal_list = [compliance_1, compliance_2, compliance_3, compliance_4,compliance_5,compliance_6]
            fatal_list_count = []
            for i in fatal_list:
                if i == 0:
                    fatal_list_count.append(i)
            no_of_fatals = len(fatal_list_count)

            if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0 or compliance_4 == 0 or compliance_5 == 0 or compliance_6 == 0:
                overall_score = 0
                fatal = True
            else:
                overall_score = oc_total + softskill_total +compliance_total
                fatal = False

            areas_improvement = request.POST['areaimprovement']
            positives = request.POST['positives']
            comments = request.POST['comments']
            added_by = request.user.profile.emp_name
            week = request.POST['week']
            am = request.POST['am']

            leadsales = monform(
                                associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                manager=manager_name,manager_id=manager_emp_id,
                                call_date=call_date, audit_date=audit_date, customer_name=customer_name,customer_contact=customer_contact,
                                campaign=campaign, concept=concept, zone=zone,call_duration=call_duration,
                                oc_1=oc_1,oc_2=oc_2,oc_3=oc_3,
                                softskill_1=softskill_1,softskill_2=softskill_2,softskill_3=softskill_3,softskill_4=softskill_4,softskill_5=softskill_5,softskill_total=softskill_total,
                                compliance_1=compliance_1, compliance_2=compliance_2,compliance_3=compliance_3,compliance_4=compliance_4,compliance_5=compliance_5,compliance_6=compliance_6,
                                compliance_total=compliance_total,
                                areas_improvement=areas_improvement,
                                positives=positives, comments=comments,
                                added_by=added_by,
                                overall_score=overall_score,category=category,
                                week=week,am=am,fatal_count=no_of_fatals,fatal=fatal,ce_total=oc_total,
                                )
            leadsales.save()

        if campaign_name == 'Zero Stress Marketing':
            newseriesAddCoaching(ZeroStressMarketingMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'WTU':
            newseriesAddCoaching(WTUMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Roof Well':
            newseriesAddCoaching(RoofWellMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Glyde App':
            newseriesAddCoaching(GlydeAppMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Millennium Scientific':
            newseriesAddCoaching(MillenniumScientificMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Stand Spot':
            newseriesAddCoaching(StandSpotMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Cam Industrial':
            newseriesAddCoaching(CamIndustrialMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Optimal Student Loan':
            newseriesAddCoaching(OptimalStudentLoanMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Navigator Bio':
            newseriesAddCoaching(NavigatorBioMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'AAdya':
            newseriesAddCoaching(MonitoringFormLeadsAadhyaSolution)
            return redirect('/employees/qahome')

        elif campaign_name == 'Insalvage':
            newseriesAddCoaching(MonitoringFormLeadsInsalvage)
            return redirect('/employees/qahome')

        elif campaign_name == 'Medicare':
            newseriesAddCoaching(MonitoringFormLeadsMedicare)
            return redirect('/employees/qahome')

        elif campaign_name == 'CTS':
            newseriesAddCoaching(MonitoringFormLeadsCTS)
            return redirect('/employees/qahome')

        elif campaign_name == 'Tentamus Food':
            newseriesAddCoaching(MonitoringFormLeadsTentamusFood)
            return redirect('/employees/qahome')

        elif campaign_name == 'Tentamus Pet':
            newseriesAddCoaching(MonitoringFormLeadsTentamusPet)
            return redirect('/employees/qahome')

        elif campaign_name == 'City Security':
            newseriesAddCoaching(MonitoringFormLeadsCitySecurity)
            return redirect('/employees/qahome')

        elif campaign_name == 'Allen Consulting':
            newseriesAddCoaching(MonitoringFormLeadsAllenConsulting)
            return redirect('/employees/qahome')

        elif campaign_name == 'System4':
            newseriesAddCoaching(MonitoringFormLeadsSystem4)
            return redirect('/employees/qahome')

        elif campaign_name == 'Louisville':
            newseriesAddCoaching(MonitoringFormLeadsLouisville)
            return redirect('/employees/qahome')

        elif campaign_name == 'Info Think LLC':
            newseriesAddCoaching(MonitoringFormLeadsInfothinkLLC)
            return redirect('/employees/qahome')

        elif campaign_name == 'PSECU':
            newseriesAddCoaching(MonitoringFormLeadsPSECU)
            return redirect('/employees/qahome')

        elif campaign_name == 'Get A Rates':
            newseriesAddCoaching(MonitoringFormLeadsGetARates)
            return redirect('/employees/qahome')

        elif campaign_name == 'Advance Consultants':
            newseriesAddCoaching(MonitoringFormLeadsAdvanceConsultants)
            return redirect('/employees/qahome')

        elif campaign_name == 'MT Cosmetic':
            newseriesAddCoaching(MTCosmeticsMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Upfront Online LLC':
            newseriesAddCoaching(UpfrontOnlineLLCMonform)
            return redirect('/employees/qahome')

        elif campaign_name == 'Micro Distributing':
            newseriesAddCoaching(MicroDistributingMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'JJ Studio':
            newseriesAddCoaching(JJStudioMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Ibiz':
            newseriesAddCoaching(IbizMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Protostar':
            newseriesAddCoaching(ProtostarMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Embassy Luxury':
            newseriesAddCoaching(EmbassyLuxuryMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'IIB':
            newseriesAddCoaching(IIBMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Terraceo - Lead':
            newseriesAddCoaching(TerraceoLeadMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Kalki Fashions':
            newseriesAddCoaching(KalkiFashions)
            return redirect('/employees/qahome')

        elif campaign_name == 'Scala':
            newseriesAddCoaching(ScalaMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Citizen Capital':
            newseriesAddCoaching(CitizenCapitalMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Golden East':
            newseriesAddCoaching(GoldenEastMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Ri8Brain':
            newseriesAddCoaching(RitBrainMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Restaurant Solution Group':
            newseriesAddCoaching(RestaurentSolMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'QBIQ':
            newseriesAddCoaching(QBIQMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Accutime':
            newseriesAddCoaching(AccutimeMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Solar Campaign':
            newseriesAddCoaching(SolarCampaignMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Yes Health Molina':
            newseriesAddCoaching(YesHealthMolinaMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'AB Hindalco Outbound':
            newseriesAddCoaching(ABHindalcoOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Aditya Birla Outbound':
            newseriesAddCoaching(AdityaBirlaOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Amerisave Outbound':
            newseriesAddCoaching(AmerisaveoutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'BhagyaLakshmi Outbound':
            newseriesAddCoaching(BhagyaLakshmiOutbound)
            return redirect('/employees/qahome')

        elif campaign_name == 'Clear View Outbound':
            newseriesAddCoaching(ClearViewOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Daniel Wellington Outbound':
            newseriesAddCoaching(DanielWellingtonOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Digital Swiss Gold Outbound':
            newseriesAddCoaching(DigitalSwissGoldOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Healthyplus Outbound':
            newseriesAddCoaching(HealthyplusOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Maxwell Properties':
            newseriesAddCoaching(MaxwellPropertiesOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Movement of Insurance':
            newseriesAddCoaching(MovementofInsuranceOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Sterling Strategies':
            newseriesAddCoaching(SterlingStrategiesOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Tonn Coa Outbound':
            newseriesAddCoaching(TonnCoaOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Wit Digital':
            newseriesAddCoaching(WitDigitalOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'PosTech':
            newseriesAddCoaching(PosTechOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Schindler Media':
            newseriesAddCoaching(SchindlerMediaOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'UPS':
            newseriesAddCoaching(UPSOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Pick Pack Deliveries':
            newseriesAddCoaching(PickPackDeliveriesMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Marcelo Perez':
            newseriesAddCoaching(MarceloPerezMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'MedTech Group Outbound':
            newseriesAddCoaching(MedTechGroupOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Digital Signage':
            newseriesAddCoaching(DigitalSignageOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Hive Incubators Outbound':
            newseriesAddCoaching(HiveIncubatorsOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Kaapi Machines Outbound':
            newseriesAddCoaching(KaapiMachinesOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Somethings Brewing Outbound':
            newseriesAddCoaching(SomethingsBrewingOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Naffa Outbound':
            newseriesAddCoaching(NaffaOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'JBN':
            newseriesAddCoaching(JBNOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Quick Auto Parts':
            newseriesAddCoaching(QuickAutoPartsOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Apex Communications Inc':
            newseriesAddCoaching(ApexCommunicationsOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Law Offices of Robert and Geller':
            newseriesAddCoaching(LawOfficesOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Woke Up Energy':
            newseriesAddCoaching(WokeUpEnergyOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Finnesse Mortgage Outbound':
            newseriesAddCoaching(FinnesseMortgageOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'United Mortgage Outbound':
            newseriesAddCoaching(UnitedMortgageOutboundMonForm)
            return redirect('/employees/qahome')

        else:
            pass


    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/new-series-comon.html', data)


def newSeriesInboundForms(request):
    if request.method == 'POST':
        campaign_name = request.POST['campaign']

        def inboundAddCoaching(monform):
            category = 'Inbound'
            associate_name = request.POST['empname']
            emp_id = request.POST['empid']
            qa = request.POST['qa']
            team_lead = request.POST['tl']
            customer_name = request.POST['customer']
            customer_contact = request.POST['customercontact']
            call_date = request.POST['calldate']
            audit_date = request.POST['auditdate']
            campaign = request.POST['campaign']
            concept = request.POST['concept']
            zone = request.POST['zone']
            call_duration = (int(request.POST['durationh']) * 3600) + (int(request.POST['durationm']) * 60) + int(request.POST['durations'])

            prof_obj = Profile.objects.get(emp_id=emp_id)
            manager = prof_obj.manager
            manager_emp_id_obj = Profile.objects.get(emp_name=manager)
            manager_emp_id = manager_emp_id_obj.emp_id
            manager_name = manager
            # Customer Experience
            ce_1 = int(request.POST['ce_1'])
            ce_2 = int(request.POST['ce_2'])
            ce_3 = int(request.POST['ce_3'])
            ce_4 = int(request.POST['ce_4'])
            ce_5 = int(request.POST['ce_5'])
            ce_6 = int(request.POST['ce_6'])
            ce_7 = int(request.POST['ce_7'])
            ce_8 = int(request.POST['ce_8'])
            ce_9 = int(request.POST['ce_9'])
            ce_10 = int(request.POST['ce_10'])
            ce_11 = int(request.POST['ce_11'])

            ce_total = ce_1 + ce_2 + ce_3 + ce_4 + ce_5 + ce_6 + ce_7 + ce_8 + ce_9 + ce_10 + ce_11

            # Business
            business_1 = int(request.POST['business_1'])
            business_2 = int(request.POST['business_2'])
            business_total = business_1 + business_2

            # Compliance
            compliance_1 = int(request.POST['compliance_1'])
            compliance_2 = int(request.POST['compliance_2'])
            compliance_3 = int(request.POST['compliance_3'])
            compliance_4 = int(request.POST['compliance_4'])
            compliance_5 = int(request.POST['compliance_5'])

            compliance_total = compliance_1 + compliance_2 + compliance_3 + compliance_4 + compliance_5

            fatal_list = [compliance_1, compliance_2, compliance_3, compliance_4, compliance_5]
            fatal_list_count = []
            for i in fatal_list:
                if i == 0:
                    fatal_list_count.append(i)

            no_of_fatals = len(fatal_list_count)

            if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0 or compliance_4 == 0 or compliance_5 == 0:
                overall_score = 0
                fatal = True
            else:
                overall_score = ce_total + business_total + compliance_total
                fatal = False

            areas_improvement = request.POST['areaimprovement']
            positives = request.POST['positives']
            comments = request.POST['comments']
            added_by = request.user.profile.emp_name

            week = request.POST['week']
            am = request.POST['am']

            inbound = monform(associate_name=associate_name, emp_id=emp_id, qa=qa,team_lead=team_lead,manager=manager_name, manager_id=manager_emp_id,

                                                                 call_date=call_date, audit_date=audit_date,
                                                                 customer_name=customer_name,
                                                                 customer_contact=customer_contact,
                                                                 campaign=campaign, concept=concept, zone=zone,
                                                                 call_duration=call_duration,

                                                                 ce_1=ce_1, ce_2=ce_2, ce_3=ce_3, ce_4=ce_4, ce_5=ce_5,
                                                                 ce_6=ce_6, ce_7=ce_7, ce_8=ce_8, ce_9=ce_9,
                                                                 ce_10=ce_10, ce_11=ce_11,
                                                                 ce_total=ce_total,

                                                                 business_1=business_1, business_2=business_2,
                                                                 business_total=business_total,

                                                                 compliance_1=compliance_1, compliance_2=compliance_2,
                                                                 compliance_3=compliance_3, compliance_4=compliance_4,
                                                                 compliance_5=compliance_5,
                                                                 compliance_total=compliance_total,

                                                                 areas_improvement=areas_improvement,
                                                                 positives=positives, comments=comments,
                                                                 added_by=added_by,

                                                                 overall_score=overall_score, category=category,
                                                                 week=week, am=am, fatal_count=no_of_fatals, fatal=fatal
                                                                 )
            inbound.save()

        if campaign_name == 'Tonn Coa Inbound':
            inboundAddCoaching(MasterMonitoringFormTonnCoaInboundCalls)
            return redirect('/employees/qahome')

        elif campaign_name == 'Somethings Brewing':
            inboundAddCoaching(SomethingsBrewingInbound)
            return redirect('/employees/qahome')

        elif campaign_name == 'Printer Pix Inbound':
            inboundAddCoaching(PrinterPixMasterMonitoringFormInboundCalls)
            return redirect('/employees/qahome')

        elif campaign_name == 'Nucleus Media':
            inboundAddCoaching(NuclusInboundCalls)
            return redirect('/employees/qahome')

        elif campaign_name == 'Naffa Innovations':
            inboundAddCoaching(NaffaInnovationsInboundCalls)
            return redirect('/employees/qahome')

        elif campaign_name == 'Kappi machine':
            inboundAddCoaching(KappimachineInboundCalls)
            return redirect('/employees/qahome')

        elif campaign_name == 'Healthyplus Inbound':
            inboundAddCoaching(HealthyplusInboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Finesse Mortgage Inbound':
            inboundAddCoaching(FinesseMortgageInboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Digital Swiss Gold Inbound':
            inboundAddCoaching(DigitalSwissGoldInboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Daniel Wellington Inbound':
            inboundAddCoaching(DanielwellingtoInboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'BhagyaLakshmi Inbound':
            inboundAddCoaching(BhagyaLakshmiInboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'AKDY Inbound':
            inboundAddCoaching(AKDYInboundMonFormNew)
            return redirect('/employees/qahome')

        elif campaign_name == 'Aditya Birla Inbound':
            inboundAddCoaching(AdityaBirlainboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'AB Hindalco Inbound':
            inboundAddCoaching(ABHindalcoInboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Rainbow Diagnostics':
            inboundAddCoaching(RainbowDiagnosticsInboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Decentralized Vision LTD':
            inboundAddCoaching(DecentralizedVisionLTDInboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'IEDHH':
            inboundAddCoaching(IEDHHInboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Amerisave Inbound':
            inboundAddCoaching(AmerisaveInboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Clear View IT Inbound':
            inboundAddCoaching(ClearViewInboundMonForms)
            return redirect('/employees/qahome')

        elif campaign_name == 'Quick Auto Parts Inbound':
            inboundAddCoaching(QuickAutoPartsInboundMonForms)
            return redirect('/employees/qahome')


    else:
        pass



############### Doestic Chat Email #################

def domesticChatEmail(request):

    if request.method == 'POST':
        campaign_name = request.POST['campaign']

        def domesticEmailChatAddCoaching(monform):

            category = 'Email - Chat'
            associate_name = request.POST['empname']
            emp_id = request.POST['empid']
            qa = request.POST['qa']
            team_lead = request.POST['tl']
            customer_name = request.POST['customer']
            customer_contact = request.POST['customercontact']
            trans_date = request.POST['trans_date']
            audit_date = request.POST['auditdate']
            campaign = request.POST['campaign']
            concept = request.POST['concept']
            zone = request.POST['zone']
            duration=(int(request.POST['durationh'])*3600)+(int(request.POST['durationm'])*60)+int(request.POST['durations'])

            #######################################
            prof_obj = Profile.objects.get(emp_id=emp_id)
            manager = prof_obj.manager

            manager_emp_id_obj = Profile.objects.get(emp_name=manager)

            manager_emp_id = manager_emp_id_obj.emp_id
            manager_name = manager
            #########################################

            # Customer Experience
            ce_1 = int(request.POST['ce_1'])
            ce_2 = int(request.POST['ce_2'])
            ce_3 = int(request.POST['ce_3'])
            ce_4 = int(request.POST['ce_4'])
            ce_5 = int(request.POST['ce_5'])
            ce_6 = int(request.POST['ce_6'])
            ce_7 = int(request.POST['ce_7'])
            ce_8 = int(request.POST['ce_8'])
            ce_9 = int(request.POST['ce_9'])
            ce_10 = int(request.POST['ce_10'])
            ce_11 = int(request.POST['ce_11'])

            ce_total = ce_1 + ce_2 + ce_3 + ce_4 + ce_5 + ce_6 + ce_7 + ce_8 + ce_9 + ce_10 + ce_11

            # Business
            business_1 = int(request.POST['business_1'])
            business_2 = int(request.POST['business_2'])

            business_total = business_1 + business_2

            # Compliance
            compliance_1 = int(request.POST['compliance_1'])
            compliance_2 = int(request.POST['compliance_2'])
            compliance_3 = int(request.POST['compliance_3'])
            compliance_4 = int(request.POST['compliance_4'])
            compliance_5 = int(request.POST['compliance_5'])

            compliance_total = compliance_1 + compliance_2 + compliance_3 + compliance_4 + compliance_5

            #################################################

            fatal_list = [compliance_1, compliance_2, compliance_3, compliance_4, compliance_5]
            fatal_list_count = []
            for i in fatal_list:
                if i == 0:
                    fatal_list_count.append(i)

            no_of_fatals = len(fatal_list_count)

            ####################################################

            if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0 or compliance_4 == 0 or compliance_5 == 0:
                overall_score = 0
                fatal = True
            else:
                overall_score = ce_total + business_total + compliance_total
                fatal = False

            areas_improvement = request.POST['areaimprovement']
            positives = request.POST['positives']
            comments = request.POST['comments']
            added_by = request.user.profile.emp_name

            week = request.POST['week']
            am = request.POST['am']

            domestic = monform(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                     manager=manager_name, manager_id=manager_emp_id,

                                     trans_date=trans_date, audit_date=audit_date, customer_name=customer_name,
                                     customer_contact=customer_contact,
                                     campaign=campaign, concept=concept, zone=zone, duration=duration,

                                     ce_1=ce_1, ce_2=ce_2, ce_3=ce_3, ce_4=ce_4, ce_5=ce_5, ce_6=ce_6, ce_7=ce_7,
                                     ce_8=ce_8, ce_9=ce_9, ce_10=ce_10, ce_11=ce_11,
                                     ce_total=ce_total,

                                     business_1=business_1, business_2=business_2, business_total=business_total,

                                     compliance_1=compliance_1, compliance_2=compliance_2, compliance_3=compliance_3,
                                     compliance_4=compliance_4, compliance_5=compliance_5,
                                     compliance_total=compliance_total,

                                     areas_improvement=areas_improvement,
                                     positives=positives, comments=comments,
                                     added_by=added_by,

                                     overall_score=overall_score, category=category,
                                     week=week, am=am, fatal_count=no_of_fatals, fatal=fatal
                                     )
            domestic.save()

        if campaign_name == 'Super Play':
            domesticEmailChatAddCoaching(SuperPlayMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Daniel Wellington - Chat - Email':
            domesticEmailChatAddCoaching(DanielWellinChatEmailMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Terraceo - Chat - Email':
            domesticEmailChatAddCoaching(TerraceoChatEmailMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Tonn Coa Chat Email':
            domesticEmailChatAddCoaching(TonnChatsEmailNewMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Printer Pix Chat Email':
            domesticEmailChatAddCoaching(PrinterPixMasterMonitoringFormChatsEmail)
            return redirect('/employees/qahome')

        elif campaign_name == 'Practo':
            domesticEmailChatAddCoaching(PractoMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Fur Baby':
            domesticEmailChatAddCoaching(FurBabyMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'AKDY - Email':
            domesticEmailChatAddCoaching(AKDYEmailMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Amerisave Email':
            domesticEmailChatAddCoaching(AmerisaveEmailMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Clear View Email':
            domesticEmailChatAddCoaching(ClearViewEmailMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Finesse Mortgage Email':
            domesticEmailChatAddCoaching(FinesseMortgageEmailMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Digital Swiss Gold Email - Chat':
            domesticEmailChatAddCoaching(DigitalSwissGoldEmailChatMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Rainbow Diagnostics Email':
            domesticEmailChatAddCoaching(RainbowDiagnosticsEmailMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Hive Incubator':
            domesticEmailChatAddCoaching(HiveIncubatorEmailMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'MedTech Group Email':
            domesticEmailChatAddCoaching(MedTechGroupEmailMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Ri8 Brain Email':
            domesticEmailChatAddCoaching(Ri8BrainEmailMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Scala Email':
            domesticEmailChatAddCoaching(ScalaEmailMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'kalki Fashion Email':
            domesticEmailChatAddCoaching(KalkiFashionEmailMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Maxwell Email':
            domesticEmailChatAddCoaching(MaxwellEmailMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Tanaor Jewelry':
            domesticEmailChatAddCoaching(TanaorJewelryEmailMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Decentralized Vision Email Chat':
            domesticEmailChatAddCoaching(DecentralizedVisionEmailChatMonForm)
            return redirect('/employees/qahome')


        else:
            pass

    else:
        return redirect('/employees/qahome')

# Other Forms

def chatCoachingformEva(request):
    if request.method == 'POST':
        category='Email/Chat Other'
        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        ticket_no=request.POST['ticketnumber']
        trans_date = request.POST['transdate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        evaluator=request.POST['evaluator']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################


        # Customer Experience
        ce_1 = int(request.POST['ce_1'])
        ce_2 = int(request.POST['ce_2'])
        ce_3 = int(request.POST['ce_3'])
        ce_4 = int(request.POST['ce_4'])

        ce_total=ce_1+ce_2+ce_3+ce_4

        #Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])
        compliance_4 = int(request.POST['compliance_4'])
        compliance_5 = int(request.POST['compliance_5'])
        compliance_6 = int(request.POST['compliance_6'])

        #################################################

        fatal_list = [compliance_1,compliance_2,compliance_3,compliance_4,compliance_5,compliance_6]
        fatal_list_count = []
        for i in fatal_list:
            if i == 0:
                fatal_list_count.append(i)

        no_of_fatals = len(fatal_list_count)

        ####################################################

        compliance_total=compliance_1+compliance_2+compliance_3+compliance_4+compliance_5+compliance_6

        if compliance_1==0 or compliance_2==0 or compliance_3==0 or compliance_4==0 or compliance_5==0 or compliance_6==0:
            overall_score=0
            fatal=True
        else:
            overall_score=ce_total+compliance_total
            fatal=False

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        week = request.POST['week']
        am = request.POST['am']

        chat = ChatMonitoringFormEva(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                     manager=manager_name,manager_id=manager_emp_id,

                                     trans_date=trans_date, audit_date=audit_date,ticket_no=ticket_no,
                                     campaign=campaign,concept=concept,evaluator=evaluator,

                                     ce_1=ce_1,ce_2=ce_2,ce_3=ce_3,ce_4=ce_4,ce_total=ce_total,

                                     compliance_1=compliance_1,compliance_2=compliance_2,compliance_3=compliance_3,
                                     compliance_4=compliance_4,compliance_5=compliance_5,compliance_6=compliance_6,
                                     compliance_total=compliance_total,

                                     areas_improvement=areas_improvement,
                                     positives=positives, comments=comments,
                                     added_by=added_by,

                                     overall_score=overall_score,category=category,
                                     week=week,am=am,fatal_count=no_of_fatals,fatal=fatal
                                     )
        chat.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/ECPL-EVA&NOVO-Monitoring-Form-chat.html', data)

def chatCoachingformPodFather(request):
    if request.method == 'POST':
        category='Email/Chat Other'
        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        ticket_no=request.POST['ticketnumber']
        trans_date = request.POST['transdate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        evaluator=request.POST['evaluator']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################

        # Customer Experience
        ce_1 = int(request.POST['ce_1'])
        ce_2 = int(request.POST['ce_2'])
        ce_3 = int(request.POST['ce_3'])
        ce_4 = int(request.POST['ce_4'])

        ce_total=ce_1+ce_2+ce_3+ce_4

        #Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])
        compliance_4 = int(request.POST['compliance_4'])
        compliance_5 = int(request.POST['compliance_5'])
        compliance_6 = int(request.POST['compliance_6'])

        #################################################

        fatal_list = [compliance_1, compliance_2, compliance_3, compliance_4, compliance_5, compliance_6]
        fatal_list_count = []
        for i in fatal_list:
            if i == 0:
                fatal_list_count.append(i)

        no_of_fatals = len(fatal_list_count)

        ####################################################

        compliance_total=compliance_1+compliance_2+compliance_3+compliance_4+compliance_5+compliance_6

        if compliance_1==0 or compliance_2==0 or compliance_3==0 or compliance_4==0 or compliance_5==0 or compliance_6==0:
            overall_score=0
            fatal =True
        else:
            overall_score=ce_total+compliance_total
            fatal = False

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        week = request.POST['week']
        am = request.POST['am']

        chat = ChatMonitoringFormPodFather(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                           manager=manager_name,manager_id=manager_emp_id,

                                     trans_date=trans_date, audit_date=audit_date,ticket_no=ticket_no,
                                     campaign=campaign,concept=concept,evaluator=evaluator,

                                     ce_1=ce_1,ce_2=ce_2,ce_3=ce_3,ce_4=ce_4,ce_total=ce_total,

                                     compliance_1=compliance_1,compliance_2=compliance_2,compliance_3=compliance_3,
                                     compliance_4=compliance_4,compliance_5=compliance_5,compliance_6=compliance_6,
                                     compliance_total=compliance_total,

                                     areas_improvement=areas_improvement,
                                     positives=positives, comments=comments,
                                     added_by=added_by,

                                     overall_score=overall_score,category=category,
                                           week=week,am=am,fatal_count=no_of_fatals,fatal=fatal
                                     )
        chat.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request,'mon-forms/ECPL-Pod-Father-Monitoring-Form-chat.html', data)


def fameHouseNew(request):

    if request.method == 'POST':
        category='Email/Chat Other'
        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']

        ticket_no=request.POST['ticket_no']
        ticket_type = request.POST['ticket_type']

        trans_date = request.POST['ticketdate']
        audit_date = request.POST['auditdate']

        campaign = request.POST['campaign']

        week = request.POST['week']
        am = request.POST['am']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        try:
            manager_emp_id_obj = Profile.objects.get(emp_name=manager)
            manager_emp_id = manager_emp_id_obj.emp_id

        except Profile.DoesNotExist:
            manager_emp_id = 0

        manager_name = manager

        # Immediate fails:
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])
        compliance_4 = int(request.POST['compliance_4'])
        compliance_5 = int(request.POST['compliance_5'])
        compliance_6 = int(request.POST['compliance_6'])
        compliance_total = compliance_1 + compliance_2 + compliance_3 + compliance_4 + compliance_5 + compliance_6

        na_list = []
        sum_list = []
        def scoreCalc(pk):

            if pk == 'NA':
                na_list.append(pk)
                return pk
            else:
                sum_list.append(int(pk))
                return int(pk)


        # Opening

        opening_1 = scoreCalc(request.POST['opening_1'])
        opening_2 = scoreCalc(request.POST['opening_2'])
        opening_3 = scoreCalc(request.POST['opening_3'])

        #opening_total = opening_1+opening_2+opening_3

        # Customer Issue Resolution

        cir_1 = scoreCalc(request.POST['cir_1'])
        cir_2 = scoreCalc(request.POST['cir_2'])
        cir_3 = scoreCalc(request.POST['cir_3'])
        cir_4 = scoreCalc(request.POST['cir_4'])
        cir_5 = scoreCalc(request.POST['cir_5'])

        #cir_total = cir_1+cir_2+cir_3+cir_4+cir_5

        # Macro Usage
        macro_1 = scoreCalc(request.POST['macro_1'])
        macro_2 = scoreCalc(request.POST['macro_2'])

        #macro_total = macro_1 + macro_2

        # Formatting
        formatting_1 = scoreCalc(request.POST['formatting_1'])
        formatting_2 = scoreCalc(request.POST['formatting_2'])
        formatting_3 = scoreCalc(request.POST['formatting_3'])

       # formatting_total = formatting_1 + formatting_2 + formatting_3

        # Documentation
        doc_1 = scoreCalc(request.POST['doc_1'])
        doc_2 = scoreCalc(request.POST['doc_2'])
        doc_3 = scoreCalc(request.POST['doc_3'])
        doc_4 = scoreCalc(request.POST['doc_4'])

       # doc_total= doc_1 + doc_2 + doc_3 + doc_4

        # Etiquette
        et_1 = scoreCalc(request.POST['et_1'])
        et_2 = scoreCalc(request.POST['et_2'])
        et_3 = scoreCalc(request.POST['et_3'])
        et_4 = scoreCalc(request.POST['et_4'])

       # et_total = et_1 + et_2 + et_3 + et_4

        # Closing
        closing_1 = scoreCalc(request.POST['closing_1'])
        closing_2 = scoreCalc(request.POST['closing_2'])

       # closing_total = closing_1 + closing_2


        fatal_list=[compliance_1,compliance_2,compliance_3,compliance_4,compliance_5,compliance_6]

        fatal_list_count=[]
        for i in fatal_list:
            if i==0:
                fatal_list_count.append(i)
        no_of_fatals=len(fatal_list_count)


        if compliance_1 == 0 or compliance_2 ==0 or compliance_3==0 or compliance_4==0 or compliance_5==0 or compliance_6==0:
            overall_score=0
            fatal=True
        else:
            overall_score= (sum(sum_list)/len(sum_list))*100
            fatal=False

        #################################################

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']

        added_by = request.user.profile.emp_name


        famehouse = FameHouseNewMonForm(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                     manager=manager_name,manager_id=manager_emp_id,am=am,

                                     trans_date=trans_date, audit_date=audit_date,ticket_no=ticket_no,
                                     campaign=campaign,
                                     compliance_1=compliance_1,compliance_2=compliance_2,compliance_3=compliance_3,compliance_4=compliance_4,compliance_5=compliance_5,compliance_6=compliance_6,compliance_total=compliance_total,
                                     opening_1=opening_1,opening_2=opening_2,opening_3=opening_3,
                                     cir_1=cir_1,cir_2=cir_2,cir_3=cir_3,cir_4=cir_4,cir_5=cir_5,
                                     macro_1=macro_1,macro_2=macro_2,
                                     formatting_1=formatting_1,formatting_2=formatting_2,formatting_3=formatting_3,
                                     doc_1=doc_1,doc_2=doc_2,doc_3=doc_3,doc_4=doc_4,
                                     et_1=et_1,et_2=et_2,et_3=et_3,et_4=et_4,
                                     closing_1=closing_1,closing_2=closing_2,

                                     areas_improvement=areas_improvement,
                                     positives=positives, comments=comments,
                                     added_by=added_by,ticket_type=ticket_type,

                                     category=category,overall_score=overall_score,
                                            week=week,fatal=fatal,fatal_count=no_of_fatals
                                     )

        famehouse.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/fame-house-new.html', data)


def flaMonForm(request):
    if request.method == 'POST':
        category='FLA'
        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        order_id=request.POST['order_id']
        trans_date = request.POST['transdate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        service=request.POST['service']
        check_list=request.POST['checklist']

        #######################################
        prof_obj=Profile.objects.get(emp_id=emp_id)
        manager=prof_obj.manager

        manager_emp_id_obj=Profile.objects.get(emp_name=manager)

        manager_emp_id=manager_emp_id_obj.emp_id
        manager_name=manager
        #########################################

        # Macros
        checklist_1 = int(request.POST['checklist_1'])

        reason_for_failure=request.POST['reason_for_failure']
        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        week = request.POST['week']
        am = request.POST['am']

        fla = FLAMonitoringForm(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                     manager=manager_name,manager_id=manager_emp_id,

                                     trans_date=trans_date, audit_date=audit_date,order_id=order_id,
                                     campaign=campaign,concept=concept,service=service,

                                     check_list=check_list,
                                     checklist_1=checklist_1,

                                     reason_for_failure=reason_for_failure,
                                     areas_improvement=areas_improvement,
                                     positives=positives, comments=comments,
                                     added_by=added_by,

                                     overall_score=checklist_1,category=category,
                                week=week,am=am
                                     )
        fla.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/FLA-mon-form.html', data)


def gubaGooNew(request):

    if request.method == 'POST':

        chat1_id = request.POST['chat1_id']
        chat2_id = request.POST['chat2_id']
        chat3_id = request.POST['chat3_id']
        chat4_id = request.POST['chat4_id']
        chat5_id = request.POST['chat5_id']
        chat6_id = request.POST['chat6_id']

        cat1chat1 = request.POST['cat1chat1']
        cat1chat2 = request.POST['cat1chat2']
        cat1chat3 = request.POST['cat1chat3']
        cat1chat4 = request.POST['cat1chat4']
        cat1chat5 = request.POST['cat1chat5']
        cat1chat6 = request.POST['cat1chat6']
        cat1 = [cat1chat1, cat1chat2, cat1chat3, cat1chat4, cat1chat5,cat1chat6]

        cat2chat1 = request.POST['cat2chat1']
        cat2chat2 = request.POST['cat2chat2']
        cat2chat3 = request.POST['cat2chat3']
        cat2chat4 = request.POST['cat2chat4']
        cat2chat5 = request.POST['cat2chat5']
        cat2chat6 = request.POST['cat2chat6']
        cat2 = [cat2chat1, cat2chat2, cat2chat3, cat2chat4, cat2chat5,cat2chat6]

        cat3chat1 = request.POST['cat3chat1']
        cat3chat2 = request.POST['cat3chat2']
        cat3chat3 = request.POST['cat3chat3']
        cat3chat4 = request.POST['cat3chat4']
        cat3chat5 = request.POST['cat3chat5']
        cat3chat6 = request.POST['cat3chat6']
        cat3 = [cat3chat1, cat3chat2, cat3chat3, cat3chat4, cat3chat5,cat3chat6]

        cat4chat1 = request.POST['cat4chat1']
        cat4chat2 = request.POST['cat4chat2']
        cat4chat3 = request.POST['cat4chat3']
        cat4chat4 = request.POST['cat4chat4']
        cat4chat5 = request.POST['cat4chat5']
        cat4chat6 = request.POST['cat4chat6']
        cat4 = [cat4chat1, cat4chat2, cat4chat3, cat4chat4, cat4chat5,cat4chat6]

        cat5chat1 = request.POST['cat5chat1']
        cat5chat2 = request.POST['cat5chat2']
        cat5chat3 = request.POST['cat5chat3']
        cat5chat4 = request.POST['cat5chat4']
        cat5chat5 = request.POST['cat5chat5']
        cat5chat6 = request.POST['cat5chat6']
        cat5 = [cat5chat1, cat5chat2, cat5chat3, cat5chat4, cat5chat5,cat5chat6]

        cat6chat1 = request.POST['cat6chat1']
        cat6chat2 = request.POST['cat6chat2']
        cat6chat3 = request.POST['cat6chat3']
        cat6chat4 = request.POST['cat6chat4']
        cat6chat5 = request.POST['cat6chat5']
        cat6chat6 = request.POST['cat6chat6']
        cat6 = [cat6chat1, cat6chat2, cat6chat3, cat6chat4, cat6chat6]

        cat7chat1 = request.POST['cat7chat1']
        cat7chat2 = request.POST['cat7chat2']
        cat7chat3 = request.POST['cat7chat3']
        cat7chat4 = request.POST['cat7chat4']
        cat7chat5 = request.POST['cat7chat5']
        cat7chat6 = request.POST['cat7chat6']
        cat7 = [cat7chat1, cat7chat2, cat7chat3, cat7chat4, cat7chat5,cat7chat6]

        cat8chat1 = request.POST['cat8chat1']
        cat8chat2 = request.POST['cat8chat2']
        cat8chat3 = request.POST['cat8chat3']
        cat8chat4 = request.POST['cat8chat4']
        cat8chat5 = request.POST['cat8chat5']
        cat8chat6 = request.POST['cat8chat6']
        cat8 = [cat8chat1, cat8chat2, cat8chat3, cat8chat4, cat8chat5,cat8chat6]

        cat9chat1 = request.POST['cat9chat1']
        cat9chat2 = request.POST['cat9chat2']
        cat9chat3 = request.POST['cat9chat3']
        cat9chat4 = request.POST['cat9chat4']
        cat9chat5 = request.POST['cat9chat5']
        cat9chat6 = request.POST['cat9chat6']
        cat9 = [cat9chat1, cat9chat2, cat9chat3, cat9chat4, cat9chat5,cat9chat6]

        cat10chat1 = request.POST['cat10chat1']
        cat10chat2 = request.POST['cat10chat2']
        cat10chat3 = request.POST['cat10chat3']
        cat10chat4 = request.POST['cat10chat4']
        cat10chat5 = request.POST['cat10chat5']
        cat10chat6 = request.POST['cat10chat6']
        cat10 = [cat10chat1, cat10chat2, cat10chat3, cat10chat4, cat10chat5,cat10chat6]

        cat11chat1 = request.POST['cat11chat1']
        cat11chat2 = request.POST['cat11chat2']
        cat11chat3 = request.POST['cat11chat3']
        cat11chat4 = request.POST['cat11chat4']
        cat11chat5 = request.POST['cat11chat5']
        cat11chat6 = request.POST['cat11chat6']
        cat11 = [cat11chat1, cat11chat2, cat11chat3, cat11chat4, cat11chat5,cat11chat6]

        cat12chat1 = request.POST['cat12chat1']
        cat12chat2 = request.POST['cat12chat2']
        cat12chat3 = request.POST['cat12chat3']
        cat12chat4 = request.POST['cat12chat4']
        cat12chat5 = request.POST['cat12chat5']
        cat12chat6 = request.POST['cat12chat6']
        cat12 = [cat12chat1, cat12chat2, cat12chat3, cat12chat4, cat12chat5,cat12chat6]

        cat13chat1 = request.POST['cat13chat1']
        cat13chat2 = request.POST['cat13chat2']
        cat13chat3 = request.POST['cat13chat3']
        cat13chat4 = request.POST['cat13chat4']
        cat13chat5 = request.POST['cat13chat5']
        cat13chat6 = request.POST['cat13chat6']
        cat13 = [cat13chat1, cat13chat2, cat13chat3, cat13chat4, cat13chat5,cat13chat6]

        cat14chat1 = request.POST['cat14chat1']
        cat14chat2 = request.POST['cat14chat2']
        cat14chat3 = request.POST['cat14chat3']
        cat14chat4 = request.POST['cat14chat4']
        cat14chat5 = request.POST['cat14chat5']
        cat14chat6 = request.POST['cat14chat6']
        cat14 = [cat14chat1, cat14chat2, cat14chat3, cat14chat4, cat14chat5,cat14chat6]

        cat15chat1 = request.POST['cat15chat1']
        cat15chat2 = request.POST['cat15chat2']
        cat15chat3 = request.POST['cat15chat3']
        cat15chat4 = request.POST['cat15chat4']
        cat15chat5 = request.POST['cat15chat5']
        cat15chat6 = request.POST['cat15chat6']
        cat15 = [cat15chat1, cat15chat2, cat15chat3, cat15chat4, cat15chat5,cat15chat6]

        cat16chat1 = request.POST['cat16chat1']
        cat16chat2 = request.POST['cat16chat2']
        cat16chat3 = request.POST['cat16chat3']
        cat16chat4 = request.POST['cat16chat4']
        cat16chat5 = request.POST['cat16chat5']
        cat16chat6 = request.POST['cat16chat6']



        def scoreCalc(lst):
            ycount = lst.count('y')
            pcount = lst.count('p')
            fcount = lst.count('n')
            nacount = lst.count('NA')
            cat1score = (ycount + pcount)/5 * 100
            
            if fcount ==3 or fcount ==4 or fcount ==5:
                fscore = 0.025
            elif fcount == 6:
                fscore = 0.05
            elif fcount <=2:
                fscore = 0        
            
            return cat1score,fscore

        def autoFailCalculation(a,b,lst):

            fcount = lst.count('n')
            if fcount == 3 or fcount == 4 or fcount == 5:
                fscore = a
                return fscore
            elif fcount == 6:
                fscore = b
                return fscore
            elif fcount <= 2:
                fscore = 0
                return fscore

        cat1fscore = autoFailCalculation(0.025,0.05,cat1)
        cat2fscore = autoFailCalculation(0.025,0.05,cat2)

        cat3fscore = autoFailCalculation(0.05,0.1,cat3)
        cat4fscore = autoFailCalculation(0.075,0.125,cat4)

        cat5fscore = autoFailCalculation(0.03,0.05,cat5)
        cat6fscore = autoFailCalculation(0.03,0.05,cat6)
        cat7fscore = autoFailCalculation(0.03,0.05,cat7)
        cat8fscore = autoFailCalculation(0.03,0.05,cat8)

        cat9fscore = autoFailCalculation(0.15,0.3,cat9)
        cat10fscore = autoFailCalculation(0.025,0.05,cat10)

        cat11fscore = autoFailCalculation(0.025,0.05,cat11)
        cat13fscore = autoFailCalculation(0.025,0.05,cat13)

        cat14fscore = autoFailCalculation(0.025,0.05,cat14)
        cat15fscore = autoFailCalculation(0.025,0.05,cat15)


        cat1score = scoreCalc(cat1)
        cat2score = scoreCalc(cat2)
        cat3score = scoreCalc(cat3)
        cat4score = scoreCalc(cat4)
        cat5score = scoreCalc(cat5)
        cat6score = scoreCalc(cat6)
        cat7score = scoreCalc(cat7)
        cat8score = scoreCalc(cat8)
        cat9score = scoreCalc(cat9)
        cat10score = scoreCalc(cat10)
        cat11score = scoreCalc(cat11)
        cat12score = scoreCalc(cat12)
        cat13score = scoreCalc(cat13)
        cat14score = scoreCalc(cat14)
        cat15score= scoreCalc(cat15)

        '''print(cat1fscore)
        print(cat2fscore)
        print(cat3fscore)
        print(cat4fscore)
        print(cat5fscore)
        print(cat6fscore)
        print(cat7fscore)
        print(cat8fscore)
        print(cat9fscore)
        print(cat10fscore)
        print(cat11fscore)
        print(cat13fscore)
        print(cat14fscore)
        print(cat15fscore)'''



        total_failing_score = cat1fscore + cat2fscore + cat3fscore + cat4fscore + cat5fscore + cat6fscore + \
                                cat7fscore + cat8fscore + cat9fscore + cat10fscore + \
                                cat11fscore + cat13fscore + \
                                cat14fscore + cat15fscore


        ######### chat 1 calculation  ##############

        total_score = 293
        ####### Greeting ###########################

        def catAndTotalScore(c,tot,score):

            if c == 'y':
                c = score
                tot=tot
                return (c,tot)
            elif c == 'n':
                c = 0
                tot = tot
                return (c,tot)
            elif c == 'p':
                c = 0
                tot = tot-score
                return (c,tot)
            else:
                c = score
                tot = tot
                return (c,tot)

        cat1chat1score, total_score = catAndTotalScore(cat1chat1, total_score, 10)
        cat2chat1score, total_score = catAndTotalScore(cat2chat1, total_score, 10)
        greeting_chat1 = cat1chat1score + cat2chat1score

        cat3chat1score, total_score = catAndTotalScore(cat3chat1, total_score, 40)
        cat4chat1score, total_score = catAndTotalScore(cat4chat1, total_score, 40)
        qn_chat1 = cat3chat1score + cat4chat1score

        cat5chat1score, total_score = catAndTotalScore(cat5chat1, total_score, 15)
        cat6chat1score, total_score = catAndTotalScore(cat6chat1, total_score, 15)
        cat7chat1score, total_score = catAndTotalScore(cat7chat1, total_score, 12)
        cat8chat1score, total_score = catAndTotalScore(cat8chat1, total_score, 12)
        lead_chat1 = cat5chat1score + cat6chat1score + cat7chat1score + cat8chat1score

        cat9chat1score, total_score = catAndTotalScore(cat9chat1, total_score, 40)
        cat10chat1score, total_score = catAndTotalScore(cat10chat1, total_score, 40)
        lf_chat1 = cat9chat1score + cat10chat1score

        cat11chat1score, total_score = catAndTotalScore(cat11chat1, total_score, 15)
        cat12chat1score, total_score = catAndTotalScore(cat12chat1, total_score, 13)
        cat13chat1score, total_score = catAndTotalScore(cat13chat1, total_score, 11)
        timing_chat1 = cat11chat1score+cat12chat1score+cat13chat1score

        cat14chat1score, total_score = catAndTotalScore(cat14chat1, total_score, 10)
        cat15chat1score, total_score = catAndTotalScore(cat15chat1, total_score, 10)
        ce_chat1 = cat14chat1score + cat15chat1score

        if cat16chat1 == 'y':
            autofail_chat1 = (greeting_chat1+qn_chat1+lead_chat1+lf_chat1+timing_chat1+ce_chat1)*(-1)
        else:
            autofail_chat1 = 0

        chat1_total = cat1chat1score+cat2chat1score+cat3chat1score+cat4chat1score+cat5chat1score+cat6chat1score+cat7chat1score+cat8chat1score+cat9chat1score+cat10chat1score+cat11chat1score+cat12chat1score+cat13chat1score+cat14chat1score+cat15chat1score
        chat1_total += autofail_chat1
        chat1_total_score = (chat1_total/total_score)*100
        chat1_total_score = round(chat1_total_score)

        ############################# chat2 ####################################
        total_score = 293

        cat1chat2score, total_score = catAndTotalScore(cat1chat2, total_score, 10)
        cat2chat2score, total_score = catAndTotalScore(cat2chat2, total_score, 10)
        greeting_chat2 = cat1chat2score + cat2chat2score

        cat3chat2score, total_score = catAndTotalScore(cat3chat2, total_score, 40)
        cat4chat2score, total_score = catAndTotalScore(cat4chat2, total_score, 40)
        qn_chat2 = cat3chat2score + cat4chat2score

        cat5chat2score, total_score = catAndTotalScore(cat5chat2, total_score, 15)
        cat6chat2score, total_score = catAndTotalScore(cat6chat2, total_score, 15)
        cat7chat2score, total_score = catAndTotalScore(cat7chat2, total_score, 12)
        cat8chat2score, total_score = catAndTotalScore(cat8chat2, total_score, 12)
        lead_chat2 = cat5chat2score + cat6chat2score + cat7chat2score + cat8chat2score

        cat9chat2score, total_score = catAndTotalScore(cat9chat2, total_score, 40)
        cat10chat2score, total_score = catAndTotalScore(cat10chat2, total_score, 40)
        lf_chat2 = cat9chat2score + cat10chat2score

        cat11chat2score, total_score = catAndTotalScore(cat11chat2, total_score, 15)
        cat12chat2score, total_score = catAndTotalScore(cat12chat2, total_score, 13)
        cat13chat2score, total_score = catAndTotalScore(cat13chat2, total_score, 11)
        timing_chat2 = cat11chat2score + cat12chat2score + cat13chat2score

        cat14chat2score, total_score = catAndTotalScore(cat14chat2, total_score, 10)
        cat15chat2score, total_score = catAndTotalScore(cat15chat2, total_score, 10)
        ce_chat2 = cat14chat2score + cat15chat2score

        if cat16chat2 == 'y':
            autofail_chat2 = (greeting_chat2 + qn_chat2 + lead_chat2 + lf_chat2 + timing_chat2 + ce_chat2) * (-1)
        else:
            autofail_chat2 = 0

        chat2_total = cat1chat2score + cat2chat2score + cat3chat2score + cat4chat2score + cat5chat2score + cat6chat2score + cat7chat2score + cat8chat2score + cat9chat2score + cat10chat2score + cat11chat2score + cat12chat2score + cat13chat2score + cat14chat2score + cat15chat2score
        chat2_total += autofail_chat2
        chat2_total_score = (chat2_total / total_score) * 100
        chat2_total_score = round(chat2_total_score)
        # print(chat2_total_score)

        ############################# chat3 ####################################
        total_score = 293

        cat1chat3score, total_score = catAndTotalScore(cat1chat3, total_score, 10)
        cat2chat3score, total_score = catAndTotalScore(cat2chat3, total_score, 10)
        greeting_chat3 = cat1chat3score + cat2chat3score

        cat3chat3score, total_score = catAndTotalScore(cat3chat3, total_score, 40)
        cat4chat3score, total_score = catAndTotalScore(cat4chat3, total_score, 40)
        qn_chat3 = cat3chat3score + cat4chat3score

        cat5chat3score, total_score = catAndTotalScore(cat5chat3, total_score, 15)
        cat6chat3score, total_score = catAndTotalScore(cat6chat3, total_score, 15)
        cat7chat3score, total_score = catAndTotalScore(cat7chat3, total_score, 12)
        cat8chat3score, total_score = catAndTotalScore(cat8chat3, total_score, 12)
        lead_chat3 = cat5chat3score + cat6chat3score + cat7chat3score + cat8chat3score

        cat9chat3score, total_score = catAndTotalScore(cat9chat3, total_score, 40)
        cat10chat3score, total_score = catAndTotalScore(cat10chat3, total_score, 40)
        lf_chat3 = cat9chat3score + cat10chat3score

        cat11chat3score, total_score = catAndTotalScore(cat11chat3, total_score, 15)
        cat12chat3score, total_score = catAndTotalScore(cat12chat3, total_score, 13)
        cat13chat3score, total_score = catAndTotalScore(cat13chat3, total_score, 11)
        timing_chat3 = cat11chat3score + cat12chat3score + cat13chat3score

        cat14chat3score, total_score = catAndTotalScore(cat14chat3, total_score, 10)
        cat15chat3score, total_score = catAndTotalScore(cat15chat3, total_score, 10)
        ce_chat3 = cat14chat3score + cat15chat3score

        if cat16chat3 == 'y':
            autofail_chat3 = (greeting_chat3 + qn_chat3 + lead_chat3 + lf_chat3 + timing_chat3 + ce_chat3) * (-1)
        else:
            autofail_chat3 = 0

        chat3_total = cat1chat3score + cat2chat3score + cat3chat3score + cat4chat3score + cat5chat3score + cat6chat3score + cat7chat3score + cat8chat3score + cat9chat3score + cat10chat3score + cat11chat3score + cat12chat3score + cat13chat3score + cat14chat3score + cat15chat3score
        chat3_total += autofail_chat3
        chat3_total_score = (chat3_total / total_score) * 100
        chat3_total_score = round(chat3_total_score)
        # print(chat3_total_score)

        ############################# chat4 ####################################
        total_score = 293
        cat1chat4score, total_score = catAndTotalScore(cat1chat4, total_score, 10)
        cat2chat4score, total_score = catAndTotalScore(cat2chat4, total_score, 10)
        greeting_chat4 = cat1chat4score + cat2chat4score

        cat3chat4score, total_score = catAndTotalScore(cat3chat4, total_score, 40)
        cat4chat4score, total_score = catAndTotalScore(cat4chat4, total_score, 40)
        qn_chat4 = cat3chat4score + cat4chat4score

        cat5chat4score, total_score = catAndTotalScore(cat5chat4, total_score, 15)
        cat6chat4score, total_score = catAndTotalScore(cat6chat4, total_score, 15)
        cat7chat4score, total_score = catAndTotalScore(cat7chat4, total_score, 12)
        cat8chat4score, total_score = catAndTotalScore(cat8chat4, total_score, 12)
        lead_chat4 = cat5chat4score + cat6chat4score + cat7chat4score + cat8chat4score

        cat9chat4score, total_score = catAndTotalScore(cat9chat4, total_score, 40)
        cat10chat4score, total_score = catAndTotalScore(cat10chat4, total_score, 40)
        lf_chat4 = cat9chat4score + cat10chat4score

        cat11chat4score, total_score = catAndTotalScore(cat11chat4, total_score, 15)
        cat12chat4score, total_score = catAndTotalScore(cat12chat4, total_score, 13)
        cat13chat4score, total_score = catAndTotalScore(cat13chat4, total_score, 11)
        timing_chat4 = cat11chat4score + cat12chat4score + cat13chat4score

        cat14chat4score, total_score = catAndTotalScore(cat14chat4, total_score, 10)
        cat15chat4score, total_score = catAndTotalScore(cat15chat4, total_score, 10)
        ce_chat4 = cat14chat4score + cat15chat4score

        if cat16chat4 == 'y':
            autofail_chat4 = (greeting_chat4 + qn_chat4 + lead_chat4 + lf_chat4 + timing_chat4 + ce_chat4) * (-1)
        else:
            autofail_chat4 = 0

        chat4_total = cat1chat4score + cat2chat4score + cat3chat4score + cat4chat4score + cat5chat4score + cat6chat4score + cat7chat4score + cat8chat4score + cat9chat4score + cat10chat4score + cat11chat4score + cat12chat4score + cat13chat4score + cat14chat4score + cat15chat4score
        chat4_total += autofail_chat4
        chat4_total_score = (chat4_total / total_score) * 100
        chat4_total_score = round(chat4_total_score)
        # print(chat4_total_score)

        ############################# chat5 ####################################
        total_score = 293
        cat1chat5score, total_score = catAndTotalScore(cat1chat5, total_score, 10)
        cat2chat5score, total_score = catAndTotalScore(cat2chat5, total_score, 10)
        greeting_chat5 = cat1chat5score + cat2chat5score

        cat3chat5score, total_score = catAndTotalScore(cat3chat5, total_score, 40)
        cat4chat5score, total_score = catAndTotalScore(cat4chat5, total_score, 40)
        qn_chat5 = cat3chat5score + cat4chat5score

        cat5chat5score, total_score = catAndTotalScore(cat5chat5, total_score, 15)
        cat6chat5score, total_score = catAndTotalScore(cat6chat5, total_score, 15)
        cat7chat5score, total_score = catAndTotalScore(cat7chat5, total_score, 12)
        cat8chat5score, total_score = catAndTotalScore(cat8chat5, total_score, 12)
        lead_chat5 = cat5chat5score + cat6chat5score + cat7chat5score + cat8chat5score

        cat9chat5score, total_score = catAndTotalScore(cat9chat5, total_score, 40)
        cat10chat5score, total_score = catAndTotalScore(cat10chat5, total_score, 40)
        lf_chat5 = cat9chat5score + cat10chat5score

        cat11chat5score, total_score = catAndTotalScore(cat11chat5, total_score, 15)
        cat12chat5score, total_score = catAndTotalScore(cat12chat5, total_score, 13)
        cat13chat5score, total_score = catAndTotalScore(cat13chat5, total_score, 11)
        timing_chat5 = cat11chat5score + cat12chat5score + cat13chat5score

        cat14chat5score, total_score = catAndTotalScore(cat14chat5, total_score, 10)
        cat15chat5score, total_score = catAndTotalScore(cat15chat5, total_score, 10)
        ce_chat5 = cat14chat5score + cat15chat5score

        if cat16chat5 == 'y':
            autofail_chat5 = (greeting_chat5 + qn_chat5 + lead_chat5 + lf_chat5 + timing_chat5 + ce_chat5) * (-1)
        else:
            autofail_chat5 = 0

        chat5_total = cat1chat5score + cat2chat5score + cat3chat5score + cat4chat5score + cat5chat5score + cat6chat5score + cat7chat5score + cat8chat5score + cat9chat5score + cat10chat5score + cat11chat5score + cat12chat5score + cat13chat5score + cat14chat5score + cat15chat5score
        chat5_total += autofail_chat5
        chat5_total_score = (chat5_total / total_score) * 100
        chat5_total_score = round(chat5_total_score)
        # print(chat5_total_score)

        ############################# chat6 ####################################
        total_score = 293
        cat1chat6score, total_score = catAndTotalScore(cat1chat6, total_score, 10)
        cat2chat6score, total_score = catAndTotalScore(cat2chat6, total_score, 10)
        greeting_chat6 = cat1chat6score + cat2chat6score

        cat3chat6score, total_score = catAndTotalScore(cat3chat6, total_score, 40)
        cat4chat6score, total_score = catAndTotalScore(cat4chat6, total_score, 40)
        qn_chat6 = cat3chat6score + cat4chat6score

        cat5chat6score, total_score = catAndTotalScore(cat5chat6, total_score, 15)
        cat6chat6score, total_score = catAndTotalScore(cat6chat6, total_score, 15)
        cat7chat6score, total_score = catAndTotalScore(cat7chat6, total_score, 12)
        cat8chat6score, total_score = catAndTotalScore(cat8chat6, total_score, 12)
        lead_chat6 = cat5chat6score + cat6chat6score + cat7chat6score + cat8chat6score

        cat9chat6score, total_score = catAndTotalScore(cat9chat6, total_score, 40)
        cat10chat6score, total_score = catAndTotalScore(cat10chat6, total_score, 40)
        lf_chat6 = cat9chat6score + cat10chat6score

        cat11chat6score, total_score = catAndTotalScore(cat11chat6, total_score, 15)
        cat12chat6score, total_score = catAndTotalScore(cat12chat6, total_score, 13)
        cat13chat6score, total_score = catAndTotalScore(cat13chat6, total_score, 11)
        timing_chat6 = cat11chat6score + cat12chat6score + cat13chat6score

        cat14chat6score, total_score = catAndTotalScore(cat14chat6, total_score, 10)
        cat15chat6score, total_score = catAndTotalScore(cat15chat6, total_score, 10)
        ce_chat6 = cat14chat6score + cat15chat6score

        if cat16chat6 == 'y':
            autofail_chat6 = (greeting_chat6 + qn_chat6 + lead_chat6 + lf_chat6 + timing_chat6 + ce_chat6) * (-1)
        else:
            autofail_chat6 = 0

        chat6_total = cat1chat6score + cat2chat6score + cat3chat6score + cat4chat6score + cat5chat6score + cat6chat6score + cat7chat6score + cat8chat6score + cat9chat6score + cat10chat6score + cat11chat6score + cat12chat6score + cat13chat6score + cat14chat6score + cat15chat6score
        chat6_total += autofail_chat6
        chat6_total_score = (chat6_total / total_score) * 100
        chat6_total_score = round(chat6_total_score)
        # print(chat6_total_score)
        # print('----------------------------------------------------------')
        # print('Failing Score',total_failing_score)

        total_chat_sum = chat1_total_score + chat2_total_score + chat3_total_score + \
                           chat4_total_score + chat5_total_score + chat6_total_score 

        total_chat_score = total_chat_sum/6

        # print(total_chat_score,'Total CHat Score')

        total_failing_perc = total_failing_score * 100

        total_audit_score = total_chat_score - total_failing_perc
        total_audit_score = round(total_audit_score)

        # print(total_audit_score,'Total Audit Score')      

        data = {
                'chat1':chat1_total_score,'chat2':chat2_total_score,
                'chat3':chat3_total_score,'chat4':chat4_total_score,
                'chat5':chat5_total_score,'chat6':chat6_total_score,
                'failing':total_failing_perc,
                'overall':total_audit_score,
                'chat1_id':chat1_id,'chat2_id':chat2_id,'chat3_id':chat3_id,
                'chat4_id': chat4_id,'chat5_id':chat5_id,'chat6_id':chat6_id,
        }

        return render(request,'mon-forms/gubagoo-result.html',data)               

############## End Mon Forms ##############################


def processNameChanger(request):

    obj=MonitoringFormLeadsAadhyaSolution.objects.all()
    for i in obj:
        i.process='AAdya'
        i.save()

def desiChanger(request):

    empid_list = [2145,3831]
    for i in empid_list:

        prof = Profile.objects.get(emp_id = i)
        prof.emp_desi = 'QA'
        prof.save()


def addSingleProfile(request):

    emp_id=6728

    manager='Dina'
    profile_object=Profile.objects.get(emp_id=emp_id)
    profile_object.manager=manager
    profile_object.save()




def updateProfile(request):

    if request.method=='POST':
        id = request.POST['id']
        desi = request.POST['desi']

        emp = Profile.objects.get(id=id)

        emp.emp_desi = desi
        #emp.save()

        return render(request, 'update-profile.html',)
    else:
        profiles=Profile.objects.all()
        data={'profiles':profiles}
        return render(request,'update-profile.html',data)


def profileDetailedView(request):
    if request.method == 'POST':
        id = request.POST['id']
        obj = Profile.objects.get(id=id)

        data = {'emp':obj}

        return render(request,'profile-detailed-view.html',data)


def powerBITest(request):

    return render(request,'test-powerbi-view.html')



def addtoUserModel(request):

    empobj=ProfileNewtoAddUserandProfile.objects.all()
    for i in empobj:
        user=User.objects.filter(username=i.username)
        if user.exists():
            print(i.emp_name+' '+'exist')
            pass
        else:
            user = User.objects.create_user(id=i.username,username=i.username,password=i.password)
            profile = Profile(id=i.username,emp_name=i.emp_name,emp_id=i.username,emp_desi=i.emp_desi,team=i.team,email=i.email,team_lead=i.team_lead,manager=i.manager,user_id=i.username,am=i.am,process=i.process)
            profile.save()
            print('User and Profile created')



def checkProfile(request):

    profile=Profile.objects.get(emp_id=6043)
    profile.user=6043
    profile.id=6043
    profile.save()

def changePassword(request):

    u = User.objects.get(username=1458)
    u.set_password('1458testuser1')
    u.save()
    return redirect('/')


def addNewCampaign(request):

    if request.method == 'POST':
        campaign = request.POST['campaign']
        type = request.POST['type']
        c = Campaigns.objects.create(name=campaign,type=type)
        c.save()
        return redirect('/add-new-campaign')

    else:
        return render(request,'add-new-campaign.html')


def deleteData(request):

    pass
    '''for i in list_of_monforms:
        i.objects.all().delete()'''



def campaignDetails(request):

    if request.method == 'POST':
        category = request.POST['campaign']

        for i in list_of_monforms:
            obj = i.objects.all()
            if obj.count() >0:
                if obj[0].process == category:
                    campaign = i
                else:
                    pass
            else:
                pass

        print(campaign)
        campaigns = Campaigns.objects.all()
        data = {'campaigns': campaigns}
        return render(request, 'all-campaigns.html', data)

    else:
        campaigns = Campaigns.objects.all()
        data = {'campaigns':campaigns}
        return render(request,'all-campaigns.html',data)



def AllProfileUpdate(request):

    new = ABCprofile.objects.all()

    prof = Profile.objects.all()

    for i in new:
        for j in prof:
            if j.emp_id == i.emp_id:
                j.manager = i.manager
                j.am = i.am
                j.team_lead = i.tl
                j.save()









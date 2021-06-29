from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django_pivot.pivot import pivot
from django.core.mail import send_mail
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

                        # Inbound
                        MasterMonitoringFormTonnCoaInboundCalls,SomethingsBrewingInbound,PrinterPixMasterMonitoringFormInboundCalls,
                        NuclusInboundCalls,NaffaInnovationsInboundCalls,KappimachineInboundCalls,HealthyplusInboundMonForm,
                        FinesseMortgageInboundMonForm,DigitalSwissGoldInboundMonForm,DanielwellingtoInboundMonForm,BhagyaLakshmiInboundMonForm,
                        AKDYInboundMonFormNew,AdityaBirlainboundMonForm,ABHindalcoInboundMonForm,

                        # Email/CHat
                        SuperPlayMonForm,DanielWellinChatEmailMonForm,TerraceoChatEmailMonForm,TonnChatsEmailNewMonForm,
                        PrinterPixMasterMonitoringFormChatsEmail,PractoMonForm,FurBabyMonForm,AKDYEmailMonForm,AmerisaveEmailMonForm,
                        ClearViewEmailMonForm,FinesseMortgageEmailMonForm,DigitalSwissGoldEmailChatMonForm,

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

        ############################





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

        associate_data = []
        associate_data_fatal = []
        associate_data_errors = []

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
        open_obj = monforms.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,
                                          associate_name=agent_name, status=False, disput_status=False).order_by(
            '-audit_date')
        disp_obj = monforms.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,
                                           associate_name=agent_name, disput_status=True).order_by('-audit_date')

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

    ################ Others ##########################################################

    if process_name == 'Fame House':
        coaching = FameHouseNewMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-fame-house-new.html', data)

    if process_name == 'Noom-EVA':
        coaching = ChatMonitoringFormEva.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-eva-chat.html', data)

    if process_name == 'Noom-POD':
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

    ################ Others ##########################################################

    if process_name == 'Fame House':
        coaching = FameHouseNewMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-fame-house-new.html', data)

    if process_name == 'Noom-EVA':
        coaching = ChatMonitoringFormEva.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-eva-chat.html', data)

    if process_name == 'Noom-POD':
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

        list_of_monforms = [

                        ]


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
        manager_mail=Profile.objects.get(emp_name=manager_name)
        manager_email=manager_mail.email
        cid = pk
        process = request.POST['campaign']

        # Email Contents
        subject_of_email='Coaching dispute of -'+emp_name
        body_of_email = 'Hello ,'+ '\n' + 'The QA socre for the following call is being disputed by '+' - '+emp_name +'\n for the following reasons -- >\n' + emp_comments +'\n -- Request you to follow up on this with the concerned as the coaching will remain OPEN until resolved, and will not reflect in the QA Scorecard.'

        def sendEmail(email):

            send_mail(subject_of_email, #Subject
                      body_of_email,#Body
                      'qms@expertcallers.com',# From
                      ['kalesh.cv@expertcallers.com','kaleshcv2@gmail.com'],# To
                      fail_silently=False)

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
        sendEmail(manager_email)
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
            x = i.objects.filter(added_by=qa_name)
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
            x = i.objects.filter(added_by=qa_name)
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
            return render(request, 'mon-forms/new-series-Inbound.html', data)

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

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################

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
        pass
    else:
        profiles=Profile.objects.all()
        data={'profiles':profiles}
        return render(request,'update-profile.html',data)


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

    for i in list_of_monforms:
        i.objects.all().delete()

        
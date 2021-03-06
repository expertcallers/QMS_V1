from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
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
from django.db.models import Count, Avg, Sum
import xlwt
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from . import forms
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q

list_of_monforms = [  # OutBound
    MonitoringFormLeadsAadhyaSolution, AccutimeMonForm, MonitoringFormLeadsAdvanceConsultants,
    MonitoringFormLeadsAllenConsulting, CamIndustrialMonForm, CitizenCapitalMonForm, MonitoringFormLeadsCitySecurity,
    MonitoringFormLeadsCTS, EmbassyLuxuryMonForm, MonitoringFormLeadsGetARates, GlydeAppMonForm, GoldenEastMonForm,
    IbizMonForm,
    IIBMonForm, MonitoringFormLeadsInfothinkLLC, MonitoringFormLeadsInsalvage, JJStudioMonForm, KalkiFashions,
    MonitoringFormLeadsLouisville,
    MonitoringFormLeadsMedicare, MicroDistributingMonForm, MillenniumScientificMonForm, MTCosmeticsMonForm,
    NavigatorBioMonForm, OptimalStudentLoanMonForm,
    ProtostarMonForm, MonitoringFormLeadsPSECU, QBIQMonForm, RestaurentSolMonForm, RitBrainMonForm,
    RoofWellMonForm, ScalaMonForm, SolarCampaignMonForm, StandSpotMonForm, MonitoringFormLeadsSystem4,
    MonitoringFormLeadsTentamusFood, MonitoringFormLeadsTentamusPet,
    TerraceoLeadMonForm, UpfrontOnlineLLCMonform, WTUMonForm, YesHealthMolinaMonForm, ZeroStressMarketingMonForm,
    ABHindalcoOutboundMonForm, AdityaBirlaOutboundMonForm, AmerisaveoutboundMonForm, BhagyaLakshmiOutbound,
    ClearViewOutboundMonForm, DanielWellingtonOutboundMonForm, DigitalSwissGoldOutboundMonForm,
    HealthyplusOutboundMonForm,
    MaxwellPropertiesOutboundMonForm, MovementofInsuranceOutboundMonForm, SterlingStrategiesOutboundMonForm,
    TonnCoaOutboundMonForm, WitDigitalOutboundMonForm,
    PosTechOutboundMonForm, SchindlerMediaOutboundMonForm, UPSOutboundMonForm,
    PickPackDeliveriesMonForm, MarceloPerezMonForm, MedTechGroupOutboundMonForm, DigitalSignageOutboundMonForm,
    HiveIncubatorsOutboundMonForm, KaapiMachinesOutboundMonForm, SomethingsBrewingOutboundMonForm, NaffaOutboundMonForm,
    JBNOutboundMonForm,
    QuickAutoPartsOutboundMonForm,
    ApexCommunicationsOutboundMonForm, LawOfficesOutboundMonForm, WokeUpEnergyOutboundMonForm,
    FinnesseMortgageOutboundMonForm,
    UnitedMortgageOutboundMonForm, CleanLivingHealthWellnessOutboundMonForm, PractoOutboundMonForm,
    ImaginariumOutboundMonForm,
    USJacleanOutboundForm, GlobalGalaxyOutboundForm, CommunityHealthProjectIncOutbound, EducatedAnalyticsLLCOutbound,
    NewDimensionPharmacyOutbound, StayNChargeOutbound,
    JHEnergyConsultantOutbound, MDRGroupLLCOutbound, CoreySmallInsuranceAgencyOutbound, EduvocateOutbound,
    CrossTowerOutbound,
    DawnFinancialOutbound, XportDigitalOutbound,
    AllCarePhysicalTherapyMonform, ExecutiveCapitalResourcesmonform, CalistaOutboundMonForm,
    BrightWayOutboundmonform, BuildinglabLLCOutboundmonform,
    GlobalPharmaOutboundmonform, ThirdWaveOutboundmonform,
    HardHatTechnologiesOutboundmonform, RedefinePlasticsOutboundmonform,
    SapphireMedicalsOutboundMonForm,
    K7Outboundmonform, GlobalArkOutboundMonform, TrialMappingOutboundmonform,
    EduClassOutboundmonform, CredAvenueOutboundmonform, TKAWDIWOutboundmonform,
    DreamPickOutboundmonform, KheloyarOutboundmonform, MaxTradingOutboundmonform,
    ESRTechTalentOutboundmonform, GreenConnectOutboundmonform,
    CentralMortgageFundingOutboundmonform, RapidMortgageOutboundmonform, LinenFinderOutboundmonform,
    BridanAssociatesOutboundmonform, BetterEdOutboundmonform, Com98Outboundmonform,
    GretnaMedicalCentreOutboundmonform, AristaMDOutboundmonform,
    RobertDamonProductionOutboundmonform, VenwizOutboundmonform, CityHabitatOutboundmonform,
    OptelOutboundmonform, SouthCountyOutboundMonForm, InpressOutboundMonForm, LMEnterprisesOutboundMonForm,
    TowersTradersGroupOutboundMonForm, JobERoofingOutboundMonForm, TravelWholesaleOutboundMonForm,

    # Inbound
    MasterMonitoringFormTonnCoaInboundCalls, SomethingsBrewingInbound, PrinterPixMasterMonitoringFormInboundCalls,
    NuclusInboundCalls, NaffaInnovationsInboundCalls, KappimachineInboundCalls, HealthyplusInboundMonForm,
    FinesseMortgageInboundMonForm, DigitalSwissGoldInboundMonForm, DanielwellingtoInboundMonForm,
    BhagyaLakshmiInboundMonForm,
    AKDYInboundMonFormNew, AdityaBirlainboundMonForm, ABHindalcoInboundMonForm,
    RainbowDiagnosticsInboundMonForm, DecentralizedVisionLTDInboundMonForm,
    AmerisaveInboundMonForm, IEDHHInboundMonForm, ClearViewInboundMonForms, QuickAutoPartsInboundMonForms,
    LJHubInboundMonForms,
    ObtheraIncInboundMonForms,
    EduvocateInboundMonForms, CrossTowerInboundMonForms,
    SanaLifeScienceInbound, MonitoringFormMobile22InboundCalls, XportDigitalInboundMonForm, CalistaInboundMonForm,
    ThirdWaveInboundMonForm, HardHatTechnologiesInboundMonForm, GretnaMedicalCenterInboundMonForm,
    BetterEdInboundMonForm, Com98InboundMonForm, OpenWindsInboundMonForm,
    EmbassyLuxuryInboundMonForm, SouthCountyInboundMonForm, CityHabitatInboundMonForm,

    # Email/CHat
    SuperPlayMonForm, DanielWellinChatEmailMonForm, TerraceoChatEmailMonForm, TonnChatsEmailNewMonForm,
    PrinterPixMasterMonitoringFormChatsEmail, FurBabyMonForm, AKDYEmailMonForm, AmerisaveEmailMonForm,
    ClearViewEmailMonForm, FinesseMortgageEmailMonForm, DigitalSwissGoldEmailChatMonForm,
    RainbowDiagnosticsEmailMonForm, HiveIncubatorEmailMonForm, MedTechGroupEmailMonForm,
    Ri8BrainEmailMonForm, ScalaEmailMonForm, KalkiFashionEmailMonForm, MaxwellEmailMonForm,
    TanaorJewelryEmailMonForm, DecentralizedVisionEmailChatMonForm,
    USJacleanEmailChatForm,
    CrossTowerEmailChatForm, SanaLifeScienceEmailChatForm, SapphireMedicalsChatMonForm,
    GretnaMedicalCenterEmailChatForm, JumpRydesEmailChatForm, NaffaInnovationEmailChatForm,
    InpressEmailChatForm,


    MovementInsuranceMonForm,


    # FLA
    FLAMonitoringForm,

    # Noom
    ChatMonitoringFormEva, ChatMonitoringFormPodFather,

    # FameHouse
    FameHouseNewMonForm,
    # Practo
    PractoNewVersion,
    # Practo WIth Sub Category
    PractoWithSubCategory, NewPractoWithSubCategory,
    # Gubagoo
    GubagooAuditForm,
    # ILM
    ILMakiageEmailChatForm,
    # wino
    WinopolyOutbound,
    # ABH
    ABHindalcoMonForm,

    # blazhog
    BlazingHogEmailChatmonform,
    # Nerotel Inbound
    NerotelInboundmonform,
    # Spoiled Child Email/Chat
    SpoiledChildChatmonform,

    # Amerisave
    AmerisaveMonForm,

    BrightwayMonForm,


]


# Index
def index(request):
    # Profile.objects.get(emp_id=)
    return render(request, 'index.html')


# Okay

# Guidelines
def outboundGuidelines(request):
    return render(request, 'guidelines/outbound.html')


def inboundGuidelines(request):
    return render(request, 'guidelines/inbound.html')


def chatGuidelines(request):
    return render(request, 'guidelines/chat.html')


def emailGuidelines(request):
    return render(request, 'guidelines/email.html')


# Okay

# Reistration, Sign up, Login, Logout, Change Password

def signup(request):
    team_leaders = Profile.objects.filter(emp_desi='Team Leader')
    managers = Profile.objects.filter(emp_desi='Manager')
    ams = Profile.objects.filter(emp_desi='AM')

    if request.method == 'POST':
        admin_id = request.POST['admin-id']
        admin_pwd = request.POST['admin-pwd']

        form = UserCreationForm(request.POST)  # form to create user
        profile_form = forms.ProfileCreation(request.POST, request.FILES)

        if form.is_valid() and profile_form.is_valid():
            # Admin ID PWD validation
            if admin_id == 'ecpl-qms' and admin_pwd == '3cplQm52021#':

                manager = request.POST['manager']
                team_lead = request.POST['team-leader']
                am = request.POST['am']
                user = form.save()
                profile = profile_form.save(commit=False)

                profile.user = user
                profile.manager = manager
                profile.team_lead = team_lead
                profile.am = am

                profile.save()
                # login(request,user)
                return render(request, 'index.html')
            else:
                messages.info(request, 'Invalid Admin Credentials !')
                return render(request, 'sign-up.html', {'form': form, 'profile_form': profile_form})
    else:
        form = UserCreationForm()
        profile_form = forms.ProfileCreation()

    return render(request, 'sign-up.html', {'form': form, 'profile_form': profile_form,
                                            'team_leaders': team_leaders, 'managers': managers, 'ams': ams
                                            })


# Okay

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)  # Login form
        if form.is_valid():

            # login the user
            user = form.get_user()
            login(request, user)

            # redirecting
            if user.profile.emp_desi == 'QA':
                return redirect('/employees/qahome')
            elif user.profile.emp_desi == 'Manager' or user.profile.emp_desi == 'AM' or user.profile.emp_desi == 'Trainer' or user.profile.emp_id == 224 or user.profile.emp_id == 6479 or user.profile.emp_desi == 'Team Leader':
                return redirect('/employees/manager-home')
            # Special Access ##########
            elif user.profile.emp_id == 3495 or user.profile.emp_id == 2922:
                return redirect('/employees/manager-home')
            elif user.profile.emp_desi == 'CRO' or user.profile.emp_desi == 'Patrolling officer':
                return redirect('/employees/agenthome')
            else:
                form = AuthenticationForm()
                messages.info(request, 'Please Contact Admin !')
                return render(request, 'login.html', {'form': form})

        else:
            form = AuthenticationForm()
            messages.info(request, 'Invalid Credentials !')
            return render(request, 'login.html', {'form': form})
    else:
        logout(request)
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


# Okay
def logout_view(request):
    logout(request)
    return redirect('/employees/login')


# Okay

# Password Reset

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            logout(request)
            return render(request, 'login.html')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})


def updateEmailAddress(request, pk):
    if request.method == 'POST':
        emp_id = pk
        email_1 = request.POST['email1']
        email_2 = request.POST['email2']
        if email_1 == email_2:
            profile_obj = Profile.objects.get(emp_id=emp_id)
            profile_obj.email = email_2
            profile_obj.save()
            messages.success(request, 'Email Address Updated Successfully ! Please login back')
            return redirect('/logout')
        else:
            messages.error(request, 'Email Address Mismatching')
            return render(request, 'update-email.html')
    else:
        return render(request, 'update-email.html')


# Done


def employeeWiseReport(request):
    if request.method == 'POST':

        currentMonth = request.POST['month']
        currentYear = request.POST['year']
        emp_id = request.POST['emp_id']
        profile = Profile.objects.get(emp_id=emp_id)
        # Mon Form List
        associate_data = []
        associate_data_fatal = []
        associate_data_errors = []

        #### Avg Score Overall ####

        avgs = []

        def avgScoreTotal(monform):
            avg_score_all = monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,
                                                   emp_id=emp_id).aggregate(davg=Avg('overall_score'))
            if avg_score_all['davg'] != None:
                avgs.append(avg_score_all['davg'])

        for i in list_of_monforms:
            avgScoreTotal(i)
        if len(avgs) > 0:
            total_score = sum(avgs) / len(avgs)
        else:
            total_score = 100
        avg_score = round(total_score, 2)

        # Score in All forms
        for i in list_of_monforms:
            coaching = i.objects.filter(emp_id=emp_id, audit_date__year=currentYear,
                                        audit_date__month=currentMonth)
            if coaching.count() > 0:
                emp_wise = i.objects.filter(emp_id=emp_id, audit_date__year=currentYear,
                                            audit_date__month=currentMonth).values(
                    'process').annotate(dcount=Count('associate_name')).annotate(
                    davg=Avg('overall_score'))
                emp_wise_fatal = i.objects.filter(emp_id=emp_id, audit_date__year=currentYear,
                                                  audit_date__month=currentMonth, fatal=True).values(
                    'process').annotate(dsum=Sum('fatal_count'))

                emp_wise_errors = i.objects.filter(emp_id=emp_id, audit_date__year=currentYear,
                                                   audit_date__month=currentMonth, overall_score__lt=100).values(
                    'process').annotate(dcount=Count('process'))

                associate_data.append(emp_wise)
                associate_data_fatal.append(emp_wise_fatal)
                associate_data_errors.append(emp_wise_errors)

        data = {'profile': profile, 'associate_data': associate_data,
                'associate_data_fatal': associate_data_fatal,
                'associate_data_errors': associate_data_errors,
                'avg_score': avg_score,
                }

        return render(request, 'employee-wise-report.html', data)


def managerWiseReport(request):
    if request.method == 'POST':

        currentMonth = request.POST['month']
        currentYear = request.POST['year']
        manager_emp_id = request.POST['emp_id']
        profile = Profile.objects.get(emp_id=manager_emp_id)
        manager_name = profile.emp_name
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

        return render(request, 'manager-wise-report.html', data)


def qualityDashboardMgt(request):
    from django.db.models import Avg
    campaigns = Campaigns.objects.all()
    import datetime
    employees = Profile.objects.exclude(emp_desi__in=['AM', 'Manager', 'Team Leader', 'Trainer', 'QA']).order_by(
        'emp_name')
    managers = Profile.objects.filter(emp_desi='Manager')
    ams = Profile.objects.filter(emp_desi='AM')
    tls = Profile.objects.filter(emp_desi='Team Leader')
    qas = Profile.objects.filter(emp_desi='QA')

    teams = Team.objects.all()

    # Date Time
    if request.method == 'POST':

        month = request.POST['month']
        year = request.POST['year']

        outbound_avg_list = []
        inbound_avg_list = []
        email_chat_avg_list = []

        camp_wise_tot = []
        for i in list_of_monforms:
            camp_wise_total = i.objects.filter(audit_date__year=year, audit_date__month=month).values(
                'process').annotate(dcount=Count('process')).annotate(davg=Avg('overall_score'))
            camp_wise_tot.append(camp_wise_total)

            outbound_score = i.objects.filter(type='Outbound', audit_date__year=year,
                                              audit_date__month=month).aggregate(davg=Avg('overall_score'))
            if outbound_score['davg']:
                outbound_avg_list.append(outbound_score['davg'])

            inbound_score = i.objects.filter(type='Inbound', audit_date__year=year, audit_date__month=month).aggregate(
                davg=Avg('overall_score'))
            if inbound_score['davg']:
                inbound_avg_list.append(inbound_score['davg'])

            email_chat_score = i.objects.filter(type='Email - Chat', audit_date__year=year,
                                                audit_date__month=month).aggregate(davg=Avg('overall_score'))
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
                'ams': ams,
                'tls': tls,
                'qas': qas,
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

            outbound_score = i.objects.filter(type='Outbound', audit_date__year=year,
                                              audit_date__month=month).aggregate(davg=Avg('overall_score'))
            if outbound_score['davg']:
                outbound_avg_list.append(outbound_score['davg'])

            inbound_score = i.objects.filter(type='Inbound', audit_date__year=year, audit_date__month=month).aggregate(
                davg=Avg('overall_score'))
            if inbound_score['davg']:
                inbound_avg_list.append(inbound_score['davg'])

            email_chat_score = i.objects.filter(type='Email - Chat', audit_date__year=year,
                                                audit_date__month=month).aggregate(davg=Avg('overall_score'))
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
                'ams': ams,
                'tls': tls,
                'qas': qas,
                }

        return render(request, 'quality-dashboard-management.html', data)


def agenthome(request):
    agent_name = request.user.profile.emp_name
    emp_id = request.user.profile.emp_id
    team = request.user.profile.process
    currentMonth = datetime.now().month
    currentYear = datetime.now().year

    #### Avg Score Overall ####

    avgs = []

    def avgScoreTotal(monform):
        avg_score_all = monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,
                                               emp_id=emp_id).aggregate(davg=Avg('overall_score'))
        if avg_score_all['davg'] != None:
            avgs.append(avg_score_all['davg'])

    for i in list_of_monforms:
        avgScoreTotal(i)

    if len(avgs) > 0:
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
                                    emp_id=emp_id).values('process').annotate(davg=Avg('overall_score'))
        camp_wise_count = i.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,
                                           emp_id=emp_id, overall_score__lt=100).values('process').annotate(
            dcount=Count('associate_name')).annotate(dfcount=Sum('fatal_count'))
        avg_campaignwise.append(emp_wise)
        campaign_wise_count.append(camp_wise_count)

    #######################################

    all_coaching_list = []
    open_coaching_list = []
    disput_list = []

    def openCampaigns(monforms):
        all_obj = monforms.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,
                                          emp_id=emp_id).order_by('-audit_date')
        open_obj = monforms.objects.filter(emp_id=emp_id, status=False, disput_status=False).order_by(
            '-audit_date')
        disp_obj = monforms.objects.filter(emp_id=emp_id, disput_status=True).order_by('-audit_date')

        all_coaching_list.append(all_obj)
        open_coaching_list.append(open_obj)

        disput_list.append(disp_obj)

    for i in list_of_monforms:
        openCampaigns(i)

    list_of_open_count = []
    list_of_all_count = []
    for i in list_of_monforms:
        count = i.objects.filter(emp_id=emp_id, audit_date__year=currentYear,
                                 audit_date__month=currentMonth, status=False).count()
        count_all = i.objects.filter(emp_id=emp_id, audit_date__year=currentYear,
                                     audit_date__month=currentMonth).count()
        list_of_open_count.append(count)
        list_of_all_count.append(count_all)

    total_open_coachings = sum(list_of_open_count)
    total_coachings = sum(list_of_all_count)

    data = {'all_coachings': all_coaching_list,
            'open_coaching': open_coaching_list,
            'disput_coaching': disput_list,
            'total_open': total_open_coachings,
            'total_coachings': total_coachings,
            'team': team,
            'overall_score': avg_score,
            'avg_campaignwise': avg_campaignwise,
            'camp_wise_count': campaign_wise_count,
            }

    return render(request, 'agent-home.html', data)


def coachingViewAgents(request, process, pk):
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

    elif process_name == 'Clean-Living Health and Wellness':
        coaching = CleanLivingHealthWellnessOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Practo Outbound':
        coaching = PractoOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Imaginarium Outbound':
        coaching = ImaginariumOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'US Jaclean Outbound':
        coaching = USJacleanOutboundForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Global Galaxy Outbound':
        coaching = GlobalGalaxyOutboundForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Community Health Project Inc':
        coaching = CommunityHealthProjectIncOutbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Educated Analytics LLC':
        coaching = EducatedAnalyticsLLCOutbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'New Dimension Pharmacy':
        coaching = NewDimensionPharmacyOutbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Stay-N-Charge':
        coaching = StayNChargeOutbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'J & H Energy Consultant':
        coaching = JHEnergyConsultantOutbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'MDR Group LLC':
        coaching = MDRGroupLLCOutbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Corey Small Insurance Agency Inc':
        coaching = CoreySmallInsuranceAgencyOutbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Eduvocate Outbound':
        coaching = EduvocateOutbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Cross Tower Outbound':
        coaching = CrossTowerOutbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Dawn Financial Outbound':
        coaching = DawnFinancialOutbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Xport Digital Outbound':
        coaching = XportDigitalOutbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Calista Outbound':
        coaching = CalistaOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Global Ark Outbound':
        coaching = GlobalArkOutboundMonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'DI Develop Outbound':
        coaching = DIDevelopOutbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Freehold Outbound':
        coaching = FreeholdOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Zeamo Outbound':
        coaching = ZeamoOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Sapphire Medicals Outbound':
        coaching = SapphireMedicalsOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Eehhaaa Outbound':
        coaching = EehhaaaOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'All Care Physical Therapy':
        coaching = AllCarePhysicalTherapyMonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Executive Capital Resources':
        coaching = ExecutiveCapitalResourcesmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Bright Way Outbound':
        coaching = BrightWayOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Building lab LLC Outbound':
        coaching = BuildinglabLLCOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Global Pharma Outbound':
        coaching = GlobalPharmaOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    # New Added
    elif process_name == 'Redefine Plastics Outbound':
        coaching = RedefinePlasticsOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Hard Hat Technologies Outbound':
        coaching = HardHatTechnologiesOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == '3rd Wave Outbound':
        coaching = ThirdWaveOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'K7 Outbound':
        coaching = K7Outboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Trial Mapping Outbound':
        coaching = TrialMappingOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Edu Class Outbound':
        coaching = EduClassOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Cred Avenue Outbound':
        coaching = CredAvenueOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'TKAWDIW Outbound':
        coaching = TKAWDIWOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Dream Pick Outbound':
        coaching = DreamPickOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Kheloyar Outbound':
        coaching = KheloyarOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Mex Trading Outbound':
        coaching = MaxTradingOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'ESR TechTalent Outbound':
        coaching = ESRTechTalentOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Green Connect Outbound':
        coaching = GreenConnectOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Central Mortgage Funding':
        coaching = CentralMortgageFundingOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Rapid Mortgage':
        coaching = RapidMortgageOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Bridan & Associates Outbound':
        coaching = BridanAssociatesOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Linen Finder Outbound':
        coaching = LinenFinderOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Better Ed Outbound':
        coaching = BetterEdOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Com 98 Outbound':
        coaching = Com98Outboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Gretna Medical Centre Outbound':
        coaching = GretnaMedicalCentreOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Arista MD Outbound':
        coaching = AristaMDOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Robert Damon Production Outbound':
        coaching = RobertDamonProductionOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Venwiz Outbound':
        coaching = VenwizOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'City Habitat Outbound':
        coaching = CityHabitatOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Optel Outbound':
        coaching = OptelOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'South County Outbound':
        coaching = SouthCountyOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Inpress Outbound':
        coaching = InpressOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'L & M Enterprises Outbound':
        coaching = LMEnterprisesOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Towers Traders Group Outbound':
        coaching = TowersTradersGroupOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Job E Roofing Outbound':
        coaching = JobERoofingOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-new-series.html', data)

    elif process_name == 'Travel Wholesale Outbound':
        coaching = TravelWholesaleOutboundMonForm.objects.get(id=pk)
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

    elif process_name == 'LJ Hub Inbound':
        coaching = LJHubInboundMonForms.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Obthera Inc':
        coaching = ObtheraIncInboundMonForms.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Eduvocate Inbound':
        coaching = EduvocateInboundMonForms.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Cross Tower Inbound':
        coaching = CrossTowerInboundMonForms.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Sana Life Science Inbound':
        coaching = SanaLifeScienceInbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Mobile 22 Inbound':
        coaching = MonitoringFormMobile22InboundCalls.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Xport Digital Inbound':
        coaching = XportDigitalInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Calista Inbound':
        coaching = CalistaInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Global Ark Inbound':
        coaching = GlobalArkInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    # New Added
    elif process_name == 'Hard Hat Technologies Inbound':
        coaching = HardHatTechnologiesInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == '3rd Wave Inbound':
        coaching = ThirdWaveInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Gretna Medical Center Inbound':
        coaching = GretnaMedicalCenterInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Better Ed Inbound':
        coaching = BetterEdInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Com 98 Inbound':
        coaching = Com98InboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Open Winds Inbound':
        coaching = OpenWindsInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'Embassy Luxury Inbound':
        coaching = EmbassyLuxuryInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'South County Inbound':
        coaching = SouthCountyInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-inbound-common.html', data)

    elif process_name == 'City Habitat Inbound':
        coaching = CityHabitatInboundMonForm.objects.get(id=pk)
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


    elif process_name == 'Finesse Mortgage Email':
        coaching = FinesseMortgageEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    elif process_name == 'Fur Baby':
        coaching = FurBabyMonForm.objects.get(id=pk)
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

    elif process_name == 'US Jaclean Email Chat':
        coaching = USJacleanEmailChatForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    elif process_name == 'Cross Tower Email-Chat':
        coaching = CrossTowerEmailChatForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    elif process_name == 'Sana Life Science Email-Chat':
        coaching = SanaLifeScienceEmailChatForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    elif process_name == 'Bhagyalaxmi Chat':
        coaching = BhagyalaxmiChatMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    elif process_name == 'Sapphire Medicals Chat':
        coaching = SapphireMedicalsChatMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    elif process_name == 'Gretna Medical Center Email':
        coaching = GretnaMedicalCenterEmailChatForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    elif process_name == 'Jump Rydes Email - Chat':
        coaching = JumpRydesEmailChatForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    elif process_name == 'Naffa Innovation Email - Chat':
        coaching = NaffaInnovationEmailChatForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-email-chat.html', data)

    elif process_name == 'Inpress Email - Chat':
        coaching = InpressEmailChatForm.objects.get(id=pk)
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

    if process_name == 'Practo':
        coaching = PractoNewVersion.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-practo-chat.html', data)

    if process_name == 'Gubagoo':
        coaching = GubagooAuditForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-gubagoo.html', data)

    if process_name == 'IL Makiage':
        coaching = ILMakiageEmailChatForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-ILM.html', data)

    if process_name == 'Digital Swiss Gold Email - Chat':
        coaching = DigitalSwissGoldEmailChatMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-dsg-email-chat.html', data)

    if process_name == 'Winopoly Outbound':
        coaching = WinopolyOutbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-winopoly.html', data)

    if process_name == 'AB Hindalco':
        coaching = ABHindalcoMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-abh.html', data)

    if process_name == 'Blazing Hog':
        coaching = BlazingHogEmailChatmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-blazing.html', data)

    if process_name == 'Practo Chat':
        coaching = NewPractoWithSubCategory.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-practo-chat.html', data)

    if process_name == 'Nerotel Inbound':
        coaching = NerotelInboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-nerotel.html', data)

    if process_name == 'Spoiled Child':
        coaching = SpoiledChildChatmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-spoiled-child.html', data)

    if process_name == 'Amerisave':
        coaching = AmerisaveMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-spoiled-child.html', data)

    if process_name == 'Movement Insurance':
        coaching = MovementInsuranceMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-movement_insurance.html', data)

    if process_name == 'Brightway':
        coaching = BrightwayMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-brightway.html', data)

    else:
        pass


def coachingViewQaDetailed(request, process, pk):
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

    elif process_name == 'Clean-Living Health and Wellness':
        coaching = CleanLivingHealthWellnessOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Practo Outbound':
        coaching = PractoOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Imaginarium Outbound':
        coaching = ImaginariumOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'US Jaclean Outbound':
        coaching = USJacleanOutboundForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Global Galaxy Outbound':
        coaching = GlobalGalaxyOutboundForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Community Health Project Inc':
        coaching = CommunityHealthProjectIncOutbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Educated Analytics LLC':
        coaching = EducatedAnalyticsLLCOutbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'New Dimension Pharmacy':
        coaching = NewDimensionPharmacyOutbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Stay-N-Charge':
        coaching = StayNChargeOutbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'J & H Energy Consultant':
        coaching = JHEnergyConsultantOutbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'MDR Group LLC':
        coaching = MDRGroupLLCOutbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Corey Small Insurance Agency Inc':
        coaching = CoreySmallInsuranceAgencyOutbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Eduvocate Outbound':
        coaching = EduvocateOutbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Cross Tower Outbound':
        coaching = CrossTowerOutbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Dawn Financial Outbound':
        coaching = DawnFinancialOutbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Xport Digital Outbound':
        coaching = XportDigitalOutbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Calista Outbound':
        coaching = CalistaOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Global Ark Outbound':
        coaching = GlobalArkOutboundMonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'DI Develop Outbound':
        coaching = DIDevelopOutbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Freehold Outbound':
        coaching = FreeholdOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Zeamo Outbound':
        coaching = ZeamoOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Sapphire Medicals Outbound':
        coaching = SapphireMedicalsOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Eehhaaa Outbound':
        coaching = EehhaaaOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'All Care Physical Therapy':
        coaching = AllCarePhysicalTherapyMonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Executive Capital Resources':
        coaching = ExecutiveCapitalResourcesmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Bright Way Outbound':
        coaching = BrightWayOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Building lab LLC Outbound':
        coaching = BuildinglabLLCOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Global Pharma Outbound':
        coaching = GlobalPharmaOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    # New Added
    elif process_name == 'Redefine Plastics Outbound':
        coaching = RedefinePlasticsOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Hard Hat Technologies Outbound':
        coaching = HardHatTechnologiesOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == '3rd Wave Outbound':
        coaching = ThirdWaveOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'K7 Outbound':
        coaching = K7Outboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Trial Mapping Outbound':
        coaching = TrialMappingOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Edu Class Outbound':
        coaching = EduClassOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Cred Avenue Outbound':
        coaching = CredAvenueOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'TKAWDIW Outbound':
        coaching = TKAWDIWOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Dream Pick Outbound':
        coaching = DreamPickOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Kheloyar Outbound':
        coaching = KheloyarOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Mex Trading Outbound':
        coaching = MaxTradingOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'ESR TechTalent Outbound':
        coaching = ESRTechTalentOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Green Connect Outbound':
        coaching = GreenConnectOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Central Mortgage Funding':
        coaching = CentralMortgageFundingOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Rapid Mortgage':
        coaching = RapidMortgageOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Bridan & Associates Outbound':
        coaching = BridanAssociatesOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Linen Finder Outbound':
        coaching = LinenFinderOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Better Ed Outbound':
        coaching = BetterEdOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Com 98 Outbound':
        coaching = Com98Outboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Gretna Medical Centre Outbound':
        coaching = GretnaMedicalCentreOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Arista MD Outbound':
        coaching = AristaMDOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Robert Damon Production Outbound':
        coaching = RobertDamonProductionOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Venwiz Outbound':
        coaching = VenwizOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'City Habitat Outbound':
        coaching = CityHabitatOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Optel Outbound':
        coaching = OptelOutboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'South County Outbound':
        coaching = SouthCountyOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Inpress Outbound':
        coaching = InpressOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'L & M Enterprises Outbound':
        coaching = LMEnterprisesOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Towers Traders Group Outbound':
        coaching = TowersTradersGroupOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Job E Roofing Outbound':
        coaching = JobERoofingOutboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-new-series.html', data)

    elif process_name == 'Travel Wholesale Outbound':
        coaching = TravelWholesaleOutboundMonForm.objects.get(id=pk)
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

    elif process_name == 'LJ Hub Inbound':
        coaching = LJHubInboundMonForms.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'Obthera Inc':
        coaching = ObtheraIncInboundMonForms.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'Eduvocate Inbound':
        coaching = EduvocateInboundMonForms.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'Cross Tower Inbound':
        coaching = CrossTowerInboundMonForms.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'Sana Life Science Inbound':
        coaching = SanaLifeScienceInbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'Mobile 22 Inbound':
        coaching = MonitoringFormMobile22InboundCalls.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'Xport Digital Inbound':
        coaching = XportDigitalInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'Calista Inbound':
        coaching = CalistaInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'Global Ark Inbound':
        coaching = GlobalArkInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    # New Added
    elif process_name == 'Hard Hat Technologies Inbound':
        coaching = HardHatTechnologiesInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == '3rd Wave Inbound':
        coaching = ThirdWaveInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)


    elif process_name == 'Gretna Medical Center Inbound':
        coaching = GretnaMedicalCenterInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)


    elif process_name == 'Better Ed Inbound':
        coaching = BetterEdInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)


    elif process_name == 'Com 98 Inbound':
        coaching = Com98InboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)


    elif process_name == 'Open Winds Inbound':
        coaching = OpenWindsInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'Embassy Luxury Inbound':
        coaching = EmbassyLuxuryInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'South County Inbound':
        coaching = SouthCountyInboundMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-inbound-common.html', data)

    elif process_name == 'City Habitat Inbound':
        coaching = CityHabitatInboundMonForm.objects.get(id=pk)
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



    elif process_name == 'Finesse Mortgage Email':
        coaching = FinesseMortgageEmailMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    elif process_name == 'Fur Baby':
        coaching = FurBabyMonForm.objects.get(id=pk)
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

    elif process_name == 'US Jaclean Email Chat':
        coaching = USJacleanEmailChatForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    elif process_name == 'Cross Tower Email-Chat':
        coaching = CrossTowerEmailChatForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    elif process_name == 'Sana Life Science Email-Chat':
        coaching = SanaLifeScienceEmailChatForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    elif process_name == 'Bhagyalaxmi Chat':
        coaching = BhagyalaxmiChatMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    elif process_name == 'Sapphire Medicals Chat':
        coaching = SapphireMedicalsChatMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    elif process_name == 'Gretna Medical Center Email':
        coaching = GretnaMedicalCenterEmailChatForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    elif process_name == 'Jump Rydes Email - Chat':
        coaching = JumpRydesEmailChatForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    elif process_name == 'Naffa Innovation Email - Chat':
        coaching = NaffaInnovationEmailChatForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-email-chat.html', data)

    elif process_name == 'Inpress Email - Chat':
        coaching = InpressEmailChatForm.objects.get(id=pk)
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

    if process_name == 'Practo':
        coaching = PractoNewVersion.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-practo-chat.html', data)

    if process_name == 'Gubagoo':
        coaching = GubagooAuditForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-gubagoo.html', data)

    if process_name == 'IL Makiage':
        coaching = ILMakiageEmailChatForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-ILM.html', data)

    if process_name == 'Digital Swiss Gold Email - Chat':
        coaching = DigitalSwissGoldEmailChatMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-dsg-email-chat.html', data)

    if process_name == 'Winopoly Outbound':
        coaching = WinopolyOutbound.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-winopoly.html', data)

    if process_name == 'AB Hindalco':
        coaching = ABHindalcoMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-abh.html', data)

    if process_name == 'Blazing Hog':
        coaching = BlazingHogEmailChatmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-blazing.html', data)

    if process_name == 'Practo Chat':
        coaching = NewPractoWithSubCategory.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-practo-chat.html', data)

    if process_name == 'Nerotel Inbound':
        coaching = NerotelInboundmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-nerotel.html', data)

    if process_name == 'Spoiled Child':
        coaching = SpoiledChildChatmonform.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-spoiled-child.html', data)

    if process_name == 'Amerisave':
        coaching = AmerisaveMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-amerisave.html', data)

    if process_name == 'Movement Insurance':
        coaching = MovementInsuranceMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-movement_insurance.html', data)

    if process_name == 'Brightway':
        coaching = BrightwayMonForm.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/qa-coaching-view-brightway.html', data)

    else:
        pass


# Campaign wise coaching view - qa - manager

def campaignwiseCoachings(request):
    if request.method == 'POST':
        campaign = request.POST['campaign']
        status = request.POST['status']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        if start_date and end_date:
            if status == 'all':
                coaching_list = []

                def dateAll(monform):
                    obj = monform.objects.filter(process=campaign, audit_date__range=[start_date, end_date])
                    return obj

                for i in list_of_monforms:
                    obj = dateAll(i)
                    coaching_list.append(obj)
            else:
                coaching_list = []

                def datestatusAll(monform):
                    obj = monform.objects.filter(process=campaign, status=status,
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
                    obj = monform.objects.filter(process=campaign)
                    return obj

                for i in list_of_monforms:
                    obj = dateAll(i)
                    coaching_list.append(obj)

            else:
                coaching_list = []

                def datestatusAll(monform):
                    obj = monform.objects.filter(process=campaign, status=status)
                    return obj

                for i in list_of_monforms:
                    obj = datestatusAll(i)
                    coaching_list.append(obj)

            data = {'coaching_list': coaching_list,
                    }

            return render(request, 'campaign-wise-coaching-view.html', data)
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
            coaching = i.objects.filter(qa=qa, process=campaign, audit_date__range=[start_date, end_date])
            coaching_list.append(coaching)
        data = {'coaching_list': coaching_list}
        return render(request, 'campaign-wise-coaching-view.html', data)

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
        emp_name = request.POST['emp_name']

        if start_date and end_date:

            if status == 'all':

                coaching_list = []

                def dateAll(monform):
                    obj = monform.objects.filter(campaign=team_name, associate_name=emp_name,
                                                 audit_date__range=[start_date, end_date])
                    return obj

                for i in list_of_monforms:
                    obj = dateAll(i)
                    coaching_list.append(obj)

            else:

                coaching_list = []

                def datestatusAll(monform):
                    obj = monform.objects.filter(campaign=team_name, associate_name=emp_name, status=status,
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
                    obj = monform.objects.filter(campaign=team_name, associate_name=emp_name, )
                    return obj

                for i in list_of_monforms:
                    obj = dateAll(i)
                    coaching_list.append(obj)

            else:

                coaching_list = []

                def datestatusAll(monform):
                    obj = monform.objects.filter(campaign=team_name, associate_name=emp_name, status=status)
                    return obj

                for i in list_of_monforms:
                    obj = datestatusAll(i)
                    coaching_list.append(obj)

            data = {'coaching_list': coaching_list,
                    }

            return render(request, 'campaign-wise-coaching-view.html', data)

    else:
        pass


def campaignwiseDetailedReport(request, cname):
    if request.method == 'POST':

        from datetime import datetime
        currentMonth = request.POST['month']
        currentYear = request.POST['year']
        campaign = cname

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

            open_coaching_employee_wise = monform.objects.filter(status=False, audit_date__year=currentYear,
                                                                 audit_date__month=currentMonth).values(
                'associate_name').annotate(
                dcount=Count('status'))

            dispute_coaching = monform.objects.filter(disput_status=True, audit_date__year=currentYear,
                                                      audit_date__month=currentMonth).values('associate_name').annotate(
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

            open_coaching_employee_wise = monform.objects.filter(status=False, audit_date__year=currentYear,
                                                                 audit_date__month=currentMonth).values(
                'associate_name').annotate(dcount=Count('status'))

            dispute_coaching = monform.objects.filter(disput_status=True, audit_date__year=currentYear,
                                                      audit_date__month=currentMonth).values('associate_name').annotate(
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


def signCoaching(request, pk):
    from datetime import date
    now = date.today()
    category = request.POST['category']
    emp_comments = request.POST['emp_comments']

    for i in list_of_monforms:
        obj = i.objects.all()
        if obj.count() > 0:
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
    coaching.disput_status = False
    coaching.save()
    return redirect('/employees/agenthome')


def coachingSuccess(request):
    return render(request, 'coaching-success-message.html')


def coachingDispute(request, pk):
    if request.method == 'POST':
        id = pk
        managers = Profile.objects.filter(emp_desi='Manager').order_by('emp_name')
        ams = Profile.objects.filter(emp_desi='AM').order_by('emp_name')
        tls = Profile.objects.filter(emp_desi='Team Leader').order_by('emp_name')

        process = request.POST['campaign']
        emp_comments = request.POST['emp_comments_dispute']

        data = {'managers': managers, 'ams': ams, 'tls': tls,
                'emp_comments': emp_comments, 'process': process,
                'id': id
                }
        return render(request, 'select-manager-am-tl.html', data)


def coachingDisputeFinal(request, pk):
    if request.method == 'POST':

        emp_name = request.user.profile.emp_name
        team = request.user.profile.process
        cid = pk
        process = request.POST['campaign']
        manager_email = request.POST['manager_email']
        am_email = request.POST['am_email']
        tl_email = request.POST['tl_email']
        emp_comments = request.POST['emp_comments_dispute']

        for i in list_of_monforms:
            obj = i.objects.all()
            if obj.count() > 0:
                if obj[0].process == process:
                    campaign = i
                else:
                    pass
            else:
                pass

        obj = campaign.objects.get(id=cid)
        obj.disput_status = True
        obj.emp_comments = emp_comments
        obj.save()
        qn_name = obj.qa

        try:
            qa_email_id = Profile.objects.get(emp_name=qn_name).email
            qa_am = Profile.objects.get(emp_name=qn_name).team_lead
            qa_am_email_id = Profile.objects.get(emp_name=qa_am).email
        except Profile.DoesNotExist:
            qa_am_email_id = 'sumitkumar.s@expertcallers.com'

        # ##### sending EMAIL ##### #
        receive_list = [manager_email, am_email, tl_email, 'tabassum.z@expertcallers.com',
                        qa_am_email_id, qa_email_id]

        html_path = 'dispute-template.html'
        data = {'id': cid, 'process': process, 'emp_name': emp_name, 'emp_comments': emp_comments}
        email_template = get_template(html_path).render(data)

        email_msg = EmailMessage('QMS - Coaching Dispute',
                                 email_template, 'qms@expertcallers.com',
                                 receive_list,
                                 reply_to=['qms@expertcallers.com'])
        email_msg.content_subtype = 'html'
        email_msg.send(fail_silently=False)

        data = {'team': team}

        return render(request, 'coaching-dispute-message.html', data)
    else:
        return redirect('/employees/agenthome')


def qahome(request):
    if request.method == 'POST':

        currentMonth = request.POST['month']
        currentYear = request.POST['year']
        qa_name = request.user.profile.emp_name

        # Total NO of Coachings
        total_coaching_ids = []
        for i in list_of_monforms:
            x = i.objects.filter(added_by=qa_name, audit_date__year=currentYear, audit_date__month=currentMonth)
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
            x = i.objects.filter(added_by=qa_name, audit_date__year=currentYear, audit_date__month=currentMonth)
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


# campaign View

def campaignView(request):
    if request.method == 'POST':

        campaign_id = request.POST['campaign_id']
        campaign = Campaigns.objects.get(id=campaign_id)
        agents = Profile.objects.exclude(emp_desi__in=['AM', 'Manager', 'Team Leader', 'Trainer', 'QA']).order_by(
            'emp_name')

        data = {'campaign': campaign, 'agents': agents}
        return render(request, 'campaign-view.html', data)

    else:
        pass


def selectCoachingForm(request):
    if request.method == 'POST':

        import datetime
        today_date = datetime.date.today()
        new_today_date = today_date.strftime("%Y-%m-%d")
        agent_id = request.POST['agent_id']
        campaign_id = request.POST['campaign_id']
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
            data = {'agent': agent, 'campaign': campaign, 'date': new_today_date}
            return render(request, 'mon-forms/ECPL-EVA&NOVO-Monitoring-Form-chat.html', data)

        elif campaign_type == 'Noom POD':

            data = {'agent': agent, 'campaign': campaign, 'date': new_today_date}
            return render(request, 'mon-forms/ECPL-Pod-Father-Monitoring-Form-chat.html', data)

        elif campaign_type == 'Fame House':
            data = {'agent': agent, 'campaign': campaign, 'date': new_today_date}
            return render(request, 'mon-forms/fame-house-new.html', data)

        elif campaign_type == 'Gubagoo':
            data = {'agent': agent, 'campaign': campaign, 'date': new_today_date}
            return render(request, 'mon-forms/gubagoo.html', data)

        elif campaign_type == 'Practo':
            data = {'agent': agent, 'campaign': campaign, 'date': new_today_date}
            return render(request, 'mon-forms/practo.html', data)

        elif campaign_type == 'PractoNew':
            data = {'agent': agent, 'campaign': campaign, 'date': new_today_date}
            return render(request, 'mon-forms/practo_chat.html', data)

        elif campaign_type == 'ILM':
            data = {'agent': agent, 'campaign': campaign, 'date': new_today_date}
            return render(request, 'mon-forms/ILM.html', data)

        elif campaign_type == 'DSG':
            data = {'agent': agent, 'campaign': campaign, 'date': new_today_date}
            return render(request, 'mon-forms/digital-swiss-gold-email-chat.html', data)

        elif campaign_type == 'wp1':
            data = {'agent': agent, 'campaign': campaign, 'date': new_today_date}
            return render(request, 'mon-forms/winopoly_1.html', data)

        elif campaign_type == 'ABH':
            data = {'agent': agent, 'campaign': campaign, 'date': new_today_date}
            return render(request, 'mon-forms/abh_new.html', data)

        elif campaign_type == 'Blazing Hog':
            data = {'agent': agent, 'campaign': campaign, 'date': new_today_date}
            return render(request, 'mon-forms/Blazing-Hog.html', data)

        elif campaign_type == 'Nerotel Inbound':
            data = {'agent': agent, 'campaign': campaign, 'date': new_today_date}
            return render(request, 'mon-forms/nerotel_inbound.html', data)

        elif campaign_type == 'Spoiled Child':
            data = {'agent': agent, 'campaign': campaign, 'date': new_today_date}
            return render(request, 'mon-forms/spoiled_child.html', data)

        elif campaign_type == 'Amerisave':
            data = {'agent': agent, 'campaign': campaign, 'date': new_today_date}
            return render(request, 'mon-forms/amerisave.html', data)

        elif campaign_type == 'Movement Insurance':
            data = {'agent': agent, 'campaign': campaign, 'date': new_today_date}
            return render(request, 'mon-forms/movement_insurance.html', data)

        elif campaign_type == 'Brightway':
            data = {'agent': agent, 'campaign': campaign, 'date': new_today_date}
            return render(request, 'mon-forms/bright_way.html', data)

    else:
        return redirect('/employees/qahome')


def coachingSummaryView(request):
    return render(request, 'coaching-summary-view.html')


def qualityDashboard(request):
    return render(request, 'quality-dashboard.html')


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
                       'qa', 'am', 'team_lead', 'manager', 'customer_name', 'customer_contact', 'zone', 'concept',

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

                       'status', 'dispute_status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = monform.objects.filter(audit_date__range=[start_date, end_date],
                                          ).values_list(
                'process', 'emp_id', 'associate_name', 'call_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager', 'customer_name', 'customer_contact', 'zone', 'concept',

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

                'status', 'disput_status',
                'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response

        #######  OUTBOUND ###########

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

        elif campaign == 'Clean-Living Health and Wellness':
            response = exportAadyaseries(CleanLivingHealthWellnessOutboundMonForm)
            return response

        elif campaign == 'Practo Outbound':
            response = exportAadyaseries(PractoOutboundMonForm)
            return response

        elif campaign == 'Imaginarium Outbound':
            response = exportAadyaseries(ImaginariumOutboundMonForm)
            return response

        elif campaign == 'US Jaclean Outbound':
            response = exportAadyaseries(USJacleanOutboundForm)
            return response

        elif campaign == 'Global Galaxy Outbound':
            response = exportAadyaseries(GlobalGalaxyOutboundForm)
            return response

        elif campaign == 'Community Health Project Inc':
            response = exportAadyaseries(CommunityHealthProjectIncOutbound)
            return response

        elif campaign == 'Educated Analytics LLC':
            response = exportAadyaseries(EducatedAnalyticsLLCOutbound)
            return response

        elif campaign == 'New Dimension Pharmacy':
            response = exportAadyaseries(NewDimensionPharmacyOutbound)
            return response

        elif campaign == 'Stay-N-Charge':
            response = exportAadyaseries(StayNChargeOutbound)
            return response

        elif campaign == 'J & H Energy Consultant':
            response = exportAadyaseries(JHEnergyConsultantOutbound)
            return response

        elif campaign == 'MDR Group LLC':
            response = exportAadyaseries(MDRGroupLLCOutbound)
            return response

        elif campaign == 'Corey Small Insurance Agency Inc':
            response = exportAadyaseries(CoreySmallInsuranceAgencyOutbound)
            return response

        elif campaign == 'Eduvocate Outbound':
            response = exportAadyaseries(EduvocateOutbound)
            return response

        elif campaign == 'Cross Tower Outbound':
            response = exportAadyaseries(CrossTowerOutbound)
            return response

        elif campaign == 'Dawn Financial Outbound':
            response = exportAadyaseries(DawnFinancialOutbound)
            return response

        elif campaign == 'Xport Digital Outbound':
            response = exportAadyaseries(XportDigitalOutbound)
            return response

        elif campaign == 'Calista Outbound':
            response = exportAadyaseries(CalistaOutboundMonForm)
            return response

        elif campaign == 'Global Ark Outbound':
            response = exportAadyaseries(GlobalArkOutboundMonform)
            return response

        elif campaign == 'DI Develop Outbound':
            response = exportAadyaseries(DIDevelopOutbound)
            return response

        elif campaign == 'Freehold Outbound':
            response = exportAadyaseries(FreeholdOutboundMonForm)
            return response

        elif campaign == 'Zeamo Outbound':
            response = exportAadyaseries(ZeamoOutboundMonForm)
            return response

        elif campaign == 'Sapphire Medicals Outbound':
            response = exportAadyaseries(SapphireMedicalsOutboundMonForm)
            return response

        elif campaign == 'Eehhaaa Outbound':
            response = exportAadyaseries(EehhaaaOutboundMonForm)
            return response

        elif campaign == 'All Care Physical Therapy':
            response = exportAadyaseries(AllCarePhysicalTherapyMonform)
            return response

        elif campaign == 'Executive Capital Resources':
            response = exportAadyaseries(ExecutiveCapitalResourcesmonform)
            return response

        elif campaign == 'Bright Way Outbound':
            response = exportAadyaseries(BrightWayOutboundmonform)
            return response

        elif campaign == 'Building lab LLC Outbound':
            response = exportAadyaseries(BuildinglabLLCOutboundmonform)
            return response

        elif campaign == 'Global Pharma Outbound':
            response = exportAadyaseries(GlobalPharmaOutboundmonform)
            return response

        elif campaign == 'Redefine Plastics Outbound':
            response = exportAadyaseries(RedefinePlasticsOutboundmonform)
            return response

        elif campaign == 'Hard Hat Technologies Outbound':
            response = exportAadyaseries(HardHatTechnologiesOutboundmonform)
            return response

        elif campaign == '3rd Wave Outbound':
            response = exportAadyaseries(ThirdWaveOutboundmonform)
            return response

        elif campaign == 'K7 Outbound':
            response = exportAadyaseries(K7Outboundmonform)
            return response

        elif campaign == 'Trial Mapping Outbound':
            response = exportAadyaseries(TrialMappingOutboundmonform)
            return response

        elif campaign == 'Edu Class Outbound':
            response = exportAadyaseries(EduClassOutboundmonform)
            return response

        elif campaign == 'Cred Avenue Outbound':
            response = exportAadyaseries(CredAvenueOutboundmonform)
            return response

        elif campaign == 'TKAWDIW Outbound':
            response = exportAadyaseries(TKAWDIWOutboundmonform)
            return response

        elif campaign == 'Dream Pick Outbound':
            response = exportAadyaseries(DreamPickOutboundmonform)
            return response

        elif campaign == 'Kheloyar Outbound':
            response = exportAadyaseries(KheloyarOutboundmonform)
            return response

        elif campaign == 'Mex Trading Outbound':
            response = exportAadyaseries(MaxTradingOutboundmonform)
            return response

        elif campaign == 'ESR TechTalent Outbound':
            response = exportAadyaseries(ESRTechTalentOutboundmonform)
            return response

        elif campaign == 'Green Connect Outbound':
            response = exportAadyaseries(GreenConnectOutboundmonform)
            return response

        elif campaign == 'Central Mortgage Funding':
            response = exportAadyaseries(CentralMortgageFundingOutboundmonform)
            return response

        elif campaign == 'Rapid Mortgage':
            response = exportAadyaseries(RapidMortgageOutboundmonform)
            return response

        elif campaign == 'Bridan & Associates Outbound':
            response = exportAadyaseries(BridanAssociatesOutboundmonform)
            return response

        elif campaign == 'Linen Finder Outbound':
            response = exportAadyaseries(LinenFinderOutboundmonform)
            return response

        elif campaign == 'Better Ed Outbound':
            response = exportAadyaseries(BetterEdOutboundmonform)
            return response

        elif campaign == 'Com 98 Outbound':
            response = exportAadyaseries(Com98Outboundmonform)
            return response


        elif campaign == 'Gretna Medical Centre Outbound':
            response = exportAadyaseries(GretnaMedicalCentreOutboundmonform)
            return response

        elif campaign == 'Arista MD Outbound':
            response = exportAadyaseries(AristaMDOutboundmonform)
            return response

        elif campaign == 'Robert Damon Production Outbound':
            response = exportAadyaseries(RobertDamonProductionOutboundmonform)
            return response

        elif campaign == 'Venwiz Outbound':
            response = exportAadyaseries(VenwizOutboundmonform)
            return response

        elif campaign == 'City Habitat Outbound':
            response = exportAadyaseries(CityHabitatOutboundmonform)
            return response

        elif campaign == 'Optel Outbound':
            response = exportAadyaseries(OptelOutboundmonform)
            return response

        elif campaign == 'South County Outbound':
            response = exportAadyaseries(SouthCountyOutboundMonForm)
            return response

        elif campaign == 'Inpress Outbound':
            response = exportAadyaseries(InpressOutboundMonForm)
            return response

        elif campaign == 'L & M Enterprises Outbound':
            response = exportAadyaseries(LMEnterprisesOutboundMonForm)
            return response

        elif campaign == 'Towers Traders Group Outbound':
            response = exportAadyaseries(TowersTradersGroupOutboundMonForm)
            return response

        elif campaign == 'Job E Roofing Outbound':
            response = exportAadyaseries(JobERoofingOutboundMonForm)
            return response

        elif campaign == 'Travel Wholesale Outbound':
            response = exportAadyaseries(TravelWholesaleOutboundMonForm)
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
                       'qa', 'am', 'team_lead', 'manager', 'customer_name', 'customer_contact', 'zone', 'concept',

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

                       'status', 'dispute_status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = monform.objects.filter(audit_date__range=[start_date, end_date],
                                          ).values_list(
                'process', 'emp_id', 'associate_name', 'call_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager', 'customer_name', 'customer_contact', 'zone', 'concept',

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

                'status', 'disput_status',
                'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments')

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

        elif campaign == 'LJ Hub Inbound':
            response = exportinbound(LJHubInboundMonForms)
            return response

        elif campaign == 'Obthera Inc':
            response = exportinbound(ObtheraIncInboundMonForms)
            return response

        elif campaign == 'Eduvocate Inbound':
            response = exportinbound(EduvocateInboundMonForms)
            return response

        elif campaign == 'Cross Tower Inbound':
            response = exportinbound(CrossTowerInboundMonForms)
            return response

        elif campaign == 'Sana Life Science Inbound':
            response = exportinbound(SanaLifeScienceInbound)
            return response

        elif campaign == 'Mobile 22 Inbound':
            response = exportinbound(MonitoringFormMobile22InboundCalls)
            return response

        elif campaign == 'Xport Digital Inbound':
            response = exportinbound(XportDigitalInboundMonForm)
            return response

        elif campaign == 'Calista Inbound':
            response = exportinbound(CalistaInboundMonForm)
            return response

        elif campaign == 'Global Ark Inbound':
            response = exportinbound(GlobalArkInboundMonForm)
            return response

        elif campaign == '3rd Wave Inbound':
            response = exportinbound(ThirdWaveInboundMonForm)
            return response

        elif campaign == 'Hard Hat Technologies Inbound':
            response = exportinbound(HardHatTechnologiesInboundMonForm)
            return response

        elif campaign == 'Gretna Medical Center Inbound':
            response = exportinbound(GretnaMedicalCenterInboundMonForm)
            return response

        elif campaign == 'Better Ed Inbound':
            response = exportinbound(BetterEdInboundMonForm)
            return response

        elif campaign == 'Com 98 Inbound':
            response = exportinbound(Com98InboundMonForm)
            return response

        elif campaign == 'Open Winds Inbound':
            response = exportinbound(OpenWindsInboundMonForm)
            return response

        elif campaign == 'Embassy Luxury Inbound':
            response = exportinbound(EmbassyLuxuryInboundMonForm)
            return response

        elif campaign == 'South County Inbound':
            response = exportinbound(SouthCountyInboundMonForm)
            return response

        elif campaign == 'City Habitat Inbound':
            response = exportinbound(CityHabitatInboundMonForm)
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
                       'qa', 'am', 'team_lead', 'manager', 'customer_name', 'customer_contact',

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

                       'status', 'disput_status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = monform.objects.filter(
                audit_date__range=[start_date, end_date], ).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager', 'customer_name', 'customer_contact',

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

                'status', 'disput_status',
                'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments')

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
        elif campaign == 'Finesse Mortgage Email':
            response = exportEmailChat(FinesseMortgageEmailMonForm)
            return response
        elif campaign == 'Fur Baby':
            response = exportEmailChat(FurBabyMonForm)
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

        elif campaign == 'US Jaclean Email Chat':
            response = exportEmailChat(USJacleanEmailChatForm)
            return response

        elif campaign == 'Cross Tower Email-Chat':
            response = exportEmailChat(CrossTowerEmailChatForm)
            return response

        elif campaign == 'Sana Life Science Email-Chat':
            response = exportEmailChat(SanaLifeScienceEmailChatForm)
            return response

        elif campaign == 'Bhagyalaxmi Chat':
            response = exportEmailChat(BhagyalaxmiChatMonForm)
            return response

        elif campaign == 'Sapphire Medicals Chat':
            response = exportEmailChat(SapphireMedicalsChatMonForm)
            return response

        elif campaign == 'Gretna Medical Center Email':
            response = exportEmailChat(GretnaMedicalCenterEmailChatForm)
            return response

        elif campaign == 'Jump Rydes Email - Chat':
            response = exportEmailChat(JumpRydesEmailChatForm)
            return response

        elif campaign == 'Naffa Innovation Email - Chat':
            response = exportEmailChat(NaffaInnovationEmailChatForm)
            return response

        elif campaign == 'Inpress Email - Chat':
            response = exportEmailChat(InpressEmailChatForm)
            return response

            ########## other campaigns ##############

        elif campaign == 'Blazing Hog':
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
                       'qa', 'am', 'team_lead', 'manager', 'customer_name', 'ticket_id', 'zone', 'concept',
                       'query_type',

                       "Understanding and Solved Customer's Issue",
                       "Displayed process knowledge",
                       'Documentation - Full information captured in internal spreadsheet',
                       'Did the agent mention correct and adequate notes if necessary',

                       'Resolved/Assigned Ticket issue in a timely manner',
                       'Categorized case properly/Check other Tickets & Previous communition Merged',

                       'Assigned to the correct department',
                       'Tool usage',
                       'Edited Customer profile/Check customer profile',

                       'status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = BlazingHogEmailChatmonform.objects.filter(audit_date__range=[start_date, end_date]).values_list(
                'process', 'emp_id', 'associate_name', 'call_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager', 'customer_name', 'ticket_id', 'zone', 'concept', 'query_type',

                'solution_1',
                'solution_2',
                'solution_3',
                'solution_4',

                'efficiency_1',
                'efficiency_2',

                'compliance_1',
                'compliance_2',
                'compliance_3',

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


        elif campaign == 'AB Hindalco':
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
                       'qa', 'am', 'team_lead', 'manager', 'customer_name', 'customer_contact', 'zone', 'concept',

                       'Used Standard Opening Protocol',
                       'Introduction of Product / Branding - 4 USP of eternia - WiWA, Warranty, Duranium, Eternia care Mentioning Hindalco, Aditya birla group',
                       'Call Closing as per the Protocol',

                       'Used Empathetic Statements whenever required',
                       'Making the conversation 2 ways, giving chance to the customer to ask question',
                       'Active Listening without Interruption',

                       'Followed Policy & Procedure (Script)',
                       'Accurate Documentation with full details in ZOHO',
                       'Inaccurate Information : Identifying the right lead to opportunity',
                       'Advisor Sounding Rude / Proafinity Usage',

                       'status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = ABHindalcoMonForm.objects.filter(audit_date__range=[start_date, end_date]).values_list(
                'process', 'emp_id', 'associate_name', 'call_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager', 'customer_name', 'customer_contact', 'zone', 'concept',

                'oc_1',
                'oc_2',
                'oc_3',

                'softskill_1',
                'softskill_2',
                'softskill_3',

                'compliance_1',
                'compliance_2',
                'compliance_3',
                'compliance_4',

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

        elif campaign == 'Winopoly Outbound':
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

                       'Recording Disclosure - (Agent must disclose the call is recorded)',
                       'Rep Name - (Did agent introduce her/himself during opening?)',
                       'Branding/Site Name - (Did the agent state the site name name in the opening?)',
                       'Call Reason - (Did the agent state the reason for the call? (confirmation call))',
                       'Contact Information - (Did the agent verify the contact info?)',

                       'Targeted Spotlight offer - (Did the agent attempt the Targeted spotlight offer?)',
                       'Lead offer - (Did the agent attempt the lead offer?)',
                       'Verification - (Did the agent ask all verification questions were applicaple?)',

                       'Excessisive off topic conversations - (Did the agent avoid unnessesary off topic conversations)',
                       'Polite - (Follow up done on the Pending Tickets (Chats & Email))',
                       'Positive and Upbeat - (Did the agent have a positive and upbeat tone)',
                       'Ethics - (Did the agent advoid misleading information about offers)',
                       'Call control - (Did the agent take control of the call)',
                       'Program of Interest - (Did the agent match the lead to a program that they stated interest in, without having to push the lead into agreeing to the program?)',

                       'TCPA Close - (Did the rep read a TCPA statement and receive an affirmative response from the lead (Yes or Yeah)?)',
                       'TCPA Close - (If interrupted did the agent reread the TCPA and get an affimative response)',
                       'Do Not Call Request - (Agent followed DNC Request Policy)',
                       'California Privacy Policy - (Agent followed CA Policy Privacy by reading the written statement for CA residents)',
                       'Transfering the call - (Did the agent conduct the intro on the transfer correctly?)',
                       'Transfer Only - (Did the agent conduct the intro on the transfer correctly)',
                       'Disposition - (Did the agent used the correct disposition?)',
                       'Auto Fail - (ZERO TOLERANCE POLICY)',

                       'status', 'disput_status',
                       'closed_date', 'fatal', 'coaching_comments', 'evaluator_comment']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = WinopolyOutbound.objects.filter(
                audit_date__range=[start_date, end_date]).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager', 'customer_name', 'customer_contact',

                'comp_1',
                'op_2',
                'op_3',
                'op_4',
                'op_5',

                'mp_1',
                'mp_2',
                'mp_3',

                'cp_1',
                'cp_2',
                'cp_3',
                'cp_4',
                'cp_5',
                'cp_6',

                'comp_2',
                'comp_3',
                'comp_4',
                'comp_5',

                'tp_1',
                'tp_2',
                'tp_3',
                'comp_6',

                'status', 'disput_status', 'closed_date', 'fatal', 'evaluator_comment', 'coaching_comments')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response

        elif campaign == 'Digital Swiss Gold Email - Chat':
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
                       'Follow up done on the Pending Tickets (Chats & Email)',
                       'Refund / Retruns / Escalation Updated in the google sheet',
                       'Process & Procedure Followed',
                       'First Chat / Email Resolution',

                       'status', 'disput_status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = DigitalSwissGoldEmailChatMonForm.objects.filter(
                audit_date__range=[start_date, end_date]).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager', 'customer_name', 'customer_contact',

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

                'status', 'disput_status',
                'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response

        elif campaign == 'IL Makiage':

            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = ['process', 'empID', 'Associate Name', 'Email/chat date', 'Audit Date', 'overall_score',
                       'Fatal Count',
                       'qa', 'am', 'team_lead', 'manager', 'customer_name', 'ticket_id', 'Query Type',

                       "Understanding and Solved Customer's Issue",
                       'Gave alternatives when required/applicable & Displayed expert product knowledge',
                       'Coupon code added/Edited Name/Values & Date//Personalised when applicable',
                       'Answered all question effectively',
                       'Resolved issue in a timely manner',
                       'Categorized case properly/Check other Tickets &Previous communition Merged',
                       'Appropriate use of macros',
                       'Magento was utilized correctly',
                       'Identified correct order type',

                       'status', 'disput_status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = ILMakiageEmailChatForm.objects.filter(
                audit_date__range=[start_date, end_date]).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager', 'customer_name', 'ticket_id', 'query_type',

                's_1',
                's_2',
                's_3',
                's_4',

                'e_1',
                'e_2',

                'compliance_1',
                'compliance_2',
                'compliance_3',

                'status', 'disput_status',
                'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)
            return response

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

                       'Shipping product incorrectly',

                       'Incorrect grammar and spelling being used/illegible responses/Does not make sense.',

                       'Blatantly incorrect or made up information provided to the customer',

                       'Sending internal notes as Public response',

                       'Responding to any ticket outside of representatives skills/assignments',

                       'Unprofessional- tone,language or content. Uses derogatory language or curse words.',

                       'Not escalating a situation/Not following proper escalation procedure/Responding to an escalated ticket',

                       'Responding to Spam',

                       'Double response-w/o addressing and apologizing',

                       'Responding with personal opinions outside of company policy',

                       'Sending same macro as last agent w/o edits.',

                       'Agent sent response as public reply',

                       'Agent greeted customer by correct name',

                       'Agent used correct appreciation/acknowledgement statement',

                       'Agent composed email with logical flow that makes sense',

                       'Agent presented information with clear formatting, correct spelling and grammar',

                       'Agent chose correct macro(s).',

                       "Agent tailored macro(s) to fit the customer's question or issue",

                       'Agent asked the customer if he/she could be of additional help',

                       'Agent used appropriate closing & signature',

                       'Agent correctly identified and understood customer issue and responded accordingly (Issue Identification)',

                       'Agent fully resolved inquiry/issue upon first contact when possible, or clearly communicated additional information/next steps for full resolution. (Issue Resolution)',

                       'Agent did not deflect any questions/avoid policy communications unnecessarily. (Non-avoidance)',

                       'Agent conveyed correct policy information to the customer',

                       'Agent conveyed correct product information to the customer',

                       'Agent established correct timeline to resolution/ CSR did not delay resolution. (Resolution Timeline)',

                       'Rep fully and accurately helped the customer within their empowerments or escalated appropriately. (Agent Empowerments)',

                       "Agent validated the customer's concern / questions / reason for contacting us",

                       "Agent offered genuine acknowledgement and empathy for customer's concern",

                       'Agent used positive tone and impartial language in all communications',
                       'Agent was professional and courteous',

                       "Representative answered in a tone consistent with UMG's core values and culture",

                       'Agent accurately completed all necessary field on the ticket',

                       'Agent merged tickets properly',

                       'Agent performed all needed Shopify processes and accurately relayed all needed information and screenshots to customer.',

                       'Agent completed all system processes correctly',

                       'status', 'disput_status',

                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows

            font_style = xlwt.XFStyle()

            rows = FameHouseNewMonForm.objects.filter(audit_date__range=[start_date, end_date], ).values_list(

                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',

                'am', 'team_lead', 'manager', 'ticket_no', 'ticket_type',

                'compliance_1',

                'compliance_2',

                'compliance_3',

                'compliance_4',

                'compliance_5',

                'compliance_6',

                'compliance_7',

                'compliance_8',

                'compliance_9',

                'compliance_10',

                'compliance_11',

                'cr_1',

                'opening_1',

                'opening_2',

                'comp_1',

                'comp_2',

                'macro_1',

                'macro_2',

                'closing_1',

                'closing_2',

                'cir_1',

                'cir_2',

                'cir_3',

                'cir_4',

                'cir_5',

                'cir_6',

                'cir_7',

                'et_1',

                'et_2',

                'et_3',

                'et_4',
                'et_5',

                'doc_1',

                'doc_2',

                'doc_3',

                'doc_4',

                'status', 'disput_status',
                'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments')

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

                       'If the user is missed to hit "finish" after sending the respective response. If the response is added with unwanted space and Punctuation. If the user name is miss-spelled/alphanumeric name on dashboard,we should use ???Hey there!???.',
                       'If the "You last checked in" user is not sent with respective message or sent twice with the response',
                       'If the user are not assigned in spreadsheet. Ex: If the user code is not added in the spreadsheet.',
                       'If "was assigned to you" users are not hit finish',

                       "If a user's query is missed to answer and directly assigned to GS.",
                       'If the user is directly assigned without an Acknowledgement. If the user is sent with irrelevant response. If user is missed to assign to a coach while user wish to be assigned',
                       'If the response is sent with any irrelevant words or free handed messages. If the task is popped up as UU and YLCI the UU task should be our first priority',
                       'If the user has a System generated message of cancellation and CRO assigned to next GS. Negative empathy for user???s message!',
                       'If the user is missed to send the survey response and assigned directly. If the survey messages are swapped.',
                       'If the user has a question or information about Covid, that needs to addressed to coaches or Seek a help from the slack channels and then respond to it',

                       'status', 'disput_status',
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

                'status', 'disput_status',
                'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments')

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

                       'If the user is missed to hit "finish" after sending the respective response. If the response is added with unwanted space and Punctuation. If the user name is miss-spelled/alphanumeric name on dashboard,we should use ???Hey there!???.',
                       'If the "You last checked in" user is not sent with respective message or sent twice with the response',
                       'If the user are not assigned in spreadsheet. Ex: If the user code is not added in the spreadsheet.',
                       'If "was assigned to you" users are not hit finish',

                       "If a user's query is missed to answer and directly assigned to GS.",
                       'If the user is directly assigned without an Acknowledgement. If the user is sent with irrelevant response. If user is missed to assign to a coach while user wish to be assigned',
                       'If the response is sent with any irrelevant words or free handed messages. If the task is popped up as UU and YLCI the UU task should be our first priority',
                       'If the user has a System generated message of cancellation and CRO assigned to next GS. Negative empathy for user???s message!',
                       'If the user is missed to send the survey response and assigned directly. If the survey messages are swapped.',
                       'If the user has a question or information about Covid, that needs to addressed to coaches or Seek a help from the slack channels and then respond to it',

                       'status', 'disput_status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = ChatMonitoringFormEva.objects.filter(audit_date__range=[start_date, end_date], ).values_list(
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

                'status', 'disput_status',
                'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments')

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

                       'status', 'disput_status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = FLAMonitoringForm.objects.filter(
                audit_date__range=[start_date, end_date], ).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager',

                'checklist_1',
                'reason_for_failure',

                'status', 'disput_status',
                'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response


        elif campaign == 'Practo':

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
                       'qa', 'am', 'team_lead', 'manager', 'conversation_id', 'customer_contact', 'training',

                       'Chat Opening (Greetings & being attentive) & Closing',
                       'FRTAT',
                       'Addressing the user/Personalisation of chat',
                       'Assurance & Acknowledgement',
                       'Coherence (understanding the issue) being attentive on chat.',
                       'Probing',
                       'Interaction: Empathy , Profressional, care',
                       'Grammar:',
                       'Relavant responses',
                       'Being courteous & using plesantries',
                       'Process followed',
                       'Explanation skills (Reasoning) & Rebuttal Handling',
                       'Sharing the information in a sequential manner',
                       'Case Documentation',
                       'Curation',
                       'Average speed of answer',
                       'Chat Hold Procedure &: Taking Perrmission before putting the chat on hold',
                       'Expectations: Setting correct expectations about issue resolution',
                       'ZTP(Zero Tolerance Policy)',

                       'status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = PractoNewVersion.objects.filter(
                audit_date__range=[start_date, end_date]).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager', 'conversation_id', 'customer_contact', 'training',
                'p_1',
                'p_2',
                'p_3',
                'p_4',
                'p_5',
                'p_6',
                'p_7',
                'p_8',
                'p_9',
                'p_10',
                'p_11',
                'p_12',
                'p_13',
                'p_14',
                'p_15',
                'p_16',
                'p_17',
                'compliance_1',
                'compliance_2',

                'status', 'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments')

        # practo chat
        elif campaign == 'Practo Chat':
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = ['process', 'empID', 'Associate Name', 'Chat date',
                       'Case Number',
                       'Issue Type',
                       'Sub-Issue Type',
                       'Sub Sub-Issue Type',
                       'CSAT',
                       'Product',
                       'Audit Date', 'overall_score',
                       'Fatal Count',
                       'qa', 'am', 'team_lead', 'manager',

                       'Chat Closing',
                       "Failed to close the chat",
                       "Failed to use the standard script (survey)",
                       "Multiple closing statement used",
                       "Failed to offer further assistance",
                       "User ended the chat",
                       "NA",

                       'FRTAT',

                       'Addressing User/Personalization of Chat',
                       "No Attempt",
                       "First name used on the chat",
                       "Less attempt - More scope",
                       "Failed to probe the user name",
                       "Incorrect Salutation",
                       "NA",

                       'Assistance & Acknowledgement',
                       "Failed to acknowledge",
                       "Incomplete acknowledgment",
                       "Failed to do throughout the chat",
                       "Incorrect assistance statement",
                       "NA",

                       'Relevant responses',

                       'Assurance',

                       'Probing',
                       "Irrelevant Probing",
                       "Incomplete Probing",
                       "Didn't Attempt to Probe",
                       "NA",

                       'Interaction: Empathy & Care, Professionalism',
                       "No Empathy",
                       "Lack of Professionalism",
                       "Lack of Care",
                       "Lack of Empathy",
                       "Inappropriate empathy",
                       'Repetitive empathy statement',
                       'NA',

                       'Grammar:',
                       "Punctuation",
                       "Capitalization",
                       "Typing Error",
                       "Sentence Formation",
                       'Spacing',
                       "Spacing",

                       'Being Courteous & Using Pleasantries',

                       'Process followed',
                       "SOP has not followed",
                       "Incorrect Information",
                       "Incomplete Information",
                       "Failed to authenticate for the medicine order",
                       "Incorrect TAT (or) Failed to inform the TAT",
                       "Incomplete/Incorrect refund details and wrong redirection",
                       "NA",

                       'Explanation Skills (Being Specific, Reasoning) & Rebuttal Handling',

                       'Sharing the Information in Sequential Manner',

                       'Case Documentation',

                       'Curation',
                       "Incomplete",
                       "Inappropriate",
                       "NA",

                       'Average speed of answer',

                       'Chat Hold Procedure &: Taking Permission before putting the chat on hold',
                       "Standard script not used",
                       "Failed to refresh the chat within promised time.",
                       "Failed to retrieve the chat",
                       "NA",

                       'PE knowledge base adherence',
                       "Failed to refer the knowledge base",
                       "Referred, but not confident",
                       "Incorrect category referred by the agent",
                       "NA",

                       'Expectations: Setting Correct Expectations about Issue Resolution',
                       "Incomplete Resolution",
                       "Incorrect Resolution",
                       "Process breach",

                       'ZTP (Zero Tolerance Policy)',

                       'status', 'disput_status',
                       'closed_date', 'fatal',
                       'areas_improvement', 'Specific Reason for FATAL with Labels and Sub Label', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = NewPractoWithSubCategory.objects.filter(
                audit_date__range=[start_date, end_date], ).values_list(
                'process', 'emp_id', 'associate_name', 'chat_date',
                'case_no',
                'issue_type',
                'sub_issue',
                'sub_sub_issue',
                'csat',
                'product',
                'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager',
                'p_1',
                'p1_s1',
                'p1_s2',
                'p1_s3',
                'p1_s4',
                'p1_s5',
                'p1_s6',
                'p_2',
                'p_3',
                'p3_s1',
                'p3_s2',
                'p3_s3',
                'p3_s4',
                'p3_s5',
                'p3_s6',
                'p_4',
                'p4_s1',
                'p4_s2',
                'p4_s3',
                'p4_s4',
                'p4_s5',
                'p_5',
                'p_6',
                'p_7',
                'p7_s1',
                'p7_s2',
                'p7_s3',
                'p7_s4',
                'p_8',
                'p8_s1',
                'p8_s2',
                'p8_s3',
                'p8_s4',
                'p8_s5',
                'p8_s6',
                'p8_s7',
                'p_9',
                'p9_s1',
                'p9_s2',
                'p9_s3',
                'p9_s4',
                'p9_s5',
                'p9_s6',
                'p_10',
                'p_11',
                'p11_s1',
                'p11_s2',
                'p11_s3',
                'p11_s4',
                'p11_s5',
                'p11_s6',
                'p11_s7',
                'p_12',
                'p_13',
                'p_14',
                'p_15',
                'p15_s1',
                'p15_s2',
                'p15_s3',
                'p_16',
                'p_17',
                'p17_s1',
                'p17_s2',
                'p17_s3',
                'p17_s4',
                'p_18',
                'p18_s1',
                'p18_s2',
                'p18_s3',
                'p18_s4',
                'compliance_1',
                'compliance1_s1',
                'compliance1_s2',
                'compliance1_s3',
                'compliance_2',

                'status', 'disput_status',
                'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response

        elif campaign == 'Gubagoo':

            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = ['process', 'empID', 'Associate Name', 'transaction date', 'Audit Date', 'overall_score',
                       'Fatal Count', 'qa', 'am', 'team_lead', 'manager',
                       'chat1_id', 'chat2_id', 'chat3_id', 'chat4_id', 'chat5_id', 'chat6_id',
                       'chat 1 score', 'chat 2 score', 'chat 3 score', 'chat 4 score', 'chat 5 score', 'chat 6 score',

                       'Was there a greeting? - chat1',
                       'Was there a greeting? - chat2',
                       'Was there a greeting? - chat3',
                       'Was there a greeting? - chat4',
                       'Was there a greeting? - chat5',
                       'Was there a greeting? - chat6',

                       'Proper greeting? - chat1',
                       'Proper greeting? - chat2',
                       'Proper greeting? - chat3',
                       'Proper greeting? - chat4',
                       'Proper greeting? - chat5',
                       'Proper greeting? - chat6',

                       'Did you ask all relevant questions? - chat1',
                       'Did you ask all relevant questions? - chat2',
                       'Did you ask all relevant questions? - chat3',
                       'Did you ask all relevant questions? - chat4',
                       'Did you ask all relevant questions? - chat5',
                       'Did you ask all relevant questions? - chat6',

                       'Were questions answered and/or relevant information/inventory pushed? - chat1',
                       'Were questions answered and/or relevant information/inventory pushed? - chat2',
                       'Were questions answered and/or relevant information/inventory pushed? - chat3',
                       'Were questions answered and/or relevant information/inventory pushed? - chat4',
                       'Were questions answered and/or relevant information/inventory pushed? - chat5',
                       'Were questions answered and/or relevant information/inventory pushed? - chat6',

                       'Was the appropriate lead generation used, and at the right time? - chat1',
                       'Was the appropriate lead generation used, and at the right time? - chat2',
                       'Was the appropriate lead generation used, and at the right time? - chat3',
                       'Was the appropriate lead generation used, and at the right time? - chat4',
                       'Was the appropriate lead generation used, and at the right time? - chat5',
                       'Was the appropriate lead generation used, and at the right time? - chat6',

                       'Did the lead generation encompass all of the guests needs? - chat1',
                       'Did the lead generation encompass all of the guests needs? - chat2',
                       'Did the lead generation encompass all of the guests needs? - chat3',
                       'Did the lead generation encompass all of the guests needs? - chat4',
                       'Did the lead generation encompass all of the guests needs? - chat5',
                       'Did the lead generation encompass all of the guests needs? - chat6',

                       'Did the customer provide all contact information OR was missing information properly gathered? - chat1',
                       'Did the customer provide all contact information OR was missing information properly gathered? - chat2',
                       'Did the customer provide all contact information OR was missing information properly gathered? - chat3',
                       'Did the customer provide all contact information OR was missing information properly gathered? - chat4',
                       'Did the customer provide all contact information OR was missing information properly gathered? - chat5',
                       'Did the customer provide all contact information OR was missing information properly gathered? - chat6',

                       'Was the chat properly recapped/ended? - chat1',
                       'Was the chat properly recapped/ended? - chat2',
                       'Was the chat properly recapped/ended? - chat3',
                       'Was the chat properly recapped/ended? - chat4',
                       'Was the chat properly recapped/ended? - chat5',
                       'Was the chat properly recapped/ended? - chat6',

                       'Was it sent to the correct department? If PSA, was it dispositioned correctly? - chat1',
                       'Was it sent to the correct department? If PSA, was it dispositioned correctly? - chat2',
                       'Was it sent to the correct department? If PSA, was it dispositioned correctly? - chat3',
                       'Was it sent to the correct department? If PSA, was it dispositioned correctly? - chat4',
                       'Was it sent to the correct department? If PSA, was it dispositioned correctly? - chat5',
                       'Was it sent to the correct department? If PSA, was it dispositioned correctly? - chat6',

                       'Was everything within the lead filled out properly? - chat1',
                       'Was everything within the lead filled out properly? - chat2',
                       'Was everything within the lead filled out properly? - chat3',
                       'Was everything within the lead filled out properly? - chat4',
                       'Was everything within the lead filled out properly? - chat5',
                       'Was everything within the lead filled out properly? - chat6',

                       'Greeting - chat1',
                       'Greeting - chat2',
                       'Greeting - chat3',
                       'Greeting - chat4',
                       'Greeting - chat5',
                       'Greeting - chat6',

                       'Responses - chat1',
                       'Responses - chat2',
                       'Responses - chat3',
                       'Responses - chat4',
                       'Responses - chat5',
                       'Responses - chat6',

                       'Sit Time - chat1',
                       'Sit Time - chat2',
                       'Sit Time - chat3',
                       'Sit Time - chat4',
                       'Sit Time - chat5',
                       'Sit Time - chat6',

                       'Were there less than 3 grammatical mistakes? - chat1',
                       'Were there less than 3 grammatical mistakes? - chat2',
                       'Were there less than 3 grammatical mistakes? - chat3',
                       'Were there less than 3 grammatical mistakes? - chat4',
                       'Were there less than 3 grammatical mistakes? - chat5',
                       'Were there less than 3 grammatical mistakes? - chat6',

                       'Was the guest satisfied with the way the operator handled the chat? - chat1',
                       'Was the guest satisfied with the way the operator handled the chat? - chat2',
                       'Was the guest satisfied with the way the operator handled the chat? - chat3',
                       'Was the guest satisfied with the way the operator handled the chat? - chat4',
                       'Was the guest satisfied with the way the operator handled the chat? - chat5',
                       'Was the guest satisfied with the way the operator handled the chat? - chat6',

                       'Auto-fail - chat1',
                       'Auto-fail - chat2',
                       'Auto-fail - chat3',
                       'Auto-fail - chat4',
                       'Auto-fail - chat5',
                       'Auto-fail - chat6',

                       'status', 'disput_status',
                       'closed_date', 'fatal', ]

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = GubagooAuditForm.objects.filter(
                audit_date__range=[start_date, end_date], ).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count',
                'qa', 'am', 'team_lead', 'manager',
                'chat1_id', 'chat2_id', 'chat3_id', 'chat4_id', 'chat5_id', 'chat6_id',
                'chat1_total_score', 'chat2_total_score', 'chat3_total_score', 'chat4_total_score', 'chat5_total_score',
                'chat6_total_score',

                'cat1chat1',
                'cat1chat2',
                'cat1chat3',
                'cat1chat4',
                'cat1chat5',
                'cat1chat6',

                'cat2chat1',
                'cat2chat2',
                'cat2chat3',
                'cat2chat4',
                'cat2chat5',
                'cat2chat6',

                'cat3chat1',
                'cat3chat2',
                'cat3chat3',
                'cat3chat4',
                'cat3chat5',
                'cat3chat6',

                'cat4chat1',
                'cat4chat2',
                'cat4chat3',
                'cat4chat4',
                'cat4chat5',
                'cat4chat6',

                'cat5chat1',
                'cat5chat2',
                'cat5chat3',
                'cat5chat4',
                'cat5chat5',
                'cat5chat6',

                'cat6chat1',
                'cat6chat2',
                'cat6chat3',
                'cat6chat4',
                'cat6chat5',
                'cat6chat6',

                'cat7chat1',
                'cat7chat2',
                'cat7chat3',
                'cat7chat4',
                'cat7chat5',
                'cat7chat6',

                'cat8chat1',
                'cat8chat2',
                'cat8chat3',
                'cat8chat4',
                'cat8chat5',
                'cat8chat6',

                'cat9chat1',
                'cat9chat2',
                'cat9chat3',
                'cat9chat4',
                'cat9chat5',
                'cat9chat6',

                'cat10chat1',
                'cat10chat2',
                'cat10chat3',
                'cat10chat4',
                'cat10chat5',
                'cat10chat6',

                'cat11chat1',
                'cat11chat2',
                'cat11chat3',
                'cat11chat4',
                'cat11chat5',
                'cat11chat6',

                'cat12chat1',
                'cat12chat2',
                'cat12chat3',
                'cat12chat4',
                'cat12chat5',
                'cat12chat6',

                'cat13chat1',
                'cat13chat2',
                'cat13chat3',
                'cat13chat4',
                'cat13chat5',
                'cat13chat6',

                'cat14chat1',
                'cat14chat2',
                'cat14chat3',
                'cat14chat4',
                'cat14chat5',
                'cat14chat6',

                'cat15chat1',
                'cat15chat2',
                'cat15chat3',
                'cat15chat4',
                'cat15chat5',
                'cat15chat6',

                'cat16chat1',
                'cat16chat2',
                'cat16chat3',
                'cat16chat4',
                'cat16chat5',
                'cat16chat6',

                'status', 'disput_status',
                'closed_date', 'fatal')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response

        elif campaign == "Nerotel Inbound":
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = ['Process', 'Employee ID', 'Associate Name',
                       'Quality Analyst', 'Team Lead', 'Assistant Manager', 'Manager', 'Customer Name',
                       'Customer Contact', 'Call Date', 'Audit Date', 'Zone', 'Concept', 'Call Duration',
                       'Week',

                       'Greeting?',
                       'Value Proposition? ',
                       'Tone and Pace?',
                       'Screening Questions?',
                       "How clear and concise was the rep's vocalization and pronunciation?",
                       'Did the rep use the correct hold procedure?',
                       'Providing Solutions?',
                       'Did the rep display active listening skills?',
                       'Call closure phase? Last Checks ?',

                       'Confirmation?',
                       'Preparation?',
                       'Clinic Procedures?',
                       'Did the rep manage time effectively?',

                       'Documentation?',
                       'Patient Details?',
                       'Discovery Questions? ',
                       'Was agent rude on the call',

                       'Status', 'Dispute Status',
                       'Closed Date', 'Fatal', 'Fatal Count', 'Overall Score', 'Areas of improvement', 'Positives',
                       'Comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = NerotelInboundmonform.objects.filter(audit_date__range=[start_date, end_date],
                                                        ).values_list(
                'process', 'emp_id', 'associate_name', 'qa', 'team_lead',
                'am', 'manager', 'customer_name', 'customer_contact',
                'call_date',
                'audit_date', 'zone', 'concept', 'call_duration', 'week',

                'eng_1', 'eng_2', 'eng_3', 'eng_4', 'eng_5', 'eng_6', 'eng_7', 'eng_8', 'eng_9',

                'res_1', 'res_2', 'res_3', 'res_4',

                'compliance_1', 'compliance_2', 'compliance_3', 'compliance_4',

                'status', 'disput_status',
                'closed_date', 'fatal', 'fatal_count', 'overall_score', 'areas_improvement', 'positives', 'comments')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response

        elif campaign == "Spoiled Child":
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = ['Process', 'Employee ID', 'Associate Name', 'Zone', 'Concept', 'Customer Name', 'Ticket ID',
                       'Qurey Tpe', 'Chat Date', 'Audit Date', 'Quality Analyst', 'Team Lead', 'Manager',
                       'Assistant Manager',
                       'Week', 'Campaign',

                       "Understanding and Solved Customer's Issue?",
                       "Gave alternatives when required/applicable & displayed expert product knowledge?",
                       "Coupon code added/Edited Name/Values & Date//Personalized when applicable?",
                       "Answered all question effectively?",

                       "Resolved issue in a timely manner?",
                       "Categorized case properly/Check other Tickets &Previous commination Merged?",

                       "Appropriate use of macros?",
                       "Magento was utilized correctly?",
                       "Identified correct order type?",

                       "Solution Total", "Efficiency Total", "Compliance Total", "Total Score",

                       'Fatal', 'Fatal Count', 'Dispute Status', 'Status',
                       'Closed Date', 'Areas of improvement', 'Positives', 'Comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = SpoiledChildChatmonform.objects.filter(audit_date__range=[start_date, end_date],
                                                          ).values_list(
                'process', 'emp_id', 'associate_name', 'zone', 'concept', 'customer_name', 'ticket_id', 'query_type',
                'chat_date', 'audit_date', 'qa', 'team_lead', 'manager', 'am', 'week', 'campaign',

                'solution_1', 'solution_2', 'solution_3', 'solution_4',

                'efficiency_1', 'efficiency_2',

                'compliance_1', 'compliance_2', 'compliance_3',

                "solution_total", "efficiency_total", "compliance_total", "overall_score",

                'fatal', 'fatal_count', 'disput_status', 'status', 'closed_date', 'areas_improvement', 'positives',
                'comments', )

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response

        elif campaign == "Amerisave":
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = ['Process', 'Employee ID', 'Associate Name', 'Type', 'Lead Source', 'Customer ID',
                       'Transfer/Non-transfer', 'Call Date', 'Audit Date', 'Quality Analyst', 'Team Lead', 'Manager',
                       'Assistant Manager', 'Week',

                       "Did CSS adhere to the script associated with the lead source?",
                       "What was the consumer's main objection?",
                       "Did CSS attempt to overcome objections?",
                       "Transfer Only: Did CSS properly transfer the customer to sales?",

                       "Did CSS disposition call correctly?",
                       "CSS Full Name",
                       "AmeriSave Mortgage Corporation",
                       "Recorded Line",
                       "Pre-qualified for a loan with AMC",
                       "Did CSS read Fine Print verbatim and completely?",

                       "If Fail, Which Type",
                       "Total Score",

                       'Fatal', 'Fatal Count', 'Dispute Status', 'Status',
                       'Closed Date', 'Areas of improvement', 'Positives', 'Comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = AmerisaveMonForm.objects.filter(audit_date__range=[start_date, end_date],
                                                   ).values_list(
                'process', 'emp_id', 'associate_name', 'category', 'lead_source', 'customer_id',
                'transfer', 'call_date', 'audit_date', 'qa', 'team_lead', 'manager',
                'am', 'week',

                "nce_1",
                "nce_2",
                "nce_3",
                "nce_4",

                "compliance_1",
                "compliance_2",
                "compliance_3",
                "compliance_4",
                "compliance_5",
                "compliance_6",

                "fail_type",
                "overall_score",

                'fatal', 'fatal_count', 'disput_status', 'status',
                'closed_date', 'areas_improvement', 'positives', 'comments')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response


        elif campaign == "Movement Insurance":
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = [
                'process', 'type', 'emp_id', 'associate_name', 'qa', 'team_lead', 'am', 'week', 'audit_date', 'form_id',
                'customer_name', 'case_id', 'transaction_date', 'zone', 'lob', 'concept', 'manager'
                'category', 'q_1', 'areas_improvement', 'positives', 'comments', 'added_by', 'status', 'closed_date',
                'emp_comments', 'overall_score', 'fatal', 'fatal_count', 'disput_status'
            ]

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = MovementInsuranceMonForm.objects.filter(audit_date__range=[start_date, end_date],
                                                   ).values_list(
                'process', 'type', 'emp_id', 'associate_name', 'qa', 'team_lead', 'am', 'week', 'audit_date',
                'form_id', 'customer_name', 'case_id', 'transaction_date', 'zone', 'lob', 'concept', 'manager',
                'category', 'q_1', 'areas_improvement', 'positives', 'comments', 'added_by', 'status',
                'closed_date', 'emp_comments', 'overall_score', 'fatal', 'fatal_count', 'disput_status')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response


        elif campaign == "Brightway":
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = [
                'process', 'type', 'emp_id', 'associate_name', 'fws_id', 'qa', 'team_lead', 'audit_date', 'policy_no',
                'place', 'policy_type', 'case_status', 'case_date', 'manager', 'manager_id', 'category',
                'q_1', 'q_2', 'q_3', 'q_4',
                'areas_improvement', 'positives', 'comments', 'added_by', 'status', 'closed_date', 'emp_comments',
                'overall_score', 'am', 'week', 'fatal', 'fatal_count', 'dispute_status'
            ]

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = BrightwayMonForm.objects.filter(audit_date__range=[start_date, end_date],
                                                   ).values_list(
                'process', 'type', 'emp_id', 'associate_name', 'fws_id', 'qa', 'team_lead', 'audit_date', 'policy_no',
                'place', 'policy_type', 'case_status', 'case_date', 'manager', 'manager_id', 'category',
                'q_1', 'q_2', 'q_3', 'q_4',
                'areas_improvement', 'positives', 'comments', 'added_by', 'status', 'closed_date', 'emp_comments',
                'overall_score', 'am', 'week', 'fatal', 'fatal_count', 'disput_status')

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
                       'qa', 'am', 'team_lead', 'manager', 'customer_name', 'customer_contact', 'zone', 'concept',

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
                'team_lead', 'manager', 'customer_name', 'customer_contact', 'zone', 'concept',

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

        #######  OUTBOUND  ###########

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

        elif campaign == 'Clean-Living Health and Wellness':
            response = exportAadyaseries(CleanLivingHealthWellnessOutboundMonForm)
            return response

        elif campaign == 'Practo Outbound':
            response = exportAadyaseries(PractoOutboundMonForm)
            return response

        elif campaign == 'Imaginarium Outbound':
            response = exportAadyaseries(ImaginariumOutboundMonForm)
            return response

        elif campaign == 'US Jaclean Outbound':
            response = exportAadyaseries(USJacleanOutboundForm)
            return response

        elif campaign == 'Global Galaxy Outbound':
            response = exportAadyaseries(GlobalGalaxyOutboundForm)
            return response

        elif campaign == 'Community Health Project Inc':
            response = exportAadyaseries(CommunityHealthProjectIncOutbound)
            return response

        elif campaign == 'Educated Analytics LLC':
            response = exportAadyaseries(EducatedAnalyticsLLCOutbound)
            return response

        elif campaign == 'New Dimension Pharmacy':
            response = exportAadyaseries(NewDimensionPharmacyOutbound)
            return response

        elif campaign == 'Stay-N-Charge':
            response = exportAadyaseries(StayNChargeOutbound)
            return response

        elif campaign == 'J & H Energy Consultant':
            response = exportAadyaseries(JHEnergyConsultantOutbound)
            return response

        elif campaign == 'MDR Group LLC':
            response = exportAadyaseries(MDRGroupLLCOutbound)
            return response

        elif campaign == 'Corey Small Insurance Agency Inc':
            response = exportAadyaseries(CoreySmallInsuranceAgencyOutbound)
            return response

        elif campaign == 'Eduvocate Outbound':
            response = exportAadyaseries(EduvocateOutbound)
            return response

        elif campaign == 'Cross Tower Outbound':
            response = exportAadyaseries(CrossTowerOutbound)
            return response

        elif campaign == 'Dawn Financial Outbound':
            response = exportAadyaseries(DawnFinancialOutbound)
            return response

        elif campaign == 'Xport Digital Outbound':
            response = exportAadyaseries(XportDigitalOutbound)
            return response

        elif campaign == 'Calista Outbound':
            response = exportAadyaseries(CalistaOutboundMonForm)
            return response

        elif campaign == 'Global Ark Outbound':
            response = exportAadyaseries(GlobalArkOutboundMonform)
            return response

        elif campaign == 'DI Develop Outbound':
            response = exportAadyaseries(DIDevelopOutbound)
            return response

        elif campaign == 'Freehold Outbound':
            response = exportAadyaseries(FreeholdOutboundMonForm)
            return response

        elif campaign == 'Zeamo Outbound':
            response = exportAadyaseries(ZeamoOutboundMonForm)
            return response

        elif campaign == 'Sapphire Medicals Outbound':
            response = exportAadyaseries(SapphireMedicalsOutboundMonForm)
            return response

        elif campaign == 'Eehhaaa Outbound':
            response = exportAadyaseries(EehhaaaOutboundMonForm)
            return response

        elif campaign == 'All Care Physical Therapy':
            response = exportAadyaseries(AllCarePhysicalTherapyMonform)
            return response

        elif campaign == 'Executive Capital Resources':
            response = exportAadyaseries(ExecutiveCapitalResourcesmonform)
            return response

        elif campaign == 'Bright Way Outbound':
            response = exportAadyaseries(BrightWayOutboundmonform)
            return response

        elif campaign == 'Building lab LLC Outbound':
            response = exportAadyaseries(BuildinglabLLCOutboundmonform)
            return response

        elif campaign == 'Global Pharma Outbound':
            response = exportAadyaseries(GlobalPharmaOutboundmonform)
            return response

        elif campaign == 'Redefine Plastics Outbound':
            response = exportAadyaseries(RedefinePlasticsOutboundmonform)
            return response

        elif campaign == 'Hard Hat Technologies Outbound':
            response = exportAadyaseries(HardHatTechnologiesOutboundmonform)
            return response

        elif campaign == '3rd Wave Outbound':
            response = exportAadyaseries(ThirdWaveOutboundmonform)
            return response

        elif campaign == 'K7 Outbound':
            response = exportAadyaseries(K7Outboundmonform)
            return response

        elif campaign == 'Trial Mapping Outbound':
            response = exportAadyaseries(TrialMappingOutboundmonform)
            return response

        elif campaign == 'Edu Class Outbound':
            response = exportAadyaseries(EduClassOutboundmonform)
            return response

        elif campaign == 'Cred Avenue Outbound':
            response = exportAadyaseries(CredAvenueOutboundmonform)
            return response

        elif campaign == 'TKAWDIW Outbound':
            response = exportAadyaseries(TKAWDIWOutboundmonform)
            return response

        elif campaign == 'Dream Pick Outbound':
            response = exportAadyaseries(DreamPickOutboundmonform)
            return response

        elif campaign == 'Kheloyar Outbound':
            response = exportAadyaseries(KheloyarOutboundmonform)
            return response

        elif campaign == 'Mex Trading Outbound':
            response = exportAadyaseries(MaxTradingOutboundmonform)
            return response

        elif campaign == 'ESR TechTalent Outbound':
            response = exportAadyaseries(ESRTechTalentOutboundmonform)
            return response

        elif campaign == 'Green Connect Outbound':
            response = exportAadyaseries(GreenConnectOutboundmonform)
            return response

        elif campaign == 'Central Mortgage Funding':
            response = exportAadyaseries(CentralMortgageFundingOutboundmonform)
            return response

        elif campaign == 'Rapid Mortgage':
            response = exportAadyaseries(RapidMortgageOutboundmonform)
            return response

        elif campaign == 'Bridan & Associates Outbound':
            response = exportAadyaseries(BridanAssociatesOutboundmonform)
            return response

        elif campaign == 'Linen Finder Outbound':
            response = exportAadyaseries(LinenFinderOutboundmonform)
            return response

        elif campaign == 'Better Ed Outbound':
            response = exportAadyaseries(BetterEdOutboundmonform)
            return response

        elif campaign == 'Com 98 Outbound':
            response = exportAadyaseries(Com98Outboundmonform)
            return response

        elif campaign == 'Gretna Medical Centre Outbound':
            response = exportAadyaseries(GretnaMedicalCentreOutboundmonform)
            return response

        elif campaign == 'Arista MD Outbound':
            response = exportAadyaseries(AristaMDOutboundmonform)
            return response

        elif campaign == 'Robert Damon Production Outbound':
            response = exportAadyaseries(RobertDamonProductionOutboundmonform)
            return response

        elif campaign == 'Venwiz Outbound':
            response = exportAadyaseries(VenwizOutboundmonform)
            return response

        elif campaign == 'City Habitat Outbound':
            response = exportAadyaseries(CityHabitatOutboundmonform)
            return response

        elif campaign == 'Optel Outbound':
            response = exportAadyaseries(OptelOutboundmonform)
            return response


        elif campaign == 'South County Outbound':
            response = exportAadyaseries(SouthCountyOutboundMonForm)
            return response

        elif campaign == 'Inpress Outbound':
            response = exportAadyaseries(InpressOutboundMonForm)
            return response

        elif campaign == 'L & M Enterprises Outbound':
            response = exportAadyaseries(LMEnterprisesOutboundMonForm)
            return response

        elif campaign == 'Towers Traders Group Outbound':
            response = exportAadyaseries(TowersTradersGroupOutboundMonForm)
            return response

        elif campaign == 'Job E Roofing Outbound':
            response = exportAadyaseries(JobERoofingOutboundMonForm)
            return response

        elif campaign == 'TravelWholesale Outbound':
            response = exportAadyaseries(TravelWholesaleOutboundMonForm)
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
                       'qa', 'am', 'team_lead', 'manager', 'customer_name', 'customer_contact', 'zone', 'concept',

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
                'team_lead', 'manager', 'customer_name', 'customer_contact', 'zone', 'concept',

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

        elif campaign == 'LJ Hub Inbound':
            response = exportinbound(LJHubInboundMonForms)
            return response

        elif campaign == 'Obthera Inc':
            response = exportinbound(ObtheraIncInboundMonForms)
            return response

        elif campaign == 'Eduvocate Inbound':
            response = exportinbound(EduvocateInboundMonForms)
            return response

        elif campaign == 'Cross Tower Inbound':
            response = exportinbound(CrossTowerInboundMonForms)
            return response

        elif campaign == 'Sana Life Science Inbound':
            response = exportinbound(SanaLifeScienceInbound)
            return response

        elif campaign == 'Mobile 22 Inbound':
            response = exportinbound(MonitoringFormMobile22InboundCalls)
            return response

        elif campaign == 'Xport Digital Inbound':
            response = exportinbound(XportDigitalInboundMonForm)
            return response

        elif campaign == 'Calista Inbound':
            response = exportinbound(CalistaInboundMonForm)
            return response

        elif campaign == 'Global Ark Inbound':
            response = exportinbound(GlobalArkInboundMonForm)
            return response

        elif campaign == '3rd Wave Inbound':
            response = exportinbound(ThirdWaveInboundMonForm)
            return response

        elif campaign == 'Hard Hat Technologies Inbound':
            response = exportinbound(HardHatTechnologiesInboundMonForm)
            return response

        elif campaign == 'Gretna Medical Center Inbound':
            response = exportinbound(GretnaMedicalCenterInboundMonForm)
            return response

        elif campaign == 'Better Ed Inbound':
            response = exportinbound(BetterEdInboundMonForm)
            return response

        elif campaign == 'Com 98 Inbound':
            response = exportinbound(Com98InboundMonForm)
            return response

        elif campaign == 'Open Winds Inbound':
            response = exportinbound(OpenWindsInboundMonForm)
            return response

        elif campaign == 'Embassy Luxury Inbound':
            response = exportinbound(EmbassyLuxuryInboundMonForm)
            return response

        elif campaign == 'South County Inbound':
            response = exportinbound(SouthCountyInboundMonForm)
            return response

        elif campaign == 'City Habitat Inbound':
            response = exportinbound(CityHabitatInboundMonForm)
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
                       'qa', 'am', 'team_lead', 'manager', 'customer_name', 'customer_contact',

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
                'team_lead', 'manager', 'customer_name', 'customer_contact',

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

        elif campaign == 'Finesse Mortgage Email':
            response = exportEmailChat(FinesseMortgageEmailMonForm)
            return response
        elif campaign == 'Fur Baby':
            response = exportEmailChat(FurBabyMonForm)
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

        elif campaign == 'US Jaclean Email Chat':
            response = exportEmailChat(USJacleanEmailChatForm)
            return response

        elif campaign == 'Cross Tower Email-Chat':
            response = exportEmailChat(CrossTowerEmailChatForm)
            return response

        elif campaign == 'Sana Life Science Email-Chat':
            response = exportEmailChat(SanaLifeScienceEmailChatForm)
            return response

        elif campaign == 'Bhagyalaxmi Chat':
            response = exportEmailChat(BhagyalaxmiChatMonForm)
            return response

        elif campaign == 'Sapphire Medicals Chat':
            response = exportEmailChat(SapphireMedicalsChatMonForm)
            return response

        elif campaign == 'Gretna Medical Center Email':
            response = exportEmailChat(GretnaMedicalCenterEmailChatForm)
            return response

        elif campaign == 'Jump Rydes Email - Chat':
            response = exportEmailChat(JumpRydesEmailChatForm)
            return response

        elif campaign == 'Naffa Innovation Email - Chat':
            response = exportEmailChat(NaffaInnovationEmailChatForm)
            return response

        elif campaign == 'Inpress Email - Chat':
            response = exportEmailChat(InpressEmailChatForm)
            return response

            ########## other campaigns ##############

        elif campaign == 'Blazing Hog':
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
                       'qa', 'am', 'team_lead', 'manager', 'customer_name', 'ticket_id', 'zone', 'concept',
                       'query_type',

                       "Understanding and Solved Customer's Issue",
                       "Displayed process knowledge",
                       'Documentation - Full information captured in internal spreadsheet',
                       'Did the agent mention correct and adequate notes if necessary',

                       'Resolved/Assigned Ticket issue in a timely manner',
                       'Categorized case properly/Check other Tickets & Previous communition Merged',

                       'Assigned to the correct department',
                       'Tool usage',
                       'Edited Customer profile/Check customer profile',

                       'status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = BlazingHogEmailChatmonform.objects.filter(audit_date__range=[start_date, end_date], qa=qa
                                                             ).values_list(
                'process', 'emp_id', 'associate_name', 'call_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager', 'customer_name', 'ticket_id', 'zone', 'concept', 'query_type',

                'solution_1',
                'solution_2',
                'solution_3',
                'solution_4',

                'efficiency_1',
                'efficiency_2',

                'compliance_1',
                'compliance_2',
                'compliance_3',

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

        elif campaign == 'AB Hindalco':
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
                       'qa', 'am', 'team_lead', 'manager', 'customer_name', 'customer_contact', 'zone', 'concept',

                       'Used Standard Opening Protocol',
                       'Introduction of Product / Branding - 4 USP of eternia - WiWA, Warranty, Duranium, Eternia care Mentioning Hindalco, Aditya birla group',
                       'Call Closing as per the Protocol',

                       'Used Empathetic Statements whenever required',
                       'Making the conversation 2 ways, giving chance to the customer to ask question',
                       'Active Listening without Interruption',

                       'Followed Policy & Procedure (Script)',
                       'Accurate Documentation with full details in ZOHO',
                       'Inaccurate Information : Identifying the right lead to opportunity',
                       'Advisor Sounding Rude / Proafinity Usage',

                       'status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = ABHindalcoMonForm.objects.filter(audit_date__range=[start_date, end_date], qa=qa
                                                    ).values_list(
                'process', 'emp_id', 'associate_name', 'call_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager', 'customer_name', 'customer_contact', 'zone', 'concept',

                'oc_1',
                'oc_2',
                'oc_3',

                'softskill_1',
                'softskill_2',
                'softskill_3',

                'compliance_1',
                'compliance_2',
                'compliance_3',
                'compliance_4',

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

        elif campaign == 'Winopoly Outbound':
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

                       'Recording Disclosure - (Agent must disclose the call is recorded)',
                       'Rep Name - (Did agent introduce her/himself during opening?)',
                       'Branding/Site Name - (Did the agent state the site name name in the opening?)',
                       'Call Reason - (Did the agent state the reason for the call? (confirmation call))',
                       'Contact Information - (Did the agent verify the contact info?)',

                       'Targeted Spotlight offer - (Did the agent attempt the Targeted spotlight offer?)',
                       'Lead offer - (Did the agent attempt the lead offer?)',
                       'Verification - (Did the agent ask all verification questions were applicaple?)',

                       'Excessisive off topic conversations - (Did the agent avoid unnessesary off topic conversations)',
                       'Polite - (Follow up done on the Pending Tickets (Chats & Email))',
                       'Positive and Upbeat - (Did the agent have a positive and upbeat tone)',
                       'Ethics - (Did the agent advoid misleading information about offers)',
                       'Call control - (Did the agent take control of the call)',
                       'Program of Interest - (Did the agent match the lead to a program that they stated interest in, without having to push the lead into agreeing to the program?)',

                       'TCPA Close - (Did the rep read a TCPA statement and receive an affirmative response from the lead (Yes or Yeah)?)',
                       'TCPA Close - (If interrupted did the agent reread the TCPA and get an affimative response)',
                       'Do Not Call Request - (Agent followed DNC Request Policy)',
                       'California Privacy Policy - (Agent followed CA Policy Privacy by reading the written statement for CA residents)',
                       'Transfering the call - (Did the agent conduct the intro on the transfer correctly?)',
                       'Transfer Only - (Did the agent conduct the intro on the transfer correctly)',
                       'Disposition - (Did the agent used the correct disposition?)',
                       'Auto Fail - (ZERO TOLERANCE POLICY)',
                       'status', 'disput_status',
                       'closed_date', 'fatal', 'coaching_comments', 'evaluator_comment']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = WinopolyOutbound.objects.filter(
                audit_date__range=[start_date, end_date], qa=qa).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager', 'customer_name', 'customer_contact',

                'comp_1',
                'op_2',
                'op_3',
                'op_4',
                'op_5',

                'mp_1',
                'mp_2',
                'mp_3',

                'cp_1',
                'cp_2',
                'cp_3',
                'cp_4',
                'cp_5',
                'cp_6',

                'comp_2',
                'comp_3',
                'comp_4',
                'comp_5',

                'tp_1',
                'tp_2',
                'tp_3',
                'comp_6',

                'status', 'disput_status', 'closed_date', 'fatal', 'evaluator_comment', 'coaching_comments')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response

        elif campaign == 'Digital Swiss Gold Email - Chat':
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
                       'Follow up done on the Pending Tickets (Chats & Email)',
                       'Refund / Retruns / Escalation Updated in the google sheet',
                       'Process & Procedure Followed',
                       'First Chat / Email Resolution',

                       'status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = DigitalSwissGoldEmailChatMonForm.objects.filter(
                audit_date__range=[start_date, end_date], qa=qa).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager', 'customer_name', 'customer_contact',

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

        elif campaign == 'IL Makiage':

            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = ['process', 'empID', 'Associate Name', 'Email/chat date', 'Audit Date', 'overall_score',
                       'Fatal Count',
                       'qa', 'am', 'team_lead', 'manager', 'customer_name', 'ticket_id', 'Query Type',

                       "Understanding and Solved Customer's Issue",
                       'Gave alternatives when required/applicable & Displayed expert product knowledge',
                       'Coupon code added/Edited Name/Values & Date//Personalised when applicable',
                       'Answered all question effectively',
                       'Resolved issue in a timely manner',
                       'Categorized case properly/Check other Tickets &Previous communition Merged',
                       'Appropriate use of macros',
                       'Magento was utilized correctly',
                       'Identified correct order type',

                       'status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = ILMakiageEmailChatForm.objects.filter(
                audit_date__range=[start_date, end_date], qa=qa).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager', 'customer_name', 'ticket_id', 'query_type',

                's_1',
                's_2',
                's_3',
                's_4',

                'e_1',
                'e_2',

                'compliance_1',
                'compliance_2',
                'compliance_3',

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
                       'Shipping product incorrectly',
                       'Incorrect grammar and spelling being used/illegible responses/Does not make sense.',
                       'Blatantly incorrect or made up information provided to the customer',
                       'Sending internal notes as Public response',
                       'Responding to any ticket outside of representatives skills/assignments',
                       'Unprofessional- tone,language or content. Uses derogatory language or curse words.',
                       'Not escalating a situation/Not following proper escalation procedure/Responding to an escalated ticket',
                       'Responding to Spam',
                       'Double response-w/o addressing and apologizing',
                       'Responding with personal opinions outside of company policy',
                       'Sending same macro as last agent w/o edits.',

                       'Agent sent response as public reply',

                       'Agent greeted customer by correct name',
                       'Agent used correct appreciation/acknowledgement statement',

                       'Agent composed email with logical flow that makes sense',
                       'Agent presented information with clear formatting, correct spelling and grammar',

                       'Agent chose correct macro(s).',
                       "Agent tailored macro(s) to fit the customer's question or issue",

                       'Agent asked the customer if he/she could be of additional help',
                       'Agent used appropriate closing & signature',

                       'Agent correctly identified and understood customer issue and responded accordingly (Issue Identification)',
                       'Agent fully resolved inquiry/issue upon first contact when possible, or clearly communicated additional information/next steps for full resolution. (Issue Resolution)',
                       'Agent did not deflect any questions/avoid policy communications unnecessarily. (Non-avoidance)',
                       'Agent conveyed correct policy information to the customer',
                       'Agent conveyed correct product information to the customer',
                       'Agent established correct timeline to resolution/ CSR did not delay resolution. (Resolution Timeline)',
                       'Rep fully and accurately helped the customer within their empowerments or escalated appropriately. (Agent Empowerments)',

                       "Agent validated the customer's concern / questions / reason for contacting us",
                       "Agent offered genuine acknowledgement and empathy for customer's concern",
                       'Agent used positive tone and impartial language in all communications',
                       'Agent was professional and courteous',
                       "Representative answered in a tone consistent with UMG's core values and culture",

                       'Agent accurately completed all necessary field on the ticket',
                       'Agent merged tickets properly',
                       'Agent performed all needed Shopify processes and accurately relayed all needed information and screenshots to customer.',
                       'Agent completed all system processes correctly',
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
                'compliance_7',
                'compliance_8',
                'compliance_9',
                'compliance_10',
                'compliance_11',

                'cr_1',

                'opening_1',
                'opening_2',

                'comp_1',
                'comp_2',

                'macro_1',
                'macro_2',

                'closing_1',
                'closing_2',

                'cir_1',
                'cir_2',
                'cir_3',
                'cir_4',
                'cir_5',
                'cir_6',
                'cir_7',

                'et_1',
                'et_2',
                'et_3',
                'et_4',
                'et_5',

                'doc_1',
                'doc_2',
                'doc_3',
                'doc_4',

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

                       'If the user is missed to hit "finish" after sending the respective response. If the response is added with unwanted space and Punctuation. If the user name is miss-spelled/alphanumeric name on dashboard,we should use ???Hey there!???.',
                       'If the "You last checked in" user is not sent with respective message or sent twice with the response',
                       'If the user are not assigned in spreadsheet. Ex: If the user code is not added in the spreadsheet.',
                       'If "was assigned to you" users are not hit finish',

                       "If a user's query is missed to answer and directly assigned to GS.",
                       'If the user is directly assigned without an Acknowledgement. If the user is sent with irrelevant response. If user is missed to assign to a coach while user wish to be assigned',
                       'If the response is sent with any irrelevant words or free handed messages. If the task is popped up as UU and YLCI the UU task should be our first priority',
                       'If the user has a System generated message of cancellation and CRO assigned to next GS. Negative empathy for user???s message!',
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

                       'If the user is missed to hit "finish" after sending the respective response. If the response is added with unwanted space and Punctuation. If the user name is miss-spelled/alphanumeric name on dashboard,we should use ???Hey there!???.',
                       'If the "You last checked in" user is not sent with respective message or sent twice with the response',
                       'If the user are not assigned in spreadsheet. Ex: If the user code is not added in the spreadsheet.',
                       'If "was assigned to you" users are not hit finish',

                       "If a user's query is missed to answer and directly assigned to GS.",
                       'If the user is directly assigned without an Acknowledgement. If the user is sent with irrelevant response. If user is missed to assign to a coach while user wish to be assigned',
                       'If the response is sent with any irrelevant words or free handed messages. If the task is popped up as UU and YLCI the UU task should be our first priority',
                       'If the user has a System generated message of cancellation and CRO assigned to next GS. Negative empathy for user???s message!',
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

        ######### Practo New Version #########################################
        elif campaign == 'Practo':

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
                       'qa', 'am', 'team_lead', 'manager', 'conversation_id', 'customer_contact', 'training',

                       'Chat Opening (Greetings & being attentive) & Closing',
                       'FRTAT',
                       'Addressing the user/Personalisation of chat',
                       'Assurance & Acknowledgement',
                       'Coherence (understanding the issue) being attentive on chat.',
                       'Probing',
                       'Interaction: Empathy , Profressional, care',
                       'Grammar:',
                       'Relavant responses',
                       'Being courteous & using plesantries',
                       'Process followed',
                       'Explanation skills (Reasoning) & Rebuttal Handling',
                       'Sharing the information in a sequential manner',
                       'Case Documentation',
                       'Curation',
                       'Average speed of answer',
                       'Chat Hold Procedure &: Taking Perrmission before putting the chat on hold',
                       'Expectations: Setting correct expectations about issue resolution',
                       'ZTP(Zero Tolerance Policy)',

                       'status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = PractoNewVersion.objects.filter(
                audit_date__range=[start_date, end_date], qa=qa).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager', 'conversation_id', 'customer_contact', 'training',
                'p_1',
                'p_2',
                'p_3',
                'p_4',
                'p_5',
                'p_6',
                'p_7',
                'p_8',
                'p_9',
                'p_10',
                'p_11',
                'p_12',
                'p_13',
                'p_14',
                'p_15',
                'p_16',
                'p_17',
                'compliance_1',
                'compliance_2',

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

        # practo chat
        elif campaign == 'Practo Chat':
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = ['process', 'empID', 'Associate Name', 'Chat date',
                       'Case Number',
                       'Issue Type',
                       'Sub-Issue Type',
                       'Sub Sub-Issue Type',
                       'CSAT',
                       'Product',
                       'Audit Date', 'overall_score',
                       'Fatal Count',
                       'qa', 'am', 'team_lead', 'manager',

                       'Chat Closing',
                       "Failed to close the chat",
                       "Failed to use the standard script (survey)",
                       "Multiple closing statement used",
                       "Failed to offer further assistance",
                       "User ended the chat",
                       "NA",

                       'FRTAT',

                       'Addressing User/Personalization of Chat',
                       "No Attempt",
                       "First name used on the chat",
                       "Less attempt - More scope",
                       "Failed to probe the user name",
                       "Incorrect Salutation",
                       "NA",

                       'Assistance & Acknowledgement',
                       "Failed to acknowledge",
                       "Incomplete acknowledgment",
                       "Failed to do throughout the chat",
                       "Incorrect assistance statement",
                       "NA",

                       'Relevant responses',

                       'Assurance',

                       'Probing',
                       "Irrelevant Probing",
                       "Incomplete Probing",
                       "Didn't Attempt to Probe",
                       "NA",

                       'Interaction: Empathy & Care, Professionalism',
                       "No Empathy",
                       "Lack of Professionalism",
                       "Lack of Care",
                       "Lack of Empathy",
                       "Inappropriate empathy",
                       'Repetitive empathy statement',
                       'NA',

                       'Grammar:',
                       "Punctuation",
                       "Capitalization",
                       "Typing Error",
                       "Sentence Formation",
                       'Spacing',
                       "Spacing",

                       'Being Courteous & Using Pleasantries',

                       'Process followed',
                       "SOP has not followed",
                       "Incorrect Information",
                       "Incomplete Information",
                       "Failed to authenticate for the medicine order",
                       "Incorrect TAT (or) Failed to inform the TAT",
                       "Incomplete/Incorrect refund details and wrong redirection",
                       "NA",

                       'Explanation Skills (Being Specific, Reasoning) & Rebuttal Handling',

                       'Sharing the Information in Sequential Manner',

                       'Case Documentation',

                       'Curation',
                       "Incomplete",
                       "Inappropriate",
                       "NA",

                       'Average speed of answer',

                       'Chat Hold Procedure &: Taking Permission before putting the chat on hold',
                       "Standard script not used",
                       "Failed to refresh the chat within promised time.",
                       "Failed to retrieve the chat",
                       "NA",

                       'PE knowledge base adherence',
                       "Failed to refer the knowledge base",
                       "Referred, but not confident",
                       "Incorrect category referred by the agent",
                       "NA",

                       'Expectations: Setting Correct Expectations about Issue Resolution',
                       "Incomplete Resolution",
                       "Incorrect Resolution",
                       "Process breach",

                       'ZTP (Zero Tolerance Policy)',

                       'status', 'disput_status',
                       'closed_date', 'fatal',
                       'areas_improvement', 'Specific Reason for FATAL with Labels and Sub Label', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = NewPractoWithSubCategory.objects.filter(
                audit_date__range=[start_date, end_date], ).values_list(
                'process', 'emp_id', 'associate_name', 'chat_date',
                'case_no',
                'issue_type',
                'sub_issue',
                'sub_sub_issue',
                'csat',
                'product',
                'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager',
                'p_1',
                'p1_s1',
                'p1_s2',
                'p1_s3',
                'p1_s4',
                'p1_s5',
                'p1_s6',
                'p_2',
                'p_3',
                'p3_s1',
                'p3_s2',
                'p3_s3',
                'p3_s4',
                'p3_s5',
                'p3_s6',
                'p_4',
                'p4_s1',
                'p4_s2',
                'p4_s3',
                'p4_s4',
                'p4_s5',
                'p_5',
                'p_6',
                'p_7',
                'p7_s1',
                'p7_s2',
                'p7_s3',
                'p7_s4',
                'p_8',
                'p8_s1',
                'p8_s2',
                'p8_s3',
                'p8_s4',
                'p8_s5',
                'p8_s6',
                'p8_s7',
                'p_9',
                'p9_s1',
                'p9_s2',
                'p9_s3',
                'p9_s4',
                'p9_s5',
                'p9_s6',
                'p_10',
                'p_11',
                'p11_s1',
                'p11_s2',
                'p11_s3',
                'p11_s4',
                'p11_s5',
                'p11_s6',
                'p11_s7',
                'p_12',
                'p_13',
                'p_14',
                'p_15',
                'p15_s1',
                'p15_s2',
                'p15_s3',
                'p_16',
                'p_17',
                'p17_s1',
                'p17_s2',
                'p17_s3',
                'p17_s4',
                'p_18',
                'p18_s1',
                'p18_s2',
                'p18_s3',
                'p18_s4',
                'compliance_1',
                'compliance1_s1',
                'compliance1_s2',
                'compliance1_s3',
                'compliance_2',

                'status', 'disput_status',
                'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response

            ######### Gubagoo #########################################
        elif campaign == 'Gubagoo':

            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = ['process', 'empID', 'Associate Name', 'transaction date', 'Audit Date', 'overall_score',
                       'Fatal Count', 'qa', 'am', 'team_lead', 'manager',
                       'chat1_id', 'chat2_id', 'chat3_id', 'chat4_id', 'chat5_id', 'chat6_id',
                       'chat 1 score', 'chat 2 score', 'chat 3 score', 'chat 4 score', 'chat 5 score', 'chat 6 score',

                       'Was there a greeting? - chat1',
                       'Was there a greeting? - chat2',
                       'Was there a greeting? - chat3',
                       'Was there a greeting? - chat4',
                       'Was there a greeting? - chat5',
                       'Was there a greeting? - chat6',

                       'Proper greeting? - chat1',
                       'Proper greeting? - chat2',
                       'Proper greeting? - chat3',
                       'Proper greeting? - chat4',
                       'Proper greeting? - chat5',
                       'Proper greeting? - chat6',

                       'Did you ask all relevant questions? - chat1',
                       'Did you ask all relevant questions? - chat2',
                       'Did you ask all relevant questions? - chat3',
                       'Did you ask all relevant questions? - chat4',
                       'Did you ask all relevant questions? - chat5',
                       'Did you ask all relevant questions? - chat6',

                       'Were questions answered and/or relevant information/inventory pushed? - chat1',
                       'Were questions answered and/or relevant information/inventory pushed? - chat2',
                       'Were questions answered and/or relevant information/inventory pushed? - chat3',
                       'Were questions answered and/or relevant information/inventory pushed? - chat4',
                       'Were questions answered and/or relevant information/inventory pushed? - chat5',
                       'Were questions answered and/or relevant information/inventory pushed? - chat6',

                       'Was the appropriate lead generation used, and at the right time? - chat1',
                       'Was the appropriate lead generation used, and at the right time? - chat2',
                       'Was the appropriate lead generation used, and at the right time? - chat3',
                       'Was the appropriate lead generation used, and at the right time? - chat4',
                       'Was the appropriate lead generation used, and at the right time? - chat5',
                       'Was the appropriate lead generation used, and at the right time? - chat6',

                       'Did the lead generation encompass all of the guests needs? - chat1',
                       'Did the lead generation encompass all of the guests needs? - chat2',
                       'Did the lead generation encompass all of the guests needs? - chat3',
                       'Did the lead generation encompass all of the guests needs? - chat4',
                       'Did the lead generation encompass all of the guests needs? - chat5',
                       'Did the lead generation encompass all of the guests needs? - chat6',

                       'Did the customer provide all contact information OR was missing information properly gathered? - chat1',
                       'Did the customer provide all contact information OR was missing information properly gathered? - chat2',
                       'Did the customer provide all contact information OR was missing information properly gathered? - chat3',
                       'Did the customer provide all contact information OR was missing information properly gathered? - chat4',
                       'Did the customer provide all contact information OR was missing information properly gathered? - chat5',
                       'Did the customer provide all contact information OR was missing information properly gathered? - chat6',

                       'Was the chat properly recapped/ended? - chat1',
                       'Was the chat properly recapped/ended? - chat2',
                       'Was the chat properly recapped/ended? - chat3',
                       'Was the chat properly recapped/ended? - chat4',
                       'Was the chat properly recapped/ended? - chat5',
                       'Was the chat properly recapped/ended? - chat6',

                       'Was it sent to the correct department? If PSA, was it dispositioned correctly? - chat1',
                       'Was it sent to the correct department? If PSA, was it dispositioned correctly? - chat2',
                       'Was it sent to the correct department? If PSA, was it dispositioned correctly? - chat3',
                       'Was it sent to the correct department? If PSA, was it dispositioned correctly? - chat4',
                       'Was it sent to the correct department? If PSA, was it dispositioned correctly? - chat5',
                       'Was it sent to the correct department? If PSA, was it dispositioned correctly? - chat6',

                       'Was everything within the lead filled out properly? - chat1',
                       'Was everything within the lead filled out properly? - chat2',
                       'Was everything within the lead filled out properly? - chat3',
                       'Was everything within the lead filled out properly? - chat4',
                       'Was everything within the lead filled out properly? - chat5',
                       'Was everything within the lead filled out properly? - chat6',

                       'Greeting - chat1',
                       'Greeting - chat2',
                       'Greeting - chat3',
                       'Greeting - chat4',
                       'Greeting - chat5',
                       'Greeting - chat6',

                       'Responses - chat1',
                       'Responses - chat2',
                       'Responses - chat3',
                       'Responses - chat4',
                       'Responses - chat5',
                       'Responses - chat6',

                       'Sit Time - chat1',
                       'Sit Time - chat2',
                       'Sit Time - chat3',
                       'Sit Time - chat4',
                       'Sit Time - chat5',
                       'Sit Time - chat6',

                       'Were there less than 3 grammatical mistakes? - chat1',
                       'Were there less than 3 grammatical mistakes? - chat2',
                       'Were there less than 3 grammatical mistakes? - chat3',
                       'Were there less than 3 grammatical mistakes? - chat4',
                       'Were there less than 3 grammatical mistakes? - chat5',
                       'Were there less than 3 grammatical mistakes? - chat6',

                       'Was the guest satisfied with the way the operator handled the chat? - chat1',
                       'Was the guest satisfied with the way the operator handled the chat? - chat2',
                       'Was the guest satisfied with the way the operator handled the chat? - chat3',
                       'Was the guest satisfied with the way the operator handled the chat? - chat4',
                       'Was the guest satisfied with the way the operator handled the chat? - chat5',
                       'Was the guest satisfied with the way the operator handled the chat? - chat6',

                       'Auto-fail - chat1',
                       'Auto-fail - chat2',
                       'Auto-fail - chat3',
                       'Auto-fail - chat4',
                       'Auto-fail - chat5',
                       'Auto-fail - chat6',

                       'status',
                       'closed_date', 'fatal', ]

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = GubagooAuditForm.objects.filter(
                audit_date__range=[start_date, end_date], qa=qa).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count',
                'qa', 'am', 'team_lead', 'manager',
                'chat1_id', 'chat2_id', 'chat3_id', 'chat4_id', 'chat5_id', 'chat6_id',
                'chat1_total_score', 'chat2_total_score', 'chat3_total_score', 'chat4_total_score', 'chat5_total_score',
                'chat6_total_score',

                'cat1chat1',
                'cat1chat2',
                'cat1chat3',
                'cat1chat4',
                'cat1chat5',
                'cat1chat6',

                'cat2chat1',
                'cat2chat2',
                'cat2chat3',
                'cat2chat4',
                'cat2chat5',
                'cat2chat6',

                'cat3chat1',
                'cat3chat2',
                'cat3chat3',
                'cat3chat4',
                'cat3chat5',
                'cat3chat6',

                'cat4chat1',
                'cat4chat2',
                'cat4chat3',
                'cat4chat4',
                'cat4chat5',
                'cat4chat6',

                'cat5chat1',
                'cat5chat2',
                'cat5chat3',
                'cat5chat4',
                'cat5chat5',
                'cat5chat6',

                'cat6chat1',
                'cat6chat2',
                'cat6chat3',
                'cat6chat4',
                'cat6chat5',
                'cat6chat6',

                'cat7chat1',
                'cat7chat2',
                'cat7chat3',
                'cat7chat4',
                'cat7chat5',
                'cat7chat6',

                'cat8chat1',
                'cat8chat2',
                'cat8chat3',
                'cat8chat4',
                'cat8chat5',
                'cat8chat6',

                'cat9chat1',
                'cat9chat2',
                'cat9chat3',
                'cat9chat4',
                'cat9chat5',
                'cat9chat6',

                'cat10chat1',
                'cat10chat2',
                'cat10chat3',
                'cat10chat4',
                'cat10chat5',
                'cat10chat6',

                'cat11chat1',
                'cat11chat2',
                'cat11chat3',
                'cat11chat4',
                'cat11chat5',
                'cat11chat6',

                'cat12chat1',
                'cat12chat2',
                'cat12chat3',
                'cat12chat4',
                'cat12chat5',
                'cat12chat6',

                'cat13chat1',
                'cat13chat2',
                'cat13chat3',
                'cat13chat4',
                'cat13chat5',
                'cat13chat6',

                'cat14chat1',
                'cat14chat2',
                'cat14chat3',
                'cat14chat4',
                'cat14chat5',
                'cat14chat6',

                'cat15chat1',
                'cat15chat2',
                'cat15chat3',
                'cat15chat4',
                'cat15chat5',
                'cat15chat6',

                'cat16chat1',
                'cat16chat2',
                'cat16chat3',
                'cat16chat4',
                'cat16chat5',
                'cat16chat6',

                'status', 'closed_date', 'fatal')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response

        elif campaign == "Nerotel Inbound":
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = ['Process', 'Employee ID', 'Associate Name',
                       'Quality Analyst', 'Team Lead', 'Assistant Manager', 'Manager', 'Customer Name',
                       'Customer Contact', 'Call Date', 'Audit Date', 'Zone', 'Concept', 'Call Duration',
                       'Week',

                       'Greeting?',
                       'Value Proposition? ',
                       'Tone and Pace?',
                       'Screening Questions?',
                       "How clear and concise was the rep's vocalization and pronunciation?",
                       'Did the rep use the correct hold procedure?',
                       'Providing Solutions?',
                       'Did the rep display active listening skills?',
                       'Call closure phase? Last Checks ?',

                       'Confirmation?',
                       'Preparation?',
                       'Clinic Procedures?',
                       'Did the rep manage time effectively?',

                       'Documentation?',
                       'Patient Details?',
                       'Discovery Questions? ',
                       'Was agent rude on the call',

                       'Status', 'Dispute Status',
                       'Closed Date', 'Fatal', 'Fatal Count', 'Overall Score', 'Areas of improvement', 'Positives',
                       'Comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = NerotelInboundmonform.objects.filter(audit_date__range=[start_date, end_date], qa=qa
                                                        ).values_list(

                'process', 'emp_id', 'associate_name', 'qa', 'team_lead',
                'am', 'manager', 'customer_name', 'customer_contact',
                'call_date',
                'audit_date', 'zone', 'concept', 'call_duration', 'week',

                'eng_1', 'eng_2', 'eng_3', 'eng_4', 'eng_5', 'eng_6', 'eng_7', 'eng_8', 'eng_9',

                'res_1', 'res_2', 'res_3', 'res_4',

                'compliance_1', 'compliance_2', 'compliance_3', 'compliance_4',

                'status', 'disput_status',
                'closed_date', 'fatal', 'fatal_count', 'overall_score', 'areas_improvement', 'positives', 'comments')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response


        elif campaign == "Spoiled Child":
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = ['Process', 'Employee ID', 'Associate Name', 'Zone', 'Concept', 'Customer Name', 'Ticket ID',
                       'Qurey Tpe', 'Chat Date', 'Audit Date', 'Quality Analyst', 'Team Lead', 'Manager',
                       'Assistant Manager',
                       'Week', 'Campaign',

                       "Understanding and Solved Customer's Issue?",
                       "Gave alternatives when required/applicable & displayed expert product knowledge?",
                       "Coupon code added/Edited Name/Values & Date//Personalized when applicable?",
                       "Answered all question effectively?",

                       "Resolved issue in a timely manner?",
                       "Categorized case properly/Check other Tickets &Previous commination Merged?",

                       "Appropriate use of macros?",
                       "Magento was utilized correctly?",
                       "Identified correct order type?",

                       "Solution Total", "Efficiency Total", "Compliance Total", "Total Score",

                       'Fatal', 'Fatal Count', 'Dispute Status', 'Status',
                       'Closed Date', 'Areas of improvement', 'Positives', 'Comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = SpoiledChildChatmonform.objects.filter(audit_date__range=[start_date, end_date], qa=qa
                                                          ).values_list(

                'process', 'emp_id', 'associate_name', 'zone', 'concept', 'customer_name', 'ticket_id', 'query_type',
                'chat_date', 'audit_date', 'qa', 'team_lead', 'manager', 'am', 'week', 'campaign',

                'solution_1', 'solution_2', 'solution_3', 'solution_4',

                'efficiency_1', 'efficiency_2',

                'compliance_1', 'compliance_2', 'compliance_3',

                "solution_total", "efficiency_total", "compliance_total", "overall_score",

                'fatal', 'fatal_count', 'disput_status', 'status', 'closed_date', 'areas_improvement', 'positives',
                'comments', )

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response

        elif campaign == "Amerisave":
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = ['Process', 'Employee ID', 'Associate Name', 'Type', 'Lead Source', 'Customer ID',
                       'Transfer/Non-transfer', 'Call Date', 'Audit Date', 'Quality Analyst', 'Team Lead', 'Manager',
                       'Assistant Manager', 'Week',

                       "Did CSS adhere to the script associated with the lead source?",
                       "What was the consumer's main objection?",
                       "Did CSS attempt to overcome objections?",
                       "Transfer Only: Did CSS properly transfer the customer to sales?",

                       "Did CSS disposition call correctly?",
                       "CSS Full Name",
                       "AmeriSave Mortgage Corporation",
                       "Recorded Line",
                       "Pre-qualified for a loan with AMC",
                       "Did CSS read Fine Print verbatim and completely?",

                       "If Fail, Which Type",
                       "Total Score",

                       'Fatal', 'Fatal Count', 'Dispute Status', 'Status',
                       'Closed Date', 'Areas of improvement', 'Positives', 'Comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = AmerisaveMonForm.objects.filter(
                audit_date__range=[start_date, end_date], qa=qa).values_list(
                'process', 'emp_id', 'associate_name', 'category', 'lead_source', 'customer_id',
                'transfer', 'call_date', 'audit_date', 'qa', 'team_lead', 'manager',
                'am', 'week',
                "nce_1",
                "nce_2",
                "nce_3",
                "nce_4",

                "compliance_1",
                "compliance_2",
                "compliance_3",
                "compliance_4",
                "compliance_5",
                "compliance_6",

                "fail_type",
                "overall_score",
                'fatal', 'fatal_count', 'disput_status', 'status',
                'closed_date', 'areas_improvement', 'positives', 'comments')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response


        elif campaign == "Movement Insurance":
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = [
                'process', 'type', 'emp_id', 'associate_name', 'qa', 'team_lead', 'am', 'week', 'audit_date', 'form_id',
                'customer_name', 'case_id', 'transaction_date', 'zone', 'lob', 'concept', 'manager'
                'category', 'q_1', 'areas_improvement', 'positives', 'comments', 'added_by', 'status', 'closed_date',
                'emp_comments', 'overall_score', 'fatal', 'fatal_count', 'disput_status'
            ]

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = MovementInsuranceMonForm.objects.filter(audit_date__range=[start_date, end_date], qa=qa
                                                   ).values_list(
                'process', 'type', 'emp_id', 'associate_name', 'qa', 'team_lead', 'am', 'week', 'audit_date',
                'form_id', 'customer_name', 'case_id', 'transaction_date', 'zone', 'lob', 'concept', 'manager',
                'category', 'q_1', 'areas_improvement', 'positives', 'comments', 'added_by', 'status',
                'closed_date', 'emp_comments', 'overall_score', 'fatal', 'fatal_count', 'disput_status')

            import datetime
            rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime.datetime) else x for x in row] for row in
                    rows]

            for row in rows:
                row_num += 1
                for col_num in range(len(row)):
                    ws.write(row_num, col_num, row[col_num], font_style)

            wb.save(response)

            return response


        elif campaign == "Brightway":
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="audit-report.xls"'
            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Users Data')  # this will make a sheet named Users Data
            # Sheet header, first row
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            columns = [
                'process', 'type', 'emp_id', 'associate_name', 'fws_id', 'qa', 'team_lead', 'audit_date', 'policy_no',
                'place', 'policy_type', 'case_status', 'case_date', 'manager', 'manager_id', 'category',
                'q_1', 'q_2', 'q_3', 'q_4',
                'areas_improvement', 'positives', 'comments', 'added_by', 'status', 'closed_date', 'emp_comments',
                'overall_score', 'am', 'week', 'fatal', 'fatal_count', 'dispute_status'
            ]

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = BrightwayMonForm.objects.filter(audit_date__range=[start_date, end_date], qa=qa
                                                   ).values_list(
                'process', 'type', 'emp_id', 'associate_name', 'fws_id', 'qa', 'team_lead', 'audit_date', 'policy_no',
                'place', 'policy_type', 'case_status', 'case_date', 'manager', 'manager_id', 'category',
                'q_1', 'q_2', 'q_3', 'q_4',
                'areas_improvement', 'positives', 'comments', 'added_by', 'status', 'closed_date', 'emp_comments',
                'overall_score', 'am', 'week', 'fatal', 'fatal_count', 'disput_status')

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


# ------------------ New Series MonForms ----------------copy Aadya---------#

def newSeriesMonForms(request):
    if request.method == 'POST':
        campaign_name = request.POST['campaign']

        def newseriesAddCoaching(monform):

            category = 'Outbound'
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
            call_duration = (int(request.POST['durationh']) * 3600) + (int(request.POST['durationm']) * 60) + int(
                request.POST['durations'])

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

            softskill_total = softskill_1 + softskill_2 + softskill_3 + softskill_4 + softskill_5
            # Compliance
            compliance_1 = int(request.POST['compliance_1'])
            compliance_2 = int(request.POST['compliance_2'])
            compliance_3 = int(request.POST['compliance_3'])
            compliance_4 = int(request.POST['compliance_4'])
            compliance_5 = int(request.POST['compliance_5'])
            compliance_6 = int(request.POST['compliance_6'])

            compliance_total = compliance_1 + compliance_2 + compliance_3 + compliance_4 + compliance_5 + compliance_6

            fatal_list = [compliance_1, compliance_2, compliance_3, compliance_4, compliance_5, compliance_6]
            fatal_list_count = []
            for i in fatal_list:
                if i == 0:
                    fatal_list_count.append(i)
            no_of_fatals = len(fatal_list_count)

            if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0 or compliance_4 == 0 or compliance_5 == 0 or compliance_6 == 0:
                overall_score = 0
                fatal = True
            else:
                overall_score = oc_total + softskill_total + compliance_total
                fatal = False

            areas_improvement = request.POST['areaimprovement']
            positives = request.POST['positives']
            comments = request.POST['comments']
            added_by = request.user.profile.emp_name
            week = request.POST['week']
            am = request.POST['am']

            leadsales = monform(
                associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                manager=manager_name, manager_id=manager_emp_id,
                call_date=call_date, audit_date=audit_date, customer_name=customer_name,
                customer_contact=customer_contact,
                campaign=campaign, concept=concept, zone=zone, call_duration=call_duration,
                oc_1=oc_1, oc_2=oc_2, oc_3=oc_3,
                softskill_1=softskill_1, softskill_2=softskill_2, softskill_3=softskill_3, softskill_4=softskill_4,
                softskill_5=softskill_5, softskill_total=softskill_total,
                compliance_1=compliance_1, compliance_2=compliance_2, compliance_3=compliance_3,
                compliance_4=compliance_4, compliance_5=compliance_5, compliance_6=compliance_6,
                compliance_total=compliance_total,
                areas_improvement=areas_improvement,
                positives=positives, comments=comments,
                added_by=added_by,
                overall_score=overall_score, category=category,
                week=week, am=am, fatal_count=no_of_fatals, fatal=fatal, ce_total=oc_total,
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

        elif campaign_name == 'Clean-Living Health and Wellness':
            newseriesAddCoaching(CleanLivingHealthWellnessOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Practo Outbound':
            newseriesAddCoaching(PractoOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Imaginarium Outbound':
            newseriesAddCoaching(ImaginariumOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'US Jaclean Outbound':
            newseriesAddCoaching(USJacleanOutboundForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Global Galaxy Outbound':
            newseriesAddCoaching(GlobalGalaxyOutboundForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Community Health Project Inc':
            newseriesAddCoaching(CommunityHealthProjectIncOutbound)
            return redirect('/employees/qahome')

        elif campaign_name == 'Educated Analytics LLC':
            newseriesAddCoaching(EducatedAnalyticsLLCOutbound)
            return redirect('/employees/qahome')

        elif campaign_name == 'New Dimension Pharmacy':
            newseriesAddCoaching(NewDimensionPharmacyOutbound)
            return redirect('/employees/qahome')

        elif campaign_name == 'Stay-N-Charge':
            newseriesAddCoaching(StayNChargeOutbound)
            return redirect('/employees/qahome')

        elif campaign_name == 'J & H Energy Consultant':
            newseriesAddCoaching(JHEnergyConsultantOutbound)
            return redirect('/employees/qahome')

        elif campaign_name == 'MDR Group LLC':
            newseriesAddCoaching(MDRGroupLLCOutbound)
            return redirect('/employees/qahome')

        elif campaign_name == 'Corey Small Insurance Agency Inc':
            newseriesAddCoaching(CoreySmallInsuranceAgencyOutbound)
            return redirect('/employees/qahome')

        elif campaign_name == 'Eduvocate Outbound':
            newseriesAddCoaching(EduvocateOutbound)
            return redirect('/employees/qahome')

        elif campaign_name == 'Cross Tower Outbound':
            newseriesAddCoaching(CrossTowerOutbound)
            return redirect('/employees/qahome')

        elif campaign_name == 'Dawn Financial Outbound':
            newseriesAddCoaching(DawnFinancialOutbound)
            return redirect('/employees/qahome')

        elif campaign_name == 'Xport Digital Outbound':
            newseriesAddCoaching(XportDigitalOutbound)
            return redirect('/employees/qahome')

        elif campaign_name == 'Calista Outbound':
            newseriesAddCoaching(CalistaOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Global Ark Outbound':
            newseriesAddCoaching(GlobalArkOutboundMonform)
            return redirect('/employees/qahome')

        elif campaign_name == 'DI Develop Outbound':
            newseriesAddCoaching(DIDevelopOutbound)
            return redirect('/employees/qahome')

        elif campaign_name == 'Freehold Outbound':
            newseriesAddCoaching(FreeholdOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Zeamo Outbound':
            newseriesAddCoaching(ZeamoOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Sapphire Medicals Outbound':
            newseriesAddCoaching(SapphireMedicalsOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Eehhaaa Outbound':
            newseriesAddCoaching(EehhaaaOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'All Care Physical Therapy':
            newseriesAddCoaching(AllCarePhysicalTherapyMonform)
            return redirect('/employees/qahome')

        elif campaign_name == 'Executive Capital Resources':
            newseriesAddCoaching(ExecutiveCapitalResourcesmonform)
            return redirect('/employees/qahome')

        elif campaign_name == 'Bright Way Outbound':
            newseriesAddCoaching(BrightWayOutboundmonform)
            return redirect('/employees/qahome')

        elif campaign_name == 'Building lab LLC Outbound':
            newseriesAddCoaching(BuildinglabLLCOutboundmonform)
            return redirect('/employees/qahome')

        elif campaign_name == 'Global Pharma Outbound':
            newseriesAddCoaching(GlobalPharmaOutboundmonform)
            return redirect('/employees/qahome')

        elif campaign_name == 'Redefine Plastics Outbound':
            newseriesAddCoaching(RedefinePlasticsOutboundmonform)
            return redirect('/employees/qahome')

        elif campaign_name == 'Hard Hat Technologies Outbound':
            newseriesAddCoaching(HardHatTechnologiesOutboundmonform)
            return redirect('/employees/qahome')

        elif campaign_name == '3rd Wave Outbound':
            newseriesAddCoaching(ThirdWaveOutboundmonform)
            return redirect('/employees/qahome')

        elif campaign_name == 'K7 Outbound':
            newseriesAddCoaching(K7Outboundmonform)
            return redirect('/employees/qahome')

        elif campaign_name == 'Trial Mapping Outbound':
            newseriesAddCoaching(TrialMappingOutboundmonform)
            return redirect('/employees/qahome')

        elif campaign_name == 'Edu Class Outbound':
            newseriesAddCoaching(EduClassOutboundmonform)
            return redirect('/employees/qahome')

        elif campaign_name == 'Cred Avenue Outbound':
            newseriesAddCoaching(CredAvenueOutboundmonform)
            return redirect('/employees/qahome')

        elif campaign_name == 'TKAWDIW Outbound':
            newseriesAddCoaching(TKAWDIWOutboundmonform)
            return redirect('/employees/qahome')

        elif campaign_name == 'Dream Pick Outbound':
            newseriesAddCoaching(DreamPickOutboundmonform)
            return redirect('/employees/qahome')

        elif campaign_name == 'Kheloyar Outbound':
            newseriesAddCoaching(KheloyarOutboundmonform)
            return redirect('/employees/qahome')

        elif campaign_name == 'Mex Trading Outbound':
            newseriesAddCoaching(MaxTradingOutboundmonform)
            return redirect('/employees/qahome')

        elif campaign_name == 'ESR TechTalent Outbound':
            newseriesAddCoaching(ESRTechTalentOutboundmonform)
            return redirect('/employees/qahome')

        elif campaign_name == 'Green Connect Outbound':
            newseriesAddCoaching(GreenConnectOutboundmonform)
            return redirect('/employees/qahome')

        elif campaign_name == 'Rapid Mortgage':
            newseriesAddCoaching(RapidMortgageOutboundmonform)
            return redirect('/employees/qahome')

        elif campaign_name == 'Central Mortgage Funding':
            newseriesAddCoaching(CentralMortgageFundingOutboundmonform)
            return redirect('/employees/qahome')

        elif campaign_name == 'Bridan & Associates Outbound':
            newseriesAddCoaching(BridanAssociatesOutboundmonform)
            return redirect('/employees/qahome')

        elif campaign_name == 'Linen Finder Outbound':
            newseriesAddCoaching(LinenFinderOutboundmonform)
            return redirect('/employees/qahome')

        elif campaign_name == 'Better Ed Outbound':
            newseriesAddCoaching(BetterEdOutboundmonform)
            return redirect('/employees/qahome')

        elif campaign_name == 'Com 98 Outbound':
            newseriesAddCoaching(Com98Outboundmonform)
            return redirect('/employees/qahome')

        elif campaign_name == 'Gretna Medical Centre Outbound':
            newseriesAddCoaching(GretnaMedicalCentreOutboundmonform)
            return redirect('/employees/qahome')

        elif campaign_name == 'Arista MD Outbound':
            newseriesAddCoaching(AristaMDOutboundmonform)
            return redirect('/employees/qahome')

        elif campaign_name == 'Robert Damon Production Outbound':
            newseriesAddCoaching(RobertDamonProductionOutboundmonform)
            return redirect('/employees/qahome')

        elif campaign_name == 'Venwiz Outbound':
            newseriesAddCoaching(VenwizOutboundmonform)
            return redirect('/employees/qahome')


        elif campaign_name == 'City Habitat Outbound':
            newseriesAddCoaching(CityHabitatOutboundmonform)
            return redirect('/employees/qahome')


        elif campaign_name == 'Optel Outbound':
            newseriesAddCoaching(OptelOutboundmonform)
            return redirect('/employees/qahome')


        elif campaign_name == 'South County Outbound':
            newseriesAddCoaching(SouthCountyOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Inpress Outbound':
            newseriesAddCoaching(InpressOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'L & M Enterprises Outbound':
            newseriesAddCoaching(LMEnterprisesOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Towers Traders Group Outbound':
            newseriesAddCoaching(TowersTradersGroupOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Job E Roofing Outbound':
            newseriesAddCoaching(JobERoofingOutboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Travel Wholesale Outbound':
            newseriesAddCoaching(TravelWholesaleOutboundMonForm)
            return redirect('/employees/qahome')

        else:
            pass


    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/new-series-comon.html', data)


def winopolyAddCoaching(request):
    if request.method == 'POST':
        campaign_name = request.POST['campaign']
        category = 'Outbound'
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
        disposition = request.POST['disposition']
        call_duration = (int(request.POST['durationh']) * 3600) + (int(request.POST['durationm']) * 60) + int(
            request.POST['durations'])
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager
        manager_emp_id_obj = Profile.objects.get(emp_name=manager)
        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager

        # Opening
        comp_1 = int(request.POST['comp_1'])
        op_2 = int(request.POST['op_2'])
        op_3 = int(request.POST['op_3'])
        op_4 = int(request.POST['op_4'])
        op_5 = int(request.POST['op_5'])
        op_total = op_2 + op_3 + op_4 + op_5

        # MATCHING PROCESS
        mp_1 = int(request.POST['mp_1'])
        mp_2 = int(request.POST['mp_2'])
        mp_3 = int(request.POST['mp_3'])
        mp_total = mp_1 + mp_2 + mp_3

        # CALL HANDLING PROCESS
        cp_1 = int(request.POST['cp_1'])
        cp_2 = int(request.POST['cp_2'])
        cp_3 = int(request.POST['cp_3'])
        cp_4 = int(request.POST['cp_4'])
        cp_5 = int(request.POST['cp_5'])
        cp_6 = int(request.POST['cp_6'])
        cp_total = cp_1 + cp_2 + cp_3 + cp_4 + cp_5 + cp_6

        #  Compliance
        comp_2 = int(request.POST['comp_2'])
        comp_3 = int(request.POST['comp_3'])
        comp_4 = int(request.POST['comp_4'])
        comp_5 = int(request.POST['comp_5'])

        # TP
        tp_1 = int(request.POST['tp_1'])
        tp_2 = int(request.POST['tp_2'])
        tp_3 = int(request.POST['tp_3'])
        comp_6 = int(request.POST['comp_6'])
        tp_total = tp_1 + tp_2 + tp_3

        evaluator_comment = request.POST['evaluator_comment']
        coaching_comments = request.POST['coaching_comments']

        compliance_total = comp_1 + comp_2 + comp_3 + comp_4 + comp_5 + comp_6

        fatal_list = [comp_1, comp_2, comp_3, comp_4, comp_5, comp_6]
        fatal_list_count = []
        for i in fatal_list:
            if i == 0:
                fatal_list_count.append(i)

        no_of_fatals = len(fatal_list_count)

        if comp_1 == 0 or comp_2 == 0 or comp_3 == 0 or comp_4 == 0 or comp_5 == 0 or comp_6 == 0:
            overall_score = 0
            fatal = True
        else:
            overall_score = op_total + mp_total + cp_total + tp_total
            fatal = False

        added_by = request.user.profile.emp_name
        week = request.POST['week']
        am = request.POST['am']

        wino = WinopolyOutbound(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                manager=manager_name, manager_id=manager_emp_id,

                                trans_date=call_date, audit_date=audit_date,
                                customer_name=customer_name,
                                customer_contact=customer_contact,
                                campaign=campaign, concept=concept, zone=zone,
                                call_duration=call_duration,
                                disposition=disposition,
                                # opening
                                comp_1=comp_1, op_2=op_2, op_3=op_3, op_4=op_4, op_5=op_5,
                                op_total=op_total,

                                mp_1=mp_1, mp_2=mp_2, mp_3=mp_3, mp_total=mp_total,

                                cp_1=cp_1, cp_2=cp_2, cp_3=cp_3, cp_4=cp_4, cp_5=cp_5,
                                cp_6=cp_6, cp_total=cp_total,

                                comp_2=comp_2, comp_3=comp_3, comp_4=comp_4, comp_5=comp_5,

                                tp_1=tp_1, tp_2=tp_2, tp_3=tp_3,
                                comp_6=comp_6, tp_total=tp_total,

                                evaluator_comment=evaluator_comment, coaching_comments=coaching_comments,

                                compliance_total=compliance_total,

                                added_by=added_by,

                                overall_score=overall_score, category=category,
                                week=week, am=am, fatal_count=no_of_fatals, fatal=fatal
                                )
        wino.save()
        return redirect('/employees/qahome')
    else:
        pass


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
            call_duration = (int(request.POST['durationh']) * 3600) + (int(request.POST['durationm']) * 60) + int(
                request.POST['durations'])

            try:
                prof_obj = Profile.objects.get(emp_id=emp_id)
                manager = prof_obj.manager
            except Profile.DoesNotExist:
                manager = 'NA'

            try:
                manager_emp_id_obj = Profile.objects.get(emp_name=manager)
                manager_emp_id = manager_emp_id_obj.emp_id
                manager_name = manager
            except Profile.DoesNotExist:
                manager_emp_id = 0
                manager_name = 'NA'

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

            inbound = monform(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                              manager=manager_name, manager_id=manager_emp_id,

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

        elif campaign_name == 'LJ Hub Inbound':
            inboundAddCoaching(LJHubInboundMonForms)
            return redirect('/employees/qahome')

        elif campaign_name == 'Obthera Inc':
            inboundAddCoaching(ObtheraIncInboundMonForms)
            return redirect('/employees/qahome')

        elif campaign_name == 'Eduvocate Inbound':
            inboundAddCoaching(EduvocateInboundMonForms)
            return redirect('/employees/qahome')

        elif campaign_name == 'Cross Tower Inbound':
            inboundAddCoaching(CrossTowerInboundMonForms)
            return redirect('/employees/qahome')

        elif campaign_name == 'Sana Life Science Inbound':
            inboundAddCoaching(SanaLifeScienceInbound)
            return redirect('/employees/qahome')

        elif campaign_name == 'Mobile 22 Inbound':
            inboundAddCoaching(MonitoringFormMobile22InboundCalls)
            return redirect('/employees/qahome')

        elif campaign_name == 'Xport Digital Inbound':
            inboundAddCoaching(XportDigitalInboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Calista Inbound':
            inboundAddCoaching(CalistaInboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Global Ark Inbound':
            inboundAddCoaching(GlobalArkInboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == '3rd Wave Inbound':
            inboundAddCoaching(ThirdWaveInboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Hard Hat Technologies Inbound':
            inboundAddCoaching(HardHatTechnologiesInboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Gretna Medical Center Inbound':
            inboundAddCoaching(GretnaMedicalCenterInboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Better Ed Inbound':
            inboundAddCoaching(BetterEdInboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Com 98 Inbound':
            inboundAddCoaching(Com98InboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Open Winds Inbound':
            inboundAddCoaching(OpenWindsInboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Embassy Luxury Inbound':
            inboundAddCoaching(EmbassyLuxuryInboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'South County Inbound':
            inboundAddCoaching(SouthCountyInboundMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'City Habitat Inbound':
            inboundAddCoaching(CityHabitatInboundMonForm)
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
            duration = (int(request.POST['durationh']) * 3600) + (int(request.POST['durationm']) * 60) + int(
                request.POST['durations'])

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

        elif campaign_name == 'US Jaclean Email Chat':
            domesticEmailChatAddCoaching(USJacleanEmailChatForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Cross Tower Email-Chat':
            domesticEmailChatAddCoaching(CrossTowerEmailChatForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Sana Life Science Email-Chat':
            domesticEmailChatAddCoaching(SanaLifeScienceEmailChatForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Bhagyalaxmi Chat':
            domesticEmailChatAddCoaching(BhagyalaxmiChatMonForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Sapphire Medicals Chat':
            domesticEmailChatAddCoaching(SapphireMedicalsChatMonForm)
            return redirect('/employees/qahome')


        elif campaign_name == 'Gretna Medical Center Email':
            domesticEmailChatAddCoaching(GretnaMedicalCenterEmailChatForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Jump Rydes Email - Chat':
            domesticEmailChatAddCoaching(JumpRydesEmailChatForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Naffa Innovation Email - Chat':
            domesticEmailChatAddCoaching(NaffaInnovationEmailChatForm)
            return redirect('/employees/qahome')

        elif campaign_name == 'Inpress Email - Chat':
            domesticEmailChatAddCoaching(InpressEmailChatForm)
            return redirect('/employees/qahome')


        else:
            pass

    else:
        return redirect('/employees/qahome')


# Other Forms

def blazinghogauditform(request):
    if request.method == 'POST':

        category = 'Email - Chat'
        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        customer_name = request.POST['customer']
        ticket_id = request.POST['ticket_id']
        call_date = request.POST['calldate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        zone = request.POST['zone']
        query_type = request.POST['query_type']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager

        # Opening and Closing

        solution_1 = int(request.POST['solution_1'])
        solution_2 = int(request.POST['solution_2'])
        solution_3 = int(request.POST['solution_3'])
        solution_4 = int(request.POST['solution_4'])
        solution_total = solution_1 + solution_2 + solution_3 + solution_4

        # Softskills
        efficiency_1 = int(request.POST['efficiency_1'])
        efficiency_2 = int(request.POST['efficiency_2'])
        efficiency_total = efficiency_1 + efficiency_2

        # Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])

        compliance_total = compliance_1 + compliance_2 + compliance_3

        fatal_list = [compliance_1, compliance_2, compliance_3]
        fatal_list_count = []
        for i in fatal_list:
            if i == 0:
                fatal_list_count.append(i)
        no_of_fatals = len(fatal_list_count)

        if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0:
            overall_score = 0
            fatal = True
        else:
            overall_score = solution_total + efficiency_total + compliance_total
            fatal = False

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name
        week = request.POST['week']
        am = request.POST['am']

        blaz = BlazingHogEmailChatmonform(
            associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
            manager=manager_name, manager_id=manager_emp_id,
            call_date=call_date, audit_date=audit_date, customer_name=customer_name, ticket_id=ticket_id,
            campaign=campaign, concept=concept, zone=zone, query_type=query_type,

            solution_1=solution_1, solution_2=solution_2, solution_3=solution_3, solution_4=solution_4,

            efficiency_1=efficiency_1, efficiency_2=efficiency_2,

            compliance_1=compliance_1, compliance_2=compliance_2, compliance_3=compliance_3,

            solution_total=solution_total, efficiency_total=efficiency_total,
            compliance_total=compliance_total,

            areas_improvement=areas_improvement,
            positives=positives, comments=comments,
            added_by=added_by,
            overall_score=overall_score, category=category,
            week=week, am=am, fatal_count=no_of_fatals, fatal=fatal,
        )
        blaz.save()
        return redirect('/employees/qahome')


def abhFormSAve(request):
    if request.method == 'POST':
        category = 'Outbound'
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
        call_duration = (int(request.POST['durationh']) * 3600) + (int(request.POST['durationm']) * 60) + int(
            request.POST['durations'])

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

        softskill_total = softskill_1 + softskill_2 + softskill_3 + softskill_4

        # Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])
        compliance_4 = int(request.POST['compliance_4'])

        compliance_total = compliance_1 + compliance_2 + compliance_3 + compliance_4

        fatal_list = [oc_2, compliance_2, compliance_3, compliance_4]
        fatal_list_count = []
        for i in fatal_list:
            if i == 0:
                fatal_list_count.append(i)
        no_of_fatals = len(fatal_list_count)

        if oc_2 == 0 or compliance_2 == 0 or compliance_3 == 0 or compliance_4 == 0:
            overall_score = 0
            fatal = True
        else:
            overall_score = oc_total + softskill_total + compliance_total
            fatal = False

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name
        week = request.POST['week']
        am = request.POST['am']

        leadsales = ABHindalcoMonForm(
            associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
            manager=manager_name, manager_id=manager_emp_id,
            call_date=call_date, audit_date=audit_date, customer_name=customer_name, customer_contact=customer_contact,
            campaign=campaign, concept=concept, zone=zone, call_duration=call_duration,

            oc_1=oc_1, oc_2=oc_2, oc_3=oc_3,

            softskill_1=softskill_1, softskill_2=softskill_2, softskill_3=softskill_3, softskill_4=softskill_4,
            softskill_total=softskill_total,

            compliance_1=compliance_1, compliance_2=compliance_2, compliance_3=compliance_3, compliance_4=compliance_4,

            compliance_total=compliance_total,

            areas_improvement=areas_improvement,
            positives=positives, comments=comments,
            added_by=added_by,
            overall_score=overall_score, category=category,
            week=week, am=am, fatal_count=no_of_fatals, fatal=fatal, oc_total=oc_total,
        )
        leadsales.save()
        return redirect('/employees/qahome')

def brightwaySubmit(request):
    if request.method == 'POST':
        category = 'Email - Chat'
        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        audit_date = request.POST['auditdate']
        fws_id = request.POST['fws_id']
        policy_no = request.POST['policy_no']
        trans_date = request.POST['trans_date']
        place = request.POST['place']
        policy_type = request.POST['policy_type']
        case_status = request.POST['case_status']
        week = request.POST['week']
        manager = request.POST['manager']

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name
        am = request.POST['am']
        try:
            manager_id = Profile.objects.get(emp_name=manager).emp_id
        except:
            manager_id = 0

        q_1 = int(request.POST['q_1'])
        q_2 = int(request.POST['q_2'])
        q_3 = int(request.POST['q_3'])
        q_4 = int(request.POST['q_4'])


        fatal_list = [q_2, q_3, q_4]
        fatal_list_count = []
        for i in fatal_list:
            if i == 0:
                fatal_list_count.append(i)
        no_of_fatals = len(fatal_list_count)

        if q_2 == 0 or q_3 == 0 or q_4 == 0 :
            overall_score = 0
            fatal = True
        else:
            overall_score = q_1 + q_2 + q_3 + q_4
            fatal = False

        BrightwayMonForm.objects.create(
            emp_id=emp_id, associate_name=associate_name, qa=qa, team_lead=team_lead, audit_date=audit_date,
            fws_id=fws_id, policy_no=policy_no, place=place, policy_type=policy_type, case_status=case_status,
            case_date=trans_date, manager=manager, manager_id=manager_id, category=category, q_1=q_1, q_2=q_2, q_3=q_3,
            q_4=q_4, areas_improvement=areas_improvement, positives=positives, comments=comments, added_by=added_by,
            overall_score=overall_score, am=am, week=week, fatal=fatal, fatal_count=no_of_fatals
        )
        return redirect('/employees/qahome')


def ilmEMailChat(request):
    if request.method == 'POST':
        category = 'Email - Chat'
        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        customer_name = request.POST['customer']
        ticket_id = request.POST['ticket_id']
        trans_date = request.POST['trans_date']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        zone = request.POST['zone']
        query_type = request.POST['query_type']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager
        manager_emp_id_obj = Profile.objects.get(emp_name=manager)
        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################

        # Solution
        s_1 = int(request.POST['s_1'])
        s_2 = int(request.POST['s_2'])
        s_3 = int(request.POST['s_3'])
        s_4 = int(request.POST['s_4'])
        s_total = s_1 + s_2 + s_3 + s_4

        # Efficiency
        e_1 = int(request.POST['e_1'])
        e_2 = int(request.POST['e_2'])
        e_total = e_1 + e_2

        # Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])
        compliance_total = compliance_1 + compliance_2 + compliance_3

        #################################################

        fatal_list = [compliance_1, compliance_2, compliance_3]
        fatal_list_count = []
        for i in fatal_list:
            if i == 0:
                fatal_list_count.append(i)

        no_of_fatals = len(fatal_list_count)

        ####################################################
        if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0:
            overall_score = 0
            fatal = True
        else:
            overall_score = s_total + e_total + compliance_total
            fatal = False

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        week = request.POST['week']
        am = request.POST['am']

        ilm = ILMakiageEmailChatForm(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                     manager=manager_name, manager_id=manager_emp_id,
                                     trans_date=trans_date, audit_date=audit_date, customer_name=customer_name,
                                     ticket_id=ticket_id,
                                     campaign=campaign, concept=concept, zone=zone,
                                     query_type=query_type,
                                     s_1=s_1, s_2=s_2, s_3=s_3, s_4=s_4,
                                     e_1=e_1, e_2=e_2,
                                     compliance_1=compliance_1, compliance_2=compliance_2, compliance_3=compliance_3,
                                     areas_improvement=areas_improvement,
                                     positives=positives, comments=comments,
                                     added_by=added_by,
                                     overall_score=overall_score, category=category,
                                     week=week, am=am, fatal_count=no_of_fatals, fatal=fatal,
                                     s_total=s_total, e_total=e_total, compliance_total=compliance_total
                                     )
        ilm.save()
        return redirect('/employees/qahome')
    else:
        pass

def movementInsurance(request):
    if request.method == 'POST':
        emp_id = request.POST['empid']
        associate_name = request.POST['empname']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        zone = request.POST['zone']
        concept = request.POST['concept']
        case_no = request.POST['case_no']
        customer_name = request.POST['customer_name']
        lob = request.POST['lob']
        id = request.POST['id']
        trans_date = request.POST['trans_date']
        auditdate = request.POST['auditdate']
        manager = request.POST['manager']
        am = request.POST['am']
        week = request.POST['week']

        # Questions
        q_1 = request.POST['q_1']

        areaimprovement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']

        manager = Profile.objects.get(emp_id=emp_id).manager
        try:
            manager_id = Profile.objects.get(emp_name=manager).emp_id
        except:
            manager_id = 0

        added_by = qa


        category = 'Email - Chat'

        MovementInsuranceMonForm.objects.create(
            emp_id=emp_id, associate_name=associate_name, qa=qa, team_lead=team_lead, am=am, week=week,
            audit_date=datetime.today(), form_id=id, customer_name=customer_name, case_id=case_no,
            transaction_date=trans_date, zone =zone, lob=lob, concept =concept,
            manager=manager, manager_id=manager_id, category=category,
            q_1=q_1,
            areas_improvement=areaimprovement, positives=positives, comments=comments,
            added_by=added_by, overall_score=q_1,
        )
        return redirect('/employees/qahome')

def Amerisave(request):
    if request.method == 'POST':
        category = request.POST['type']
        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        customer_id = request.POST['customer_id']
        call_date = request.POST['call_date']
        audit_date = request.POST['auditdate']
        lead_source = request.POST['lead_source']
        transfer = request.POST['transfer']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager

        # NCE
        nce_1 = int(request.POST['nce_1'])
        nce_2 = request.POST['nce_2']
        nce_3 = int(request.POST['nce_3'])
        nce_4 = int(request.POST['nce_4'])
        nce_total = nce_1 + nce_3 + nce_4

        # Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])
        compliance_4 = int(request.POST['compliance_4'])
        compliance_5 = int(request.POST['compliance_5'])
        compliance_6 = int(request.POST['compliance_6'])

        compliance_total = compliance_1 + compliance_2 + compliance_3 + compliance_4 + compliance_5 + compliance_6

        fatal_list = [compliance_1, compliance_2, compliance_3, compliance_4, compliance_5, compliance_6]
        fatal_list_count = []
        for i in fatal_list:
            if i == 0:
                fatal_list_count.append(i)
        no_of_fatals = len(fatal_list_count)

        if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0 or compliance_4 == 0 or compliance_5 == 0 or compliance_6 == 0:
            overall_score = 0
            fatal = True
        else:
            overall_score = nce_total + compliance_total
            fatal = False

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        fail_type = request.POST.get('fail_type')
        added_by = request.user.profile.emp_name
        week = request.POST['week']
        am = request.POST['am']

        leadsales = AmerisaveMonForm(
            associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
            manager=manager_name, manager_id=manager_emp_id,
            call_date=call_date, audit_date=audit_date, customer_id=customer_id, lead_source=lead_source,
            category=category, transfer=transfer, fail_type=fail_type,

            nce_1=nce_1, nce_2=nce_2, nce_3=nce_3, nce_4=nce_4, nce_total=nce_total,

            compliance_1=compliance_1, compliance_2=compliance_2, compliance_3=compliance_3, compliance_4=compliance_4,
            compliance_5=compliance_5, compliance_6=compliance_6,
            compliance_total=compliance_total,

            areas_improvement=areas_improvement,
            positives=positives, comments=comments,
            added_by=added_by,
            overall_score=overall_score,
            week=week, am=am, fatal_count=no_of_fatals, fatal=fatal,
        )
        leadsales.save()
        return redirect('/employees/qahome')


def chatCoachingformEva(request):
    if request.method == 'POST':
        category = 'Email/Chat Other'
        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        ticket_no = request.POST['ticketnumber']
        trans_date = request.POST['transdate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        evaluator = request.POST['evaluator']

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

        ce_total = ce_1 + ce_2 + ce_3 + ce_4

        # Compliance
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

        compliance_total = compliance_1 + compliance_2 + compliance_3 + compliance_4 + compliance_5 + compliance_6

        if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0 or compliance_4 == 0 or compliance_5 == 0 or compliance_6 == 0:
            overall_score = 0
            fatal = True
        else:
            overall_score = ce_total + compliance_total
            fatal = False

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        week = request.POST['week']
        am = request.POST['am']

        chat = ChatMonitoringFormEva(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                     manager=manager_name, manager_id=manager_emp_id,

                                     trans_date=trans_date, audit_date=audit_date, ticket_no=ticket_no,
                                     campaign=campaign, concept=concept, evaluator=evaluator,

                                     ce_1=ce_1, ce_2=ce_2, ce_3=ce_3, ce_4=ce_4, ce_total=ce_total,

                                     compliance_1=compliance_1, compliance_2=compliance_2, compliance_3=compliance_3,
                                     compliance_4=compliance_4, compliance_5=compliance_5, compliance_6=compliance_6,
                                     compliance_total=compliance_total,

                                     areas_improvement=areas_improvement,
                                     positives=positives, comments=comments,
                                     added_by=added_by,

                                     overall_score=overall_score, category=category,
                                     week=week, am=am, fatal_count=no_of_fatals, fatal=fatal
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
        category = 'Email/Chat Other'
        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        ticket_no = request.POST['ticketnumber']
        trans_date = request.POST['transdate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        evaluator = request.POST['evaluator']

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

        ce_total = ce_1 + ce_2 + ce_3 + ce_4

        # Compliance
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

        compliance_total = compliance_1 + compliance_2 + compliance_3 + compliance_4 + compliance_5 + compliance_6

        if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0 or compliance_4 == 0 or compliance_5 == 0 or compliance_6 == 0:
            overall_score = 0
            fatal = True
        else:
            overall_score = ce_total + compliance_total
            fatal = False

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        week = request.POST['week']
        am = request.POST['am']

        chat = ChatMonitoringFormPodFather(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                           manager=manager_name, manager_id=manager_emp_id,

                                           trans_date=trans_date, audit_date=audit_date, ticket_no=ticket_no,
                                           campaign=campaign, concept=concept, evaluator=evaluator,

                                           ce_1=ce_1, ce_2=ce_2, ce_3=ce_3, ce_4=ce_4, ce_total=ce_total,

                                           compliance_1=compliance_1, compliance_2=compliance_2,
                                           compliance_3=compliance_3,
                                           compliance_4=compliance_4, compliance_5=compliance_5,
                                           compliance_6=compliance_6,
                                           compliance_total=compliance_total,

                                           areas_improvement=areas_improvement,
                                           positives=positives, comments=comments,
                                           added_by=added_by,

                                           overall_score=overall_score, category=category,
                                           week=week, am=am, fatal_count=no_of_fatals, fatal=fatal
                                           )
        chat.save()
        return redirect('/employees/qahome')
    else:
        teams = Team.objects.all()
        users = User.objects.all()
        data = {'teams': teams, 'users': users}
        return render(request, 'mon-forms/ECPL-Pod-Father-Monitoring-Form-chat.html', data)


def fameHouseNew(request):
    if request.method == 'POST':
        category = 'Email/Chat Other'
        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']

        ticket_no = request.POST['ticket_no']
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
        compliance_7 = int(request.POST['compliance_7'])
        compliance_8 = int(request.POST['compliance_8'])
        compliance_9 = int(request.POST['compliance_9'])
        compliance_10 = int(request.POST['compliance_10'])
        compliance_11 = int(request.POST['compliance_11'])

        compliance_total = compliance_1 + compliance_2 + compliance_3 + compliance_4 + compliance_5 + compliance_6 + \
                           compliance_7 + compliance_8 + compliance_9 + compliance_10 + compliance_11

        na_list = []
        sum_list = []

        def scoreCalc(pk):
            if pk == 'NA':
                na_list.append(pk)
                return pk
            else:
                sum_list.append(int(pk))
                return int(pk)

        # Customer Response
        cr_1 = scoreCalc(request.POST["cr_1"])

        # Opening
        opening_1 = scoreCalc(request.POST['opening_1'])
        opening_2 = scoreCalc(request.POST['opening_2'])

        # Composition
        comp_1 = scoreCalc(request.POST['comp_1'])
        comp_2 = scoreCalc(request.POST['comp_2'])

        # Macro
        macro_1 = scoreCalc(request.POST['macro_1'])
        macro_2 = scoreCalc(request.POST['macro_2'])

        # Closing
        closing_1 = scoreCalc(request.POST['closing_1'])
        closing_2 = scoreCalc(request.POST['closing_2'])

        # Customer Issue Resolution
        cir_1 = scoreCalc(request.POST['cir_1'])
        cir_2 = scoreCalc(request.POST['cir_2'])
        cir_3 = scoreCalc(request.POST['cir_3'])
        cir_4 = scoreCalc(request.POST['cir_4'])
        cir_5 = scoreCalc(request.POST['cir_5'])
        cir_6 = scoreCalc(request.POST['cir_6'])
        cir_7 = scoreCalc(request.POST['cir_7'])

        # Ettiqt
        et_1 = scoreCalc(request.POST['et_1'])
        et_2 = scoreCalc(request.POST['et_2'])
        et_3 = scoreCalc(request.POST['et_3'])
        et_4 = scoreCalc(request.POST['et_4'])
        et_5 = scoreCalc(request.POST['et_5'])

        # Documentation
        doc_1 = scoreCalc(request.POST['doc_1'])
        doc_2 = scoreCalc(request.POST['doc_2'])
        doc_3 = scoreCalc(request.POST['doc_3'])
        doc_4 = scoreCalc(request.POST['doc_4'])

        fatal_list = [compliance_1, compliance_2, compliance_3, compliance_4, compliance_5, compliance_6,
                      compliance_7, compliance_8, compliance_9, compliance_10, compliance_11]

        fatal_list_count = []
        for i in fatal_list:
            if i == 0:
                fatal_list_count.append(i)
        no_of_fatals = len(fatal_list_count)

        if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0 or compliance_4 == 0 or compliance_5 == 0 or compliance_6 == 0 or compliance_7 == 0 or compliance_8 == 0 or compliance_9 == 0 or compliance_10 == 0 or compliance_11 == 0:
            overall_score = 0
            fatal = True
        else:
            if sum(sum_list) != 0:
                overall_score = (sum(sum_list) / len(sum_list)) * 100
            else:
                overall_score = 100
            fatal = False

        #################################################

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']

        added_by = request.user.profile.emp_name

        famehouse = FameHouseNewMonForm(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                        manager=manager_name, manager_id=manager_emp_id, am=am,
                                        trans_date=trans_date, audit_date=audit_date, ticket_no=ticket_no,
                                        campaign=campaign,
                                        compliance_1=compliance_1, compliance_2=compliance_2, compliance_3=compliance_3,
                                        compliance_4=compliance_4,
                                        compliance_5=compliance_5, compliance_6=compliance_6, compliance_7=compliance_7,
                                        compliance_8=compliance_8,
                                        compliance_9=compliance_9, compliance_10=compliance_10,
                                        compliance_11=compliance_11, compliance_total=compliance_total,
                                        cr_1=cr_1,
                                        opening_1=opening_1, opening_2=opening_2,
                                        comp_1=comp_1, comp_2=comp_2,
                                        cir_1=cir_1, cir_2=cir_2, cir_3=cir_3, cir_4=cir_4, cir_5=cir_5, cir_6=cir_6,
                                        cir_7=cir_7,
                                        macro_1=macro_1, macro_2=macro_2,
                                        doc_1=doc_1, doc_2=doc_2, doc_3=doc_3, doc_4=doc_4,
                                        et_1=et_1, et_2=et_2, et_3=et_3, et_4=et_4, et_5=et_5,
                                        closing_1=closing_1, closing_2=closing_2,
                                        areas_improvement=areas_improvement,
                                        positives=positives, comments=comments,
                                        added_by=added_by, ticket_type=ticket_type,
                                        category=category, overall_score=overall_score,
                                        week=week, fatal=fatal, fatal_count=no_of_fatals
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
        category = 'FLA'
        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        order_id = request.POST['order_id']
        trans_date = request.POST['transdate']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        service = request.POST['service']
        check_list = request.POST['checklist']

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        #########################################

        # Macros
        checklist_1 = int(request.POST['checklist_1'])

        reason_for_failure = request.POST['reason_for_failure']
        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        week = request.POST['week']
        am = request.POST['am']

        fla = FLAMonitoringForm(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                manager=manager_name, manager_id=manager_emp_id,

                                trans_date=trans_date, audit_date=audit_date, order_id=order_id,
                                campaign=campaign, concept=concept, service=service,

                                check_list=check_list,
                                checklist_1=checklist_1,

                                reason_for_failure=reason_for_failure,
                                areas_improvement=areas_improvement,
                                positives=positives, comments=comments,
                                added_by=added_by,

                                overall_score=checklist_1, category=category,
                                week=week, am=am
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
        cat1 = [cat1chat1, cat1chat2, cat1chat3, cat1chat4, cat1chat5, cat1chat6]

        cat2chat1 = request.POST['cat2chat1']
        cat2chat2 = request.POST['cat2chat2']
        cat2chat3 = request.POST['cat2chat3']
        cat2chat4 = request.POST['cat2chat4']
        cat2chat5 = request.POST['cat2chat5']
        cat2chat6 = request.POST['cat2chat6']
        cat2 = [cat2chat1, cat2chat2, cat2chat3, cat2chat4, cat2chat5, cat2chat6]

        cat3chat1 = request.POST['cat3chat1']
        cat3chat2 = request.POST['cat3chat2']
        cat3chat3 = request.POST['cat3chat3']
        cat3chat4 = request.POST['cat3chat4']
        cat3chat5 = request.POST['cat3chat5']
        cat3chat6 = request.POST['cat3chat6']
        cat3 = [cat3chat1, cat3chat2, cat3chat3, cat3chat4, cat3chat5, cat3chat6]

        cat4chat1 = request.POST['cat4chat1']
        cat4chat2 = request.POST['cat4chat2']
        cat4chat3 = request.POST['cat4chat3']
        cat4chat4 = request.POST['cat4chat4']
        cat4chat5 = request.POST['cat4chat5']
        cat4chat6 = request.POST['cat4chat6']
        cat4 = [cat4chat1, cat4chat2, cat4chat3, cat4chat4, cat4chat5, cat4chat6]

        cat5chat1 = request.POST['cat5chat1']
        cat5chat2 = request.POST['cat5chat2']
        cat5chat3 = request.POST['cat5chat3']
        cat5chat4 = request.POST['cat5chat4']
        cat5chat5 = request.POST['cat5chat5']
        cat5chat6 = request.POST['cat5chat6']
        cat5 = [cat5chat1, cat5chat2, cat5chat3, cat5chat4, cat5chat5, cat5chat6]

        cat6chat1 = request.POST['cat6chat1']
        cat6chat2 = request.POST['cat6chat2']
        cat6chat3 = request.POST['cat6chat3']
        cat6chat4 = request.POST['cat6chat4']
        cat6chat5 = request.POST['cat6chat5']
        cat6chat6 = request.POST['cat6chat6']
        cat6 = [cat6chat1, cat6chat2, cat6chat3, cat6chat4, cat6chat5, cat6chat6]

        cat7chat1 = request.POST['cat7chat1']
        cat7chat2 = request.POST['cat7chat2']
        cat7chat3 = request.POST['cat7chat3']
        cat7chat4 = request.POST['cat7chat4']
        cat7chat5 = request.POST['cat7chat5']
        cat7chat6 = request.POST['cat7chat6']
        cat7 = [cat7chat1, cat7chat2, cat7chat3, cat7chat4, cat7chat5, cat7chat6]

        cat8chat1 = request.POST['cat8chat1']
        cat8chat2 = request.POST['cat8chat2']
        cat8chat3 = request.POST['cat8chat3']
        cat8chat4 = request.POST['cat8chat4']
        cat8chat5 = request.POST['cat8chat5']
        cat8chat6 = request.POST['cat8chat6']
        cat8 = [cat8chat1, cat8chat2, cat8chat3, cat8chat4, cat8chat5, cat8chat6]

        cat9chat1 = request.POST['cat9chat1']
        cat9chat2 = request.POST['cat9chat2']
        cat9chat3 = request.POST['cat9chat3']
        cat9chat4 = request.POST['cat9chat4']
        cat9chat5 = request.POST['cat9chat5']
        cat9chat6 = request.POST['cat9chat6']
        cat9 = [cat9chat1, cat9chat2, cat9chat3, cat9chat4, cat9chat5, cat9chat6]

        cat10chat1 = request.POST['cat10chat1']
        cat10chat2 = request.POST['cat10chat2']
        cat10chat3 = request.POST['cat10chat3']
        cat10chat4 = request.POST['cat10chat4']
        cat10chat5 = request.POST['cat10chat5']
        cat10chat6 = request.POST['cat10chat6']
        cat10 = [cat10chat1, cat10chat2, cat10chat3, cat10chat4, cat10chat5, cat10chat6]

        cat11chat1 = request.POST['cat11chat1']
        cat11chat2 = request.POST['cat11chat2']
        cat11chat3 = request.POST['cat11chat3']
        cat11chat4 = request.POST['cat11chat4']
        cat11chat5 = request.POST['cat11chat5']
        cat11chat6 = request.POST['cat11chat6']
        cat11 = [cat11chat1, cat11chat2, cat11chat3, cat11chat4, cat11chat5, cat11chat6]

        cat12chat1 = request.POST['cat12chat1']
        cat12chat2 = request.POST['cat12chat2']
        cat12chat3 = request.POST['cat12chat3']
        cat12chat4 = request.POST['cat12chat4']
        cat12chat5 = request.POST['cat12chat5']
        cat12chat6 = request.POST['cat12chat6']
        cat12 = [cat12chat1, cat12chat2, cat12chat3, cat12chat4, cat12chat5, cat12chat6]

        cat13chat1 = request.POST['cat13chat1']
        cat13chat2 = request.POST['cat13chat2']
        cat13chat3 = request.POST['cat13chat3']
        cat13chat4 = request.POST['cat13chat4']
        cat13chat5 = request.POST['cat13chat5']
        cat13chat6 = request.POST['cat13chat6']
        cat13 = [cat13chat1, cat13chat2, cat13chat3, cat13chat4, cat13chat5, cat13chat6]

        cat14chat1 = request.POST['cat14chat1']
        cat14chat2 = request.POST['cat14chat2']
        cat14chat3 = request.POST['cat14chat3']
        cat14chat4 = request.POST['cat14chat4']
        cat14chat5 = request.POST['cat14chat5']
        cat14chat6 = request.POST['cat14chat6']
        cat14 = [cat14chat1, cat14chat2, cat14chat3, cat14chat4, cat14chat5, cat14chat6]

        cat15chat1 = request.POST['cat15chat1']
        cat15chat2 = request.POST['cat15chat2']
        cat15chat3 = request.POST['cat15chat3']
        cat15chat4 = request.POST['cat15chat4']
        cat15chat5 = request.POST['cat15chat5']
        cat15chat6 = request.POST['cat15chat6']
        cat15 = [cat15chat1, cat15chat2, cat15chat3, cat15chat4, cat15chat5, cat15chat6]

        cat16chat1 = request.POST['cat16chat1']
        cat16chat2 = request.POST['cat16chat2']
        cat16chat3 = request.POST['cat16chat3']
        cat16chat4 = request.POST['cat16chat4']
        cat16chat5 = request.POST['cat16chat5']
        cat16chat6 = request.POST['cat16chat6']
        ######## DOnE #########################

        cat1chat1cs = request.POST['cat1chat1cs']
        cat1chat2cs = request.POST['cat1chat2cs']
        cat1chat3cs = request.POST['cat1chat3cs']
        cat1chat4cs = request.POST['cat1chat4cs']
        cat1chat5cs = request.POST['cat1chat5cs']
        cat1chat6cs = request.POST['cat1chat6cs']

        cat1chat1cy = request.POST['cat1chat1cy']
        cat1chat2cy = request.POST['cat1chat2cy']
        cat1chat3cy = request.POST['cat1chat3cy']
        cat1chat4cy = request.POST['cat1chat4cy']
        cat1chat5cy = request.POST['cat1chat5cy']
        cat1chat6cy = request.POST['cat1chat6cy']

        cat2chat1cs = request.POST['cat2chat1cs']
        cat2chat2cs = request.POST['cat2chat2cs']
        cat2chat3cs = request.POST['cat2chat3cs']
        cat2chat4cs = request.POST['cat2chat4cs']
        cat2chat5cs = request.POST['cat2chat5cs']
        cat2chat6cs = request.POST['cat2chat6cs']

        cat2chat1cy = request.POST['cat2chat1cy']
        cat2chat2cy = request.POST['cat2chat2cy']
        cat2chat3cy = request.POST['cat2chat3cy']
        cat2chat4cy = request.POST['cat2chat4cy']
        cat2chat5cy = request.POST['cat2chat5cy']
        cat2chat6cy = request.POST['cat2chat6cy']

        cat3chat1cs = request.POST['cat3chat1cs']
        cat3chat2cs = request.POST['cat3chat2cs']
        cat3chat3cs = request.POST['cat3chat3cs']
        cat3chat4cs = request.POST['cat3chat4cs']
        cat3chat5cs = request.POST['cat3chat5cs']
        cat3chat6cs = request.POST['cat3chat6cs']

        cat3chat1cy = request.POST['cat3chat1cy']
        cat3chat2cy = request.POST['cat3chat2cy']
        cat3chat3cy = request.POST['cat3chat3cy']
        cat3chat4cy = request.POST['cat3chat4cy']
        cat3chat5cy = request.POST['cat3chat5cy']
        cat3chat6cy = request.POST['cat3chat6cy']

        cat4chat1cs = request.POST['cat4chat1cs']
        cat4chat2cs = request.POST['cat4chat2cs']
        cat4chat3cs = request.POST['cat4chat3cs']
        cat4chat4cs = request.POST['cat4chat4cs']
        cat4chat5cs = request.POST['cat4chat5cs']
        cat4chat6cs = request.POST['cat4chat6cs']

        cat4chat1cy = request.POST['cat4chat1cy']
        cat4chat2cy = request.POST['cat4chat2cy']
        cat4chat3cy = request.POST['cat4chat3cy']
        cat4chat4cy = request.POST['cat4chat4cy']
        cat4chat5cy = request.POST['cat4chat5cy']
        cat4chat6cy = request.POST['cat4chat6cy']

        cat5chat1cs = request.POST['cat5chat1cs']
        cat5chat2cs = request.POST['cat5chat2cs']
        cat5chat3cs = request.POST['cat5chat3cs']
        cat5chat4cs = request.POST['cat5chat4cs']
        cat5chat5cs = request.POST['cat5chat5cs']
        cat5chat6cs = request.POST['cat5chat6cs']

        cat5chat1cy = request.POST['cat5chat1cy']
        cat5chat2cy = request.POST['cat5chat2cy']
        cat5chat3cy = request.POST['cat5chat3cy']
        cat5chat4cy = request.POST['cat5chat4cy']
        cat5chat5cy = request.POST['cat5chat5cy']
        cat5chat6cy = request.POST['cat5chat6cy']

        cat6chat1cs = request.POST['cat6chat1cs']
        cat6chat2cs = request.POST['cat6chat2cs']
        cat6chat3cs = request.POST['cat6chat3cs']
        cat6chat4cs = request.POST['cat6chat4cs']
        cat6chat5cs = request.POST['cat6chat5cs']
        cat6chat6cs = request.POST['cat6chat6cs']

        cat6chat1cy = request.POST['cat6chat1cy']
        cat6chat2cy = request.POST['cat6chat2cy']
        cat6chat3cy = request.POST['cat6chat3cy']
        cat6chat4cy = request.POST['cat6chat4cy']
        cat6chat5cy = request.POST['cat6chat5cy']
        cat6chat6cy = request.POST['cat6chat6cy']

        cat7chat1cs = request.POST['cat7chat1cs']
        cat7chat2cs = request.POST['cat7chat2cs']
        cat7chat3cs = request.POST['cat7chat3cs']
        cat7chat4cs = request.POST['cat7chat4cs']
        cat7chat5cs = request.POST['cat7chat5cs']
        cat7chat6cs = request.POST['cat7chat6cs']

        cat7chat1cy = request.POST['cat7chat1cy']
        cat7chat2cy = request.POST['cat7chat2cy']
        cat7chat3cy = request.POST['cat7chat3cy']
        cat7chat4cy = request.POST['cat7chat4cy']
        cat7chat5cy = request.POST['cat7chat5cy']
        cat7chat6cy = request.POST['cat7chat6cy']

        cat8chat1cs = request.POST['cat8chat1cs']
        cat8chat2cs = request.POST['cat8chat2cs']
        cat8chat3cs = request.POST['cat8chat3cs']
        cat8chat4cs = request.POST['cat8chat4cs']
        cat8chat5cs = request.POST['cat8chat5cs']
        cat8chat6cs = request.POST['cat8chat6cs']

        cat8chat1cy = request.POST['cat8chat1cy']
        cat8chat2cy = request.POST['cat8chat2cy']
        cat8chat3cy = request.POST['cat8chat3cy']
        cat8chat4cy = request.POST['cat8chat4cy']
        cat8chat5cy = request.POST['cat8chat5cy']
        cat8chat6cy = request.POST['cat8chat6cy']

        cat9chat1cs = request.POST['cat9chat1cs']
        cat9chat2cs = request.POST['cat9chat2cs']
        cat9chat3cs = request.POST['cat9chat3cs']
        cat9chat4cs = request.POST['cat9chat4cs']
        cat9chat5cs = request.POST['cat9chat5cs']
        cat9chat6cs = request.POST['cat9chat6cs']

        cat9chat1cy = request.POST['cat9chat1cy']
        cat9chat2cy = request.POST['cat9chat2cy']
        cat9chat3cy = request.POST['cat9chat3cy']
        cat9chat4cy = request.POST['cat9chat4cy']
        cat9chat5cy = request.POST['cat9chat5cy']
        cat9chat6cy = request.POST['cat9chat6cy']

        cat10chat1cs = request.POST['cat10chat1cs']
        cat10chat2cs = request.POST['cat10chat2cs']
        cat10chat3cs = request.POST['cat10chat3cs']
        cat10chat4cs = request.POST['cat10chat4cs']
        cat10chat5cs = request.POST['cat10chat5cs']
        cat10chat6cs = request.POST['cat10chat6cs']

        cat10chat1cy = request.POST['cat10chat1cy']
        cat10chat2cy = request.POST['cat10chat2cy']
        cat10chat3cy = request.POST['cat10chat3cy']
        cat10chat4cy = request.POST['cat10chat4cy']
        cat10chat5cy = request.POST['cat10chat5cy']
        cat10chat6cy = request.POST['cat10chat6cy']

        cat11chat1cs = request.POST['cat11chat1cs']
        cat11chat2cs = request.POST['cat11chat2cs']
        cat11chat3cs = request.POST['cat11chat3cs']
        cat11chat4cs = request.POST['cat11chat4cs']
        cat11chat5cs = request.POST['cat11chat5cs']
        cat11chat6cs = request.POST['cat11chat6cs']

        cat11chat1cy = request.POST['cat11chat1cy']
        cat11chat2cy = request.POST['cat11chat2cy']
        cat11chat3cy = request.POST['cat11chat3cy']
        cat11chat4cy = request.POST['cat11chat4cy']
        cat11chat5cy = request.POST['cat11chat5cy']
        cat11chat6cy = request.POST['cat11chat6cy']

        cat12chat1cs = request.POST['cat12chat1cs']
        cat12chat2cs = request.POST['cat12chat2cs']
        cat12chat3cs = request.POST['cat12chat3cs']
        cat12chat4cs = request.POST['cat12chat4cs']
        cat12chat5cs = request.POST['cat12chat5cs']
        cat12chat6cs = request.POST['cat12chat6cs']

        cat12chat1cy = request.POST['cat12chat1cy']
        cat12chat2cy = request.POST['cat12chat2cy']
        cat12chat3cy = request.POST['cat12chat3cy']
        cat12chat4cy = request.POST['cat12chat4cy']
        cat12chat5cy = request.POST['cat12chat5cy']
        cat12chat6cy = request.POST['cat12chat6cy']

        cat13chat1cs = request.POST['cat13chat1cs']
        cat13chat2cs = request.POST['cat13chat2cs']
        cat13chat3cs = request.POST['cat13chat3cs']
        cat13chat4cs = request.POST['cat13chat4cs']
        cat13chat5cs = request.POST['cat13chat5cs']
        cat13chat6cs = request.POST['cat13chat6cs']

        cat13chat1cy = request.POST['cat13chat1cy']
        cat13chat2cy = request.POST['cat13chat2cy']
        cat13chat3cy = request.POST['cat13chat3cy']
        cat13chat4cy = request.POST['cat13chat4cy']
        cat13chat5cy = request.POST['cat13chat5cy']
        cat13chat6cy = request.POST['cat13chat6cy']

        cat14chat1cs = request.POST['cat14chat1cs']
        cat14chat2cs = request.POST['cat14chat2cs']
        cat14chat3cs = request.POST['cat14chat3cs']
        cat14chat4cs = request.POST['cat14chat4cs']
        cat14chat5cs = request.POST['cat14chat5cs']
        cat14chat6cs = request.POST['cat14chat6cs']

        cat14chat1cy = request.POST['cat14chat1cy']
        cat14chat2cy = request.POST['cat14chat2cy']
        cat14chat3cy = request.POST['cat14chat3cy']
        cat14chat4cy = request.POST['cat14chat4cy']
        cat14chat5cy = request.POST['cat14chat5cy']
        cat14chat6cy = request.POST['cat14chat6cy']

        cat15chat1cs = request.POST['cat15chat1cs']
        cat15chat2cs = request.POST['cat15chat2cs']
        cat15chat3cs = request.POST['cat15chat3cs']
        cat15chat4cs = request.POST['cat15chat4cs']
        cat15chat5cs = request.POST['cat15chat5cs']
        cat15chat6cs = request.POST['cat15chat6cs']

        cat15chat1cy = request.POST['cat15chat1cy']
        cat15chat2cy = request.POST['cat15chat2cy']
        cat15chat3cy = request.POST['cat15chat3cy']
        cat15chat4cy = request.POST['cat15chat4cy']
        cat15chat5cy = request.POST['cat15chat5cy']
        cat15chat6cy = request.POST['cat15chat6cy']

        cat16chat1cs = request.POST['cat16chat1cs']
        cat16chat2cs = request.POST['cat16chat2cs']
        cat16chat3cs = request.POST['cat16chat3cs']
        cat16chat4cs = request.POST['cat16chat4cs']
        cat16chat5cs = request.POST['cat16chat5cs']
        cat16chat6cs = request.POST['cat16chat6cs']

        cat16chat1cy = request.POST['cat16chat1cy']
        cat16chat2cy = request.POST['cat16chat2cy']
        cat16chat3cy = request.POST['cat16chat3cy']
        cat16chat4cy = request.POST['cat16chat4cy']
        cat16chat5cy = request.POST['cat16chat5cy']
        cat16chat6cy = request.POST['cat16chat6cy']

        def scoreCalc(lst):
            ycount = lst.count('y')
            pcount = lst.count('p')
            fcount = lst.count('n')
            nacount = lst.count('NA')
            cat1score = (ycount + pcount) / 6 * 100

            return cat1score

        def autoFailCalculation(a, b, lst):

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

        cat1fscore = autoFailCalculation(0.025, 0.05, cat1)
        cat2fscore = autoFailCalculation(0.025, 0.05, cat2)

        cat3fscore = autoFailCalculation(0.05, 0.1, cat3)
        cat4fscore = autoFailCalculation(0.075, 0.125, cat4)

        cat5fscore = autoFailCalculation(0.03, 0.05, cat5)
        cat6fscore = autoFailCalculation(0.03, 0.05, cat6)
        cat7fscore = autoFailCalculation(0.03, 0.05, cat7)
        cat8fscore = autoFailCalculation(0.03, 0.05, cat8)

        cat9fscore = autoFailCalculation(0.15, 0.3, cat9)
        cat10fscore = autoFailCalculation(0.025, 0.05, cat10)

        cat11fscore = autoFailCalculation(0.025, 0.05, cat11)
        cat13fscore = autoFailCalculation(0.025, 0.05, cat13)

        cat14fscore = autoFailCalculation(0.025, 0.05, cat14)
        cat15fscore = autoFailCalculation(0.025, 0.05, cat15)

        total_failing_score = cat1fscore + cat2fscore + cat3fscore + cat4fscore + cat5fscore + cat6fscore + \
                              cat7fscore + cat8fscore + cat9fscore + cat10fscore + \
                              cat11fscore + cat13fscore + \
                              cat14fscore + cat15fscore

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
        cat15score = scoreCalc(cat15)

        ######### chat 1 calculation  ##############
        total_score = 293

        def catAndTotalScore(c, tot, score):

            if c == 'y':
                c = score
                tot = tot
                return (c, tot)
            elif c == 'n':
                c = 0
                tot = tot
                return (c, tot)
            elif c == 'p':
                c = 0
                tot = tot - score
                return (c, tot)
            else:
                c = score
                tot = tot
                return (c, tot)

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
        timing_chat1 = cat11chat1score + cat12chat1score + cat13chat1score

        cat14chat1score, total_score = catAndTotalScore(cat14chat1, total_score, 10)
        cat15chat1score, total_score = catAndTotalScore(cat15chat1, total_score, 10)
        ce_chat1 = cat14chat1score + cat15chat1score

        if cat16chat1 == 'y':
            autofail_chat1 = (greeting_chat1 + qn_chat1 + lead_chat1 + lf_chat1 + timing_chat1 + ce_chat1) * (-1)
        else:
            autofail_chat1 = 0

        chat1_total = cat1chat1score + cat2chat1score + cat3chat1score + cat4chat1score + cat5chat1score + cat6chat1score + cat7chat1score + cat8chat1score + cat9chat1score + cat10chat1score + cat11chat1score + cat12chat1score + cat13chat1score + cat14chat1score + cat15chat1score
        chat1_total += autofail_chat1
        chat1_total_score = (chat1_total / total_score) * 100
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

        total_chat_sum = chat1_total_score + chat2_total_score + chat3_total_score + \
                         chat4_total_score + chat5_total_score + chat6_total_score

        total_chat_score = total_chat_sum / 6

        total_failing_perc = total_failing_score * 100
        total_audit_score = total_chat_score - total_failing_perc
        total_audit_score = round(total_audit_score)

        category = 'Gubagoo'
        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        trans_date = request.POST['trans_date']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        zone = request.POST['zone']

        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager
        try:
            manager_emp_id_obj = Profile.objects.get(emp_name=manager)
            manager_emp_id = manager_emp_id_obj.emp_id
            manager_name = manager

        except Profile.DoesNotExist:
            manager_emp_id = 0
            manager_name = manager

        added_by = request.user.profile.emp_name
        week = request.POST['week']
        am = request.POST['am']

        fatal_list = [cat16chat1, cat16chat2, cat16chat3, cat16chat4, cat16chat5, cat16chat6]

        fatal_list_count = []
        for i in fatal_list:
            if i == 'y':
                fatal_list_count.append(i)

        no_of_fatals = len(fatal_list_count)
        ####################################################
        if cat16chat1 == 'y' or cat16chat2 == 'y' or cat16chat3 == 'y' or cat16chat4 == 'y' or cat16chat5 == 'y' or cat16chat6 == 'y':
            fatal = True
        else:
            fatal = False

        gubagoo = GubagooAuditForm(

            cat7chat1cy=cat7chat1cy,
            cat7chat2cy=cat7chat2cy,
            cat7chat3cy=cat7chat3cy,
            cat7chat4cy=cat7chat4cy,
            cat7chat5cy=cat7chat5cy,
            cat7chat6cy=cat7chat6cy,

            cat8chat1cs=cat8chat1cs,
            cat8chat2cs=cat8chat2cs,
            cat8chat3cs=cat8chat3cs,
            cat8chat4cs=cat8chat4cs,
            cat8chat5cs=cat8chat5cs,
            cat8chat6cs=cat8chat6cs,

            cat8chat1cy=cat8chat1cy,
            cat8chat2cy=cat8chat2cy,
            cat8chat3cy=cat8chat3cy,
            cat8chat4cy=cat8chat4cy,
            cat8chat5cy=cat8chat5cy,
            cat8chat6cy=cat8chat6cy,

            cat9chat1cs=cat9chat1cs,
            cat9chat2cs=cat9chat2cs,
            cat9chat3cs=cat9chat3cs,
            cat9chat4cs=cat9chat4cs,
            cat9chat5cs=cat9chat5cs,
            cat9chat6cs=cat9chat6cs,

            cat9chat1cy=cat9chat1cy,
            cat9chat2cy=cat9chat2cy,
            cat9chat3cy=cat9chat3cy,
            cat9chat4cy=cat9chat4cy,
            cat9chat5cy=cat9chat5cy,
            cat9chat6cy=cat9chat6cy,

            cat10chat1cs=cat10chat1cs,
            cat10chat2cs=cat10chat2cs,
            cat10chat3cs=cat10chat3cs,
            cat10chat4cs=cat10chat4cs,
            cat10chat5cs=cat10chat5cs,
            cat10chat6cs=cat10chat6cs,

            cat10chat1cy=cat10chat1cy,
            cat10chat2cy=cat10chat2cy,
            cat10chat3cy=cat10chat3cy,
            cat10chat4cy=cat10chat4cy,
            cat10chat5cy=cat10chat5cy,
            cat10chat6cy=cat10chat6cy,

            cat11chat1cs=cat11chat1cs,
            cat11chat2cs=cat11chat2cs,
            cat11chat3cs=cat11chat3cs,
            cat11chat4cs=cat11chat4cs,
            cat11chat5cs=cat11chat5cs,
            cat11chat6cs=cat11chat6cs,

            cat11chat1cy=cat11chat1cy,
            cat11chat2cy=cat11chat2cy,
            cat11chat3cy=cat11chat3cy,
            cat11chat4cy=cat11chat4cy,
            cat11chat5cy=cat11chat5cy,
            cat11chat6cy=cat11chat6cy,

            cat12chat1cs=cat12chat1cs,
            cat12chat2cs=cat12chat2cs,
            cat12chat3cs=cat12chat3cs,
            cat12chat4cs=cat12chat4cs,
            cat12chat5cs=cat12chat5cs,
            cat12chat6cs=cat12chat6cs,

            cat12chat1cy=cat12chat1cy,
            cat12chat2cy=cat12chat2cy,
            cat12chat3cy=cat12chat3cy,
            cat12chat4cy=cat12chat4cy,
            cat12chat5cy=cat12chat5cy,
            cat12chat6cy=cat12chat6cy,

            cat13chat1cs=cat13chat1cs,
            cat13chat2cs=cat13chat2cs,
            cat13chat3cs=cat13chat3cs,
            cat13chat4cs=cat13chat4cs,
            cat13chat5cs=cat13chat5cs,
            cat13chat6cs=cat13chat6cs,

            cat13chat1cy=cat13chat1cy,
            cat13chat2cy=cat13chat2cy,
            cat13chat3cy=cat13chat3cy,
            cat13chat4cy=cat13chat4cy,
            cat13chat5cy=cat13chat5cy,
            cat13chat6cy=cat13chat6cy,

            cat14chat1cs=cat14chat1cs,
            cat14chat2cs=cat14chat2cs,
            cat14chat3cs=cat14chat3cs,
            cat14chat4cs=cat14chat4cs,
            cat14chat5cs=cat14chat5cs,
            cat14chat6cs=cat14chat6cs,

            cat14chat1cy=cat14chat1cy,
            cat14chat2cy=cat14chat2cy,
            cat14chat3cy=cat14chat3cy,
            cat14chat4cy=cat14chat4cy,
            cat14chat5cy=cat14chat5cy,
            cat14chat6cy=cat14chat6cy,

            cat15chat1cs=cat15chat1cs,
            cat15chat2cs=cat15chat2cs,
            cat15chat3cs=cat15chat3cs,
            cat15chat4cs=cat15chat4cs,
            cat15chat5cs=cat15chat5cs,
            cat15chat6cs=cat15chat6cs,

            cat15chat1cy=cat15chat1cy,
            cat15chat2cy=cat15chat2cy,
            cat15chat3cy=cat15chat3cy,
            cat15chat4cy=cat15chat4cy,
            cat15chat5cy=cat15chat5cy,
            cat15chat6cy=cat15chat6cy,

            cat16chat1cs=cat16chat1cs,
            cat16chat2cs=cat16chat2cs,
            cat16chat3cs=cat16chat3cs,
            cat16chat4cs=cat16chat4cs,
            cat16chat5cs=cat16chat5cs,
            cat16chat6cs=cat16chat6cs,

            cat16chat1cy=cat16chat1cy,
            cat16chat2cy=cat16chat2cy,
            cat16chat3cy=cat16chat3cy,
            cat16chat4cy=cat16chat4cy,
            cat16chat5cy=cat16chat5cy,
            cat16chat6cy=cat16chat6cy,

            cat1fscore=cat1fscore,
            cat2fscore=cat2fscore,
            cat3fscore=cat3fscore,
            cat4fscore=cat4fscore,
            cat5fscore=cat5fscore,

            cat6fscore=cat6fscore,
            cat7fscore=cat7fscore,
            cat8fscore=cat8fscore,
            cat9fscore=cat9fscore,
            cat10fscore=cat10fscore,
            cat11fscore=cat11fscore,
            cat13fscore=cat13fscore,
            cat14fscore=cat14fscore,
            cat15fscore=cat15fscore,

            total_failing_score=total_failing_score,

            cat1score=cat1score,
            cat2score=cat2score,
            cat3score=cat3score,
            cat4score=cat4score,
            cat5score=cat5score,
            cat6score=cat6score,
            cat7score=cat7score,
            cat8score=cat8score,
            cat9score=cat9score,
            cat10score=cat10score,
            cat11score=cat11score,
            cat12score=cat12score,
            cat13score=cat13score,
            cat14score=cat14score,
            cat15score=cat15score,

            chat1_total_score=chat1_total_score,
            chat2_total_score=chat2_total_score,
            chat3_total_score=chat3_total_score,
            chat4_total_score=chat4_total_score,
            chat5_total_score=chat5_total_score,
            chat6_total_score=chat6_total_score,

            total_failing_perc=total_failing_perc,
            associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
            manager=manager_name, manager_id=manager_emp_id,
            trans_date=trans_date, audit_date=audit_date,
            campaign=campaign, concept=concept, zone=zone,
            added_by=added_by,
            overall_score=total_audit_score, category=category,
            week=week, am=am, fatal_count=no_of_fatals, fatal=fatal
        )

        gubagoo.save()
        gubagoo = GubagooAuditForm.objects.get(id=gubagoo.id)

        gubagoo.chat1_id = chat1_id
        gubagoo.chat2_id = chat2_id
        gubagoo.chat3_id = chat3_id
        gubagoo.chat4_id = chat4_id
        gubagoo.chat5_id = chat5_id
        gubagoo.chat6_id = chat6_id

        gubagoo.cat1chat1 = cat1chat1
        gubagoo.cat1chat2 = cat1chat2
        gubagoo.cat1chat3 = cat1chat3
        gubagoo.cat1chat4 = cat1chat4
        gubagoo.cat1chat5 = cat1chat5
        gubagoo.cat1chat6 = cat1chat6

        gubagoo.cat2chat1 = cat2chat1
        gubagoo.cat2chat2 = cat2chat2
        gubagoo.cat2chat3 = cat2chat3
        gubagoo.cat2chat4 = cat2chat4
        gubagoo.cat2chat5 = cat2chat5
        gubagoo.cat2chat6 = cat2chat6

        gubagoo.cat3chat1 = cat3chat1
        gubagoo.cat3chat2 = cat3chat2
        gubagoo.cat3chat3 = cat3chat3
        gubagoo.cat3chat4 = cat3chat4
        gubagoo.cat3chat5 = cat3chat5
        gubagoo.cat3chat6 = cat3chat6

        gubagoo.cat4chat1 = cat4chat1
        gubagoo.cat4chat2 = cat4chat2
        gubagoo.cat4chat3 = cat4chat3
        gubagoo.cat4chat4 = cat4chat4
        gubagoo.cat4chat5 = cat4chat5
        gubagoo.cat4chat6 = cat4chat6

        gubagoo.cat5chat1 = cat5chat1
        gubagoo.cat5chat2 = cat5chat2
        gubagoo.cat5chat3 = cat5chat3
        gubagoo.cat5chat4 = cat5chat4
        gubagoo.cat5chat5 = cat5chat5
        gubagoo.cat5chat6 = cat5chat6

        gubagoo.cat6chat1 = cat6chat1
        gubagoo.cat6chat2 = cat6chat2
        gubagoo.cat6chat3 = cat6chat3
        gubagoo.cat6chat4 = cat6chat4
        gubagoo.cat6chat5 = cat6chat5
        gubagoo.cat6chat6 = cat6chat6

        gubagoo.cat7chat1 = cat7chat1
        gubagoo.cat7chat2 = cat7chat2
        gubagoo.cat7chat3 = cat7chat3
        gubagoo.cat7chat4 = cat7chat4
        gubagoo.cat7chat5 = cat7chat5
        gubagoo.cat7chat6 = cat7chat6

        gubagoo.cat8chat1 = cat8chat1
        gubagoo.cat8chat2 = cat8chat2
        gubagoo.cat8chat3 = cat8chat3
        gubagoo.cat8chat4 = cat8chat4
        gubagoo.cat8chat5 = cat8chat5
        gubagoo.cat8chat6 = cat8chat6

        gubagoo.cat9chat1 = cat9chat1
        gubagoo.cat9chat2 = cat9chat2
        gubagoo.cat9chat3 = cat9chat3
        gubagoo.cat9chat4 = cat9chat4
        gubagoo.cat9chat5 = cat9chat5
        gubagoo.cat9chat6 = cat9chat6

        gubagoo.cat10chat1 = cat10chat1
        gubagoo.cat10chat2 = cat10chat2
        gubagoo.cat10chat3 = cat10chat3
        gubagoo.cat10chat4 = cat10chat4
        gubagoo.cat10chat5 = cat10chat5
        gubagoo.cat10chat6 = cat10chat6

        gubagoo.cat11chat1 = cat11chat1
        gubagoo.cat11chat2 = cat11chat2
        gubagoo.cat11chat3 = cat11chat3
        gubagoo.cat11chat4 = cat11chat4
        gubagoo.cat11chat5 = cat11chat5
        gubagoo.cat11chat6 = cat11chat6

        gubagoo.cat12chat1 = cat12chat1
        gubagoo.cat12chat2 = cat12chat2
        gubagoo.cat12chat3 = cat12chat3
        gubagoo.cat12chat4 = cat12chat4
        gubagoo.cat12chat5 = cat12chat5
        gubagoo.cat12chat6 = cat12chat6

        gubagoo.cat13chat1 = cat13chat1
        gubagoo.cat13chat2 = cat13chat2
        gubagoo.cat13chat3 = cat13chat3
        gubagoo.cat13chat4 = cat13chat4
        gubagoo.cat13chat5 = cat13chat5
        gubagoo.cat13chat6 = cat13chat6

        gubagoo.cat14chat1 = cat14chat1
        gubagoo.cat14chat2 = cat14chat2
        gubagoo.cat14chat3 = cat14chat3
        gubagoo.cat14chat4 = cat14chat4
        gubagoo.cat14chat5 = cat14chat5
        gubagoo.cat14chat6 = cat14chat6

        gubagoo.cat15chat1 = cat15chat1
        gubagoo.cat15chat2 = cat15chat2
        gubagoo.cat15chat3 = cat15chat3
        gubagoo.cat15chat4 = cat15chat4
        gubagoo.cat15chat5 = cat15chat5
        gubagoo.cat15chat6 = cat15chat6

        gubagoo.cat16chat1 = cat16chat1
        gubagoo.cat16chat2 = cat16chat2
        gubagoo.cat16chat3 = cat16chat3
        gubagoo.cat16chat4 = cat16chat4
        gubagoo.cat16chat5 = cat16chat5
        gubagoo.cat16chat6 = cat16chat6

        gubagoo.cat1chat1cs = cat1chat1cs
        gubagoo.cat1chat2cs = cat1chat2cs
        gubagoo.cat1chat3cs = cat1chat3cs
        gubagoo.cat1chat4cs = cat1chat4cs
        gubagoo.cat1chat5cs = cat1chat5cs
        gubagoo.cat1chat6cs = cat1chat6cs

        gubagoo.cat1chat1cy = cat1chat1cy
        gubagoo.cat1chat2cy = cat1chat2cy
        gubagoo.cat1chat3cy = cat1chat3cy
        gubagoo.cat1chat4cy = cat1chat4cy
        gubagoo.cat1chat5cy = cat1chat5cy
        gubagoo.cat1chat6cy = cat1chat6cy

        gubagoo.cat2chat1cs = cat2chat1cs
        gubagoo.cat2chat2cs = cat2chat2cs
        gubagoo.cat2chat3cs = cat2chat3cs
        gubagoo.cat2chat4cs = cat2chat4cs
        gubagoo.cat2chat5cs = cat2chat5cs
        gubagoo.cat2chat6cs = cat2chat6cs

        gubagoo.cat2chat1cy = cat2chat1cy
        gubagoo.cat2chat2cy = cat2chat2cy
        gubagoo.cat2chat3cy = cat2chat3cy
        gubagoo.cat2chat4cy = cat2chat4cy
        gubagoo.cat2chat5cy = cat2chat5cy
        gubagoo.cat2chat6cy = cat2chat6cy

        gubagoo.cat3chat1cs = cat3chat1cs
        gubagoo.cat3chat2cs = cat3chat2cs
        gubagoo.cat3chat3cs = cat3chat3cs
        gubagoo.cat3chat4cs = cat3chat4cs
        gubagoo.cat3chat5cs = cat3chat5cs
        gubagoo.cat3chat6cs = cat3chat6cs

        gubagoo.cat3chat1cy = cat3chat1cy
        gubagoo.cat3chat2cy = cat3chat2cy
        gubagoo.cat3chat3cy = cat3chat3cy
        gubagoo.cat3chat4cy = cat3chat4cy
        gubagoo.cat3chat5cy = cat3chat5cy
        gubagoo.cat3chat6cy = cat3chat6cy

        gubagoo.cat4chat1cs = cat4chat1cs
        gubagoo.cat4chat2cs = cat4chat2cs
        gubagoo.cat4chat3cs = cat4chat3cs
        gubagoo.cat4chat4cs = cat4chat4cs
        gubagoo.cat4chat5cs = cat4chat5cs
        gubagoo.cat4chat6cs = cat4chat6cs

        gubagoo.cat4chat1cy = cat4chat1cy
        gubagoo.cat4chat2cy = cat4chat2cy
        gubagoo.cat4chat3cy = cat4chat3cy
        gubagoo.cat4chat4cy = cat4chat4cy
        gubagoo.cat4chat5cy = cat4chat5cy
        gubagoo.cat4chat6cy = cat4chat6cy

        gubagoo.cat5chat1cs = cat5chat1cs
        gubagoo.cat5chat2cs = cat5chat2cs
        gubagoo.cat5chat3cs = cat5chat3cs
        gubagoo.cat5chat4cs = cat5chat4cs
        gubagoo.cat5chat5cs = cat5chat5cs
        gubagoo.cat5chat6cs = cat5chat6cs

        gubagoo.cat5chat1cy = cat5chat1cy
        gubagoo.cat5chat2cy = cat5chat2cy
        gubagoo.cat5chat3cy = cat5chat3cy
        gubagoo.cat5chat4cy = cat5chat4cy
        gubagoo.cat5chat5cy = cat5chat5cy
        gubagoo.cat5chat6cy = cat5chat6cy

        gubagoo.cat6chat1cs = cat6chat1cs
        gubagoo.cat6chat2cs = cat6chat2cs
        gubagoo.cat6chat3cs = cat6chat3cs
        gubagoo.cat6chat4cs = cat6chat4cs
        gubagoo.cat6chat5cs = cat6chat5cs
        gubagoo.cat6chat6cs = cat6chat6cs

        gubagoo.cat6chat1cy = cat6chat1cy
        gubagoo.cat6chat2cy = cat6chat2cy
        gubagoo.cat6chat3cy = cat6chat3cy
        gubagoo.cat6chat4cy = cat6chat4cy
        gubagoo.cat6chat5cy = cat6chat5cy
        gubagoo.cat6chat6cy = cat6chat6cy

        gubagoo.cat7chat1cs = cat7chat1cs
        gubagoo.cat7chat2cs = cat7chat2cs
        gubagoo.cat7chat3cs = cat7chat3cs
        gubagoo.cat7chat4cs = cat7chat4cs
        gubagoo.cat7chat5cs = cat7chat5cs
        gubagoo.cat7chat6cs = cat7chat6cs

        gubagoo.save()
        return redirect('/employees/qahome')


def practoNewVersion(request):
    if request.method == 'POST':

        # Training
        training_status = request.POST['training']
        if training_status == 'yes':
            training = 'Yes'
        elif training_status == 'no':
            training = 'No'

        p_1 = int(request.POST['p1'])
        p_2 = int(request.POST['p2'])
        p_3 = int(request.POST['p3'])
        p_4 = int(request.POST['p4'])
        p_5 = int(request.POST['p5'])
        p_6 = int(request.POST['p6'])
        p_7 = int(request.POST['p7'])
        p_8 = int(request.POST['p8'])
        p_9 = int(request.POST['p9'])
        p_10 = int(request.POST['p10'])
        p_11 = int(request.POST['p11'])
        p_12 = int(request.POST['p12'])
        p_13 = int(request.POST['p13'])
        p_14 = int(request.POST['p14'])
        p_15 = int(request.POST['p15'])
        p_16 = int(request.POST['p16'])
        p_17 = int(request.POST['p17'])

        # Compliance
        compliance_1 = request.POST['fatal1']
        compliance_2 = request.POST['fatal2']

        lst = [p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8, p_9, p_10, p_11, p_12, p_13, p_14, p_15, p_16, p_17, ]

        total_score = sum(lst)

        category = 'Practo'
        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        conversation_id = request.POST['customer']
        customer_contact = request.POST['customercontact']
        trans_date = request.POST['trans_date']
        audit_date = request.POST['auditdate']
        campaign = request.POST['campaign']
        concept = request.POST['concept']
        zone = request.POST['zone']
        duration = (int(request.POST['durationh']) * 3600) + (int(request.POST['durationm']) * 60) + int(
            request.POST['durations'])

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        try:
            manager_emp_id_obj = Profile.objects.get(emp_name=manager)
            manager_emp_id = manager_emp_id_obj.emp_id
            manager_name = manager

        except Profile.DoesNotExist:
            manager_emp_id = 0
            manager_name = manager

        #################################################
        fatal_list = [compliance_1, compliance_2]
        fatal_list_count = []
        for i in fatal_list:
            if i == 'fatal':
                fatal_list_count.append(i)

        no_of_fatals = len(fatal_list_count)
        ####################################################
        if compliance_1 == 'fatal' or compliance_2 == 'fatal':
            overall_score = 0
            fatal = True
        else:
            overall_score = total_score
            fatal = False

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        week = request.POST['week']
        am = request.POST['am']

        domestic = PractoNewVersion(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                    manager=manager_name, manager_id=manager_emp_id,
                                    trans_date=trans_date, audit_date=audit_date, conversation_id=conversation_id,
                                    customer_contact=customer_contact,
                                    campaign=campaign, concept=concept, zone=zone, duration=duration,

                                    p_1=p_1, p_2=p_2, p_3=p_3, p_4=p_4, p_5=p_5, p_6=p_6, p_7=p_7,
                                    p_8=p_8, p_9=p_9, p_10=p_10, p_11=p_11, p_12=p_12, p_13=p_13, p_14=p_14,
                                    p_15=p_15, p_16=p_16, p_17=p_17,

                                    # Training
                                    training=training,

                                    compliance_1=compliance_1, compliance_2=compliance_2,
                                    areas_improvement=areas_improvement,
                                    positives=positives, comments=comments,
                                    added_by=added_by,
                                    overall_score=overall_score, category=category,
                                    week=week, am=am, fatal_count=no_of_fatals, fatal=fatal,

                                    )
        domestic.save()
        return redirect('/employees/qahome')


def PractoWithSubCategoryFunc(request):
    if request.method == 'POST':
        p_1 = int(request.POST['p1'])  # Chat Closing
        p1_s1 = request.POST.get("chat_1")
        p1_s2 = request.POST.get("chat_2")
        p1_s3 = request.POST.get("chat_3")
        p1_s4 = request.POST.get("chat_4")
        p1_s5 = request.POST.get("chat_5")
        p1_s6 = request.POST.get("chat_6")
        p_2 = int(request.POST['p2'])  # FRTAT
        p_3 = int(request.POST['p3'])  # Addressing the user/Personalisation of chat
        p3_s1 = request.POST.get("pers_1")
        p3_s2 = request.POST.get("pers_2")
        p3_s3 = request.POST.get("pers_3")
        p3_s4 = request.POST.get("pers_4")
        p3_s5 = request.POST.get("pers_5")
        p3_s6 = request.POST.get("pers_6")
        p_4 = int(request.POST['p4'])  # Assistance & Acknowledgment
        p4_s1 = request.POST.get("assu_1")
        p4_s2 = request.POST.get("assu_2")
        p4_s3 = request.POST.get("assu_3")
        p4_s4 = request.POST.get("assu_4")
        p4_s5 = request.POST.get("assu_5")
        p_5 = int(request.POST['p5'])  # Relevant responses
        p_6 = int(request.POST['p19'])  # Assurance
        p_7 = int(request.POST['p6'])  # Probing
        p7_s1 = request.POST.get("prob_1")
        p7_s2 = request.POST.get("prob_2")
        p7_s3 = request.POST.get("prob_3")
        p7_s4 = request.POST.get("prob_4")
        p_8 = int(request.POST['p7'])  # Interaction: Empathy , Profressional, care
        p8_s1 = request.POST.get("inte_1")
        p8_s2 = request.POST.get("inte_2")
        p8_s3 = request.POST.get("inte_3")
        p8_s4 = request.POST.get("inte_4")
        p8_s5 = request.POST.get("inte_5")
        p8_s6 = request.POST.get("inte_6")
        p8_s7 = request.POST.get("inte_7")
        p_9 = int(request.POST['p8'])  # Grammar
        p9_s1 = request.POST.get("gram_1")
        p9_s2 = request.POST.get("gram_2")
        p9_s3 = request.POST.get("gram_3")
        p9_s4 = request.POST.get("gram_4")
        p9_s5 = request.POST.get("gram_5")
        p9_s6 = request.POST.get("gram_6")
        p_10 = int(request.POST['p10'])  # Being courteous & using plesantries
        p_11 = int(request.POST['p11'])  # Process followed
        p11_s1 = request.POST.get("proc_1")
        p11_s2 = request.POST.get("proc_2")
        p11_s3 = request.POST.get("proc_3")
        p11_s4 = request.POST.get("proc_4")
        p11_s5 = request.POST.get("proc_5")
        p11_s6 = request.POST.get("proc_6")
        p11_s7 = request.POST.get("proc_7")
        p_12 = int(request.POST['p12'])  # Explanation Skills (Being Specific, Reasoning) & Rebuttal Handling
        p_13 = int(request.POST['p13'])  # Sharing the information in a sequential manner
        p_14 = int(request.POST['p14'])  # Case Documentation
        p_15 = int(request.POST['p15'])  # Curation
        p15_s1 = request.POST.get("cura_1")
        p15_s2 = request.POST.get("cura_2")
        p15_s3 = request.POST.get("cura_3")
        p_16 = int(request.POST['p16'])  # Average Speed of Answer
        p_17 = int(request.POST['p17'])  # Chat Hold Procedure &: Taking Permission before putting the chat on hold.
        p17_s1 = request.POST.get("hold_1")
        p17_s2 = request.POST.get("hold_3")
        p17_s3 = request.POST.get("hold_3")
        p17_s4 = request.POST.get("hold_4")
        p_18 = int(request.POST['p18'])  # PE knowledge base adherence
        p18_s1 = request.POST.get("pekb_1")
        p18_s2 = request.POST.get("pekb_2")
        p18_s3 = request.POST.get("pekb_3")
        p18_s4 = request.POST.get("pekb_4")

        # Compliance
        compliance_1 = request.POST['fatal1']  # Expectations: Setting correct expectations about issue resolution
        compliance1_s1 = request.POST.get("expe_1")
        compliance1_s2 = request.POST.get("expe_2")
        compliance1_s3 = request.POST.get("expe_3")
        compliance_2 = request.POST['fatal2']  # ZTP(Zero Tolerance Policy)

        lst = [p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8, p_9, p_10, p_11, p_12, p_13, p_14, p_15, p_16, p_17, p_18]

        total_score = sum(lst)

        category = 'Practo Chat'
        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        case_no = request.POST["case_no"]

        issue_type = request.POST["issue_type"]
        sub_issue_type = request.POST["sub_issue_type"]
        sub_sub_issue_type = request.POST["sub_sub_issue_type"]

        chat_date = request.POST["chat_date"]
        csat = request.POST['csat']
        product = request.POST['product']
        audit_date = request.POST['auditdate']
        concept = request.POST['concept']
        zone = request.POST['zone']
        campaign = request.POST['campaign']
        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        try:
            manager_emp_id_obj = Profile.objects.get(emp_name=manager)
            manager_emp_id = manager_emp_id_obj.emp_id
            manager_name = manager

        except Profile.DoesNotExist:
            manager_emp_id = 0
            manager_name = manager

        #################################################
        fatal_list = [compliance_1, compliance_2]
        fatal_list_count = []
        for i in fatal_list:
            if i == 'fatal':
                fatal_list_count.append(i)

        no_of_fatals = len(fatal_list_count)
        ####################################################
        if compliance_1 == 'fatal' or compliance_2 == 'fatal':
            overall_score = 0
            fatal = True
        else:
            overall_score = total_score
            fatal = False

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        week = request.POST['week']
        am = request.POST['am']

        domestic = NewPractoWithSubCategory(associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
                                            manager=manager_name, manager_id=manager_emp_id, audit_date=audit_date,
                                            concept=concept,
                                            zone=zone, case_no=case_no, issue_type=issue_type, sub_issue=sub_issue_type,
                                            sub_sub_issue=sub_sub_issue_type,
                                            chat_date=chat_date, csat=csat, product=product, campaign=campaign,

                                            p_1=p_1, p_2=p_2, p_3=p_3, p_4=p_4, p_5=p_5, p_6=p_6, p_7=p_7,
                                            p_8=p_8, p_9=p_9, p_10=p_10, p_11=p_11, p_12=p_12, p_13=p_13, p_14=p_14,
                                            p_15=p_15, p_16=p_16, p_17=p_17, p_18=p_18,

                                            p1_s1=p1_s1, p1_s2=p1_s2, p1_s3=p1_s3, p1_s4=p1_s4, p1_s5=p1_s5,
                                            p1_s6=p1_s6,
                                            p3_s1=p3_s1, p3_s2=p3_s2, p3_s3=p3_s3, p3_s4=p3_s4, p3_s5=p3_s5,
                                            p3_s6=p3_s6,
                                            p4_s1=p4_s1, p4_s2=p4_s2, p4_s3=p4_s3, p4_s4=p4_s4, p4_s5=p4_s5,
                                            p7_s1=p7_s1, p7_s2=p7_s2, p7_s3=p7_s3, p7_s4=p7_s4,
                                            p8_s1=p8_s1, p8_s2=p8_s2, p8_s3=p8_s3, p8_s4=p8_s4, p8_s5=p8_s5,
                                            p8_s6=p8_s6, p8_s7=p8_s7,
                                            p9_s1=p9_s1, p9_s2=p9_s2, p9_s3=p9_s3, p9_s4=p9_s4, p9_s5=p9_s5,
                                            p9_s6=p9_s6,
                                            p11_s1=p11_s1, p11_s2=p11_s2, p11_s3=p11_s3, p11_s4=p11_s4, p11_s5=p11_s5,
                                            p11_s6=p11_s6, p11_s7=p11_s7,
                                            p15_s1=p15_s1, p15_s2=p15_s2, p15_s3=p15_s3,
                                            p17_s1=p17_s1, p17_s2=p17_s2, p17_s3=p17_s3, p17_s4=p17_s4,
                                            p18_s1=p18_s1, p18_s2=p18_s2, p18_s3=p18_s3, p18_s4=p18_s4,
                                            compliance1_s1=compliance1_s1, compliance1_s2=compliance1_s2,
                                            compliance1_s3=compliance1_s3,

                                            compliance_1=compliance_1, compliance_2=compliance_2,
                                            areas_improvement=areas_improvement,
                                            positives=positives, comments=comments,
                                            added_by=added_by,
                                            overall_score=overall_score, category=category,
                                            week=week, am=am, fatal_count=no_of_fatals, fatal=fatal,

                                            )
        domestic.save()
        return redirect('/employees/qahome')
    else:
        return render(request, 'mon-forms/practo_chat.html')


def nerotelInbound(request):
    if request.method == 'POST':
        category = 'Nerotel Inbound'
        associate_name = request.POST['empname']
        emp_id = request.POST['empid']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        customer_name = request.POST['customer']
        customer_contact = request.POST['customercontact']
        call_date = request.POST['calldate']
        audit_date = request.POST['auditdate']
        concept = request.POST['concept']
        zone = request.POST['zone']
        call_duration = (int(request.POST['durationh']) * 3600) + (int(request.POST['durationm']) * 60) + int(
            request.POST['durations'])

        #######################################
        prof_obj = Profile.objects.get(emp_id=emp_id)
        manager = prof_obj.manager

        manager_emp_id_obj = Profile.objects.get(emp_name=manager)

        manager_emp_id = manager_emp_id_obj.emp_id
        manager_name = manager
        # Engagement
        eng_1 = int(request.POST['e_1'])
        eng_2 = int(request.POST['e_2'])
        eng_3 = int(request.POST['e_3'])
        eng_4 = int(request.POST['e_4'])
        eng_5 = int(request.POST['e_5'])
        eng_6 = int(request.POST['e_6'])
        eng_7 = int(request.POST['e_7'])
        eng_8 = int(request.POST['e_8'])
        eng_9 = int(request.POST['e_9'])
        eng_total = eng_1 + eng_2 + eng_3 + eng_4 + eng_5 + eng_6 + eng_7 + eng_8 + eng_9
        # Resolution
        res_1 = int(request.POST['res_1'])
        res_2 = int(request.POST['res_2'])
        res_3 = int(request.POST['res_3'])
        res_4 = int(request.POST['res_4'])
        res_total = res_1 + res_2 + res_3 + res_4

        # Business needs
        compliance_1 = int(request.POST['busi_1'])
        compliance_2 = int(request.POST['busi_2'])
        compliance_3 = int(request.POST['busi_3'])
        compliance_4 = int(request.POST['busi_4'])
        com_total = compliance_1 + compliance_2 + compliance_3 + compliance_4

        fatal_list = [compliance_1, compliance_2, compliance_3, compliance_4]
        fatal_list_count = []
        for i in fatal_list:
            if i == 0:
                fatal_list_count.append(i)
        no_of_fatals = len(fatal_list_count)

        if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0 or compliance_4 == 0:
            overall_score = 0
            fatal = True
        else:
            overall_score = eng_total + res_total + com_total
            fatal = False

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name
        week = request.POST['week']
        am = request.POST['am']

        leadsales = NerotelInboundmonform(
            associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
            manager=manager_name, manager_id=manager_emp_id,
            call_date=call_date, audit_date=audit_date, customer_name=customer_name, customer_contact=customer_contact,
            concept=concept, zone=zone, call_duration=call_duration,
            eng_1=eng_1, eng_2=eng_2, eng_3=eng_3, eng_4=eng_4, eng_5=eng_5, eng_6=eng_6, eng_7=eng_7, eng_8=eng_8,
            eng_9=eng_9,
            res_1=res_1, res_2=res_2, res_3=res_3, res_4=res_4,
            compliance_1=compliance_1, compliance_2=compliance_2, compliance_3=compliance_3, compliance_4=compliance_4,
            areas_improvement=areas_improvement,
            positives=positives, comments=comments,
            added_by=added_by,
            overall_score=overall_score, category=category,
            week=week, am=am, fatal_count=no_of_fatals, fatal=fatal,
        )
        leadsales.save()
        return redirect('/employees/qahome')


def spoiledChildEmail(request):
    if request.method == 'POST':

        category = 'Email - Chat'

        emp_id = request.POST['empid']
        associate_name = request.POST['empname']
        zone = request.POST['zone']
        concept = request.POST['concept']
        customer_name = request.POST['customer']
        ticket_id = request.POST['ticketid']
        query_type = request.POST['query_type']
        call_date = request.POST['calldate']
        audit_date = request.POST['auditdate']
        qa = request.POST['qa']
        team_lead = request.POST['tl']
        # mgt
        manager = Profile.objects.get(emp_id=emp_id).manager
        manager_id = Profile.objects.get(emp_name=manager).emp_id
        am = request.POST['am']
        week = request.POST['week']

        campaign = request.POST['campaign']

        # Opening and Closing

        solution_1 = int(request.POST['solution_1'])
        solution_2 = int(request.POST['solution_2'])
        solution_3 = int(request.POST['solution_3'])
        solution_4 = int(request.POST['solution_4'])
        solution_total = solution_1 + solution_2 + solution_3 + solution_4

        # Softskills
        efficiency_1 = int(request.POST['eff_1'])
        efficiency_2 = int(request.POST['eff_2'])
        efficiency_total = efficiency_1 + efficiency_2

        # Compliance
        compliance_1 = int(request.POST['compliance_1'])
        compliance_2 = int(request.POST['compliance_2'])
        compliance_3 = int(request.POST['compliance_3'])

        compliance_total = compliance_1 + compliance_2 + compliance_3

        fatal_list = [compliance_1, compliance_2, compliance_3]
        fatal_list_count = []
        for i in fatal_list:
            if i == 0:
                fatal_list_count.append(i)
        no_of_fatals = len(fatal_list_count)

        if compliance_1 == 0 or compliance_2 == 0 or compliance_3 == 0:
            overall_score = 0
            fatal = True
        else:
            overall_score = solution_total + efficiency_total + compliance_total
            fatal = False

        areas_improvement = request.POST['areaimprovement']
        positives = request.POST['positives']
        comments = request.POST['comments']
        added_by = request.user.profile.emp_name

        spoil = SpoiledChildChatmonform(
            associate_name=associate_name, emp_id=emp_id, qa=qa, team_lead=team_lead,
            manager=manager, manager_id=manager_id,
            chat_date=call_date, audit_date=audit_date, customer_name=customer_name, ticket_id=ticket_id,
            campaign=campaign, concept=concept, zone=zone, query_type=query_type,

            solution_1=solution_1, solution_2=solution_2, solution_3=solution_3, solution_4=solution_4,

            efficiency_1=efficiency_1, efficiency_2=efficiency_2,

            compliance_1=compliance_1, compliance_2=compliance_2, compliance_3=compliance_3,

            solution_total=solution_total, efficiency_total=efficiency_total,
            compliance_total=compliance_total,

            areas_improvement=areas_improvement,
            positives=positives, comments=comments,
            added_by=added_by,
            overall_score=overall_score, category=category,
            week=week, am=am, fatal_count=no_of_fatals, fatal=fatal,
        )
        spoil.save()
        return redirect('/employees/qahome')


############## End Mon Forms ##############################


def processNameChanger(request):
    obj = MonitoringFormLeadsAadhyaSolution.objects.all()
    for i in obj:
        i.process = 'AAdya'
        i.save()


def desiChanger(request):
    empid_list = [2145, 3831]
    for i in empid_list:
        prof = Profile.objects.get(emp_id=i)
        prof.emp_desi = 'QA'
        prof.save()


def addSingleProfile(request):
    emp_id = 6728

    manager = 'Dina'
    profile_object = Profile.objects.get(emp_id=emp_id)
    profile_object.manager = manager
    profile_object.save()


def updateProfile(request):
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['desi']

        emp = Profile.objects.get(id=id)

        emp.emp_name = name
        emp.save()

        return render(request, 'update-profile.html', )
    else:
        profiles = Profile.objects.all()
        data = {'profiles': profiles}
        return render(request, 'update-profile.html', data)


def profileDetailedView(request):
    if request.method == 'POST':
        id = request.POST['id']
        obj = Profile.objects.get(id=id)

        data = {'emp': obj}

        return render(request, 'profile-detailed-view.html', data)


def powerBITest(request):
    return render(request, 'test-powerbi-view.html')


def addtoUserModel(request):
    empobj = ProfileNewtoAddUserandProfile.objects.all()
    for i in empobj:
        user = User.objects.filter(username=i.username)
        if user.exists():
            print(i.emp_name + ' ' + 'exist')
            pass
        else:
            user = User.objects.create_user(id=i.username, username=i.username, password=i.password)
            profile = Profile(id=i.username, emp_name=i.emp_name, emp_id=i.username, emp_desi=i.emp_desi, team=i.team,
                              email=i.email, team_lead=i.team_lead, manager=i.manager, user_id=i.username, am=i.am,
                              process=i.process)
            profile.save()
            print('User and Profile created')


def checkProfile(request):
    profile = Profile.objects.get(emp_id=6043)
    profile.user = 6043
    profile.id = 6043
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
        c = Campaigns.objects.create(name=campaign, type=type)
        c.save()
        return redirect('/add-new-campaign')

    else:
        return render(request, 'add-new-campaign.html')


def deleteData(request):
    ILMakiageEmailChatForm.objects.filter(overall_score=1).delete()
    return redirect('/')

def campaignDetails(request):
    if request.method == 'POST':
        category = request.POST['campaign']

        for i in list_of_monforms:
            obj = i.objects.all()
            if obj.count() > 0:
                if obj[0].process == category:
                    campaign = i
                else:
                    pass
            else:
                pass

        campaigns = Campaigns.objects.all()
        data = {'campaigns': campaigns}
        return render(request, 'all-campaigns.html', data)

    else:
        campaigns = Campaigns.objects.all()
        data = {'campaigns': campaigns}
        return render(request, 'all-campaigns.html', data)


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


def DeleteTestAudits(request):
    for i in list_of_monforms:
        i.objects.filter(Q(added_by='5670') | Q(added_by='Ranjitha M')).delete()
    return redirect('/')


# EDit Team RM


def createUserAndProfile(request):
    emp_id = request.user.profile.emp_id
    if emp_id == 4458 or emp_id == 8413:
        if request.method == 'POST':

            id = request.POST['emp_id']
            user_name = request.POST['user_name']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            emp_name = request.POST['emp_name']
            emp_desi = request.POST['emp_desi']
            process = request.POST['process']
            email = request.POST['email']
            manager = request.POST['manager']
            am = request.POST['am']
            tl = request.POST['tl']
            admin_id = request.POST['admin_id']
            admin_password = request.POST['admin_password']

            if id != user_name:
                messages.info(request, 'Emp ID and Username Must be Same !!!')
                return redirect('/create-user-profile')
            else:
                pass

            if password1 != password2:
                messages.info(request, 'Password not matching !!!')
                return redirect('/create-user-profile')
            else:
                password = password1

            if admin_id == 'ecpl-qms' and admin_password == 'EcplQms2021!':

                user = User.objects.filter(username=id)
                if user.exists():
                    messages.info(request, 'User Already exist !!!')
                    return redirect('/create-user-profile')
                else:

                    user = User.objects.create_user(id=id, username=user_name, password=password)
                    profile = Profile(id=id, emp_name=emp_name, emp_id=id, emp_desi=emp_desi, team=process,
                                      email=email, team_lead=tl, manager=manager, user_id=id, am=am, process=process)
                    user.save()
                    profile.save()

                    add_obj = ProfileCreatedByManagers()
                    add_obj.emp_name = emp_name
                    add_obj.emp_id = id
                    add_obj.created_by = request.user.profile.emp_id
                    add_obj.created_date = datetime.now()
                    add_obj.save()

                    messages.info(request, 'User has been Created, Please try Login now !!!')
                    return redirect('/create-user-profile')

            else:
                messages.info(request, 'Incorrect Admin ID or Password !!!')
                return redirect('/create-user-profile')

        else:

            managers = Profile.objects.filter(
                Q(emp_desi='Team Leader') | Q(emp_desi='AM') | Q(emp_desi='Manager') | Q(emp_desi='SME'))
            ams = Profile.objects.filter(
                Q(emp_desi='Team Leader') | Q(emp_desi='AM') | Q(emp_desi='Manager') | Q(emp_desi='SME'))
            tls = Profile.objects.filter(
                Q(emp_desi='Team Leader') | Q(emp_desi='AM') | Q(emp_desi='Manager') | Q(emp_desi='SME'))

            data = {'managers': managers, 'ams': ams, 'tls': tls}
            return render(request, 'create-user-profile.html', data)
    else:
        messages.error(request, "Unauthorized access!")
        return redirect('/')


def editTeamRMS(request):
    campaigns = Campaigns.objects.all()
    profile = Profile.objects.filter(Q(emp_desi='Team Leader') | Q(emp_desi='AM') | Q(emp_desi='Manager'))

    data = {'campaigns': campaigns, 'profile': profile}
    return render(request, 'edit-team-rms.html', data)


def coachingStatusReportAll(request):
    lst = []
    lst_dispute = []
    for i in list_of_monforms:
        status = i.objects.filter(status=False).values(
            'process').annotate(dcount=Count('status'))
        lst.append(status)

        dispute = i.objects.filter(disput_status=True).values(
            'process').annotate(dcount=Count('disput_status'))
        lst_dispute.append(dispute)

    data = {'status': lst, 'dispute': lst_dispute}

    return render(request, 'coaching-summary-view.html', data)


def coachingStatusCampaignwise(request, campaign):
    def campaignWise(monform):

        emp_wise = monform.objects.filter(status=False).values(
            'associate_name').annotate(dcount=Count('status'))
        data = {'emp_wise': emp_wise, 'campaign': campaign}
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
        return render(request, 'coaching-summary-view-agents.html', data)
    else:
        data = campaignWise(monform)
    return render(request, 'coaching-summary-view-agents.html', data)


def disputeStatusAgents(request, campaign):
    def campaignWise(monform):

        emp_wise = monform.objects.filter(disput_status=True).values(
            'associate_name').annotate(dcount=Count('status'))
        data = {'emp_wise': emp_wise, 'campaign': campaign}
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
        return render(request, 'dispute-summary-view-agents.html', data)
    else:
        data = campaignWise(monform)
    return render(request, 'dispute-summary-view-agents.html', data)


def PasswordReset(request):
    emp = request.user.profile.emp_id
    if emp == 8413 or emp == 4458 or emp == 5670:
        if request.method == 'POST':
            emp_id = request.POST['emp_id']
            new = request.POST['new']
            confirm = request.POST['confirm']
            if new == confirm:
                user = User.objects.get(username=emp_id)
                user.password = make_password(new)
                user.save()
                messages.error(request, 'Password changed successfully!')
                return redirect('/password-reset')
            else:
                messages.error(request, 'Passwords does not match')
                return redirect('/password-reset')
        else:
            profiles = Profile.objects.all()
            data = {'profiles': profiles}
            return render(request, 'password-reset.html', data)
    else:
        messages.error(request, 'Invalid Request!!')
        return redirect('/')


from drf_multiple_model.views import ObjectMultipleModelAPIView
from drf_multiple_model.views import FlatMultipleModelAPIView


class TotalList(FlatMultipleModelAPIView):
    querylist = [
        {'queryset': ChatMonitoringFormPodFather.objects.all(),
         'serializer_class': ChatMonitoringSerializer},

        {'queryset': MonitoringFormLeadsAadhyaSolution.objects.all(),
         'serializer_class': adhyaSerializer},

        {'queryset': AccutimeMonForm.objects.all(),
         'serializer_class': AccutimeMonFormSerializer},

        {'queryset': MonitoringFormLeadsAdvanceConsultants.objects.all(),
         'serializer_class': MonitoringFormLeadsAdvanceConsultantsSerializer},

        {'queryset': MonitoringFormLeadsAllenConsulting.objects.all(),
         'serializer_class': MonitoringFormLeadsAllenConsultingSerializer},

        {'queryset': CamIndustrialMonForm.objects.all(),
         'serializer_class': CamIndustrialMonFormSerializer},

        {'queryset': CitizenCapitalMonForm.objects.all(),
         'serializer_class': CitizenCapitalMonFormSerializer},

        {'queryset': MonitoringFormLeadsCitySecurity.objects.all(),
         'serializer_class': MonitoringFormLeadsCitySecuritySerializer},

        {'queryset': MonitoringFormLeadsCTS.objects.all(),
         'serializer_class': MonitoringFormLeadsCTSSerializer},

        {'queryset': EmbassyLuxuryMonForm.objects.all(),
         'serializer_class': EmbassyLuxuryMonFormSerializer},

        {'queryset': MonitoringFormLeadsGetARates.objects.all(),
         'serializer_class': MonitoringFormLeadsGetARatesSerializer},

        {'queryset': GlydeAppMonForm.objects.all(),
         'serializer_class': GlydeAppMonFormSerializer},

        {'queryset': GoldenEastMonForm.objects.all(),
         'serializer_class': GoldenEastMonFormSerializer},

        {'queryset': IbizMonForm.objects.all(),
         'serializer_class': IbizMonFormSerializer},

        {'queryset': IIBMonForm.objects.all(),
         'serializer_class': IIBMonFormSerializer},

        {'queryset': MonitoringFormLeadsInfothinkLLC.objects.all(),
         'serializer_class': MonitoringFormLeadsInfothinkLLCSerializer},

        {'queryset': MonitoringFormLeadsInsalvage.objects.all(),
         'serializer_class': MonitoringFormLeadsInsalvageSerializer},

        {'queryset': JJStudioMonForm.objects.all(),
         'serializer_class': JJStudioMonFormSerializer},

        {'queryset': KalkiFashions.objects.all(),
         'serializer_class': KalkiFashionsSerializer},

        {'queryset': MonitoringFormLeadsLouisville.objects.all(),
         'serializer_class': MonitoringFormLeadsLouisvilleSerializer},

        {'queryset': MonitoringFormLeadsMedicare.objects.all(),
         'serializer_class': MonitoringFormLeadsMedicareSerializer},

        {'queryset': MicroDistributingMonForm.objects.all(),
         'serializer_class': MicroDistributingMonFormSerializer},

        {'queryset': MillenniumScientificMonForm.objects.all(),
         'serializer_class': MillenniumScientificMonFormSerializer},

        {'queryset': MTCosmeticsMonForm.objects.all(),
         'serializer_class': MTCosmeticsMonFormSerializer},

        {'queryset': NavigatorBioMonForm.objects.all(),
         'serializer_class': NavigatorBioMonFormSerializer},

        {'queryset': OptimalStudentLoanMonForm.objects.all(),
         'serializer_class': OptimalStudentLoanMonFormSerializer},

        {'queryset': ProtostarMonForm.objects.all(),
         'serializer_class': ProtostarMonFormSerializer},

        {'queryset': MonitoringFormLeadsPSECU.objects.all(),
         'serializer_class': MonitoringFormLeadsPSECUSerializer},

        {'queryset': QBIQMonForm.objects.all(),
         'serializer_class': QBIQMonFormSerializer},

        {'queryset': RestaurentSolMonForm.objects.all(),
         'serializer_class': RestaurentSolMonFormSerializer},

        {'queryset': RitBrainMonForm.objects.all(),
         'serializer_class': RitBrainMonFormSerializer},

        {'queryset': RoofWellMonForm.objects.all(),
         'serializer_class': RoofWellMonFormSerializer},

        {'queryset': ScalaMonForm.objects.all(),
         'serializer_class': ScalaMonFormSerializer},

        {'queryset': SolarCampaignMonForm.objects.all(),
         'serializer_class': SolarCampaignMonFormSerializer},

        {'queryset': StandSpotMonForm.objects.all(),
         'serializer_class': StandSpotMonFormSerializer},

        {'queryset': MonitoringFormLeadsSystem4.objects.all(),
         'serializer_class': MonitoringFormLeadsSystem4Serializer},

        {'queryset': MonitoringFormLeadsTentamusFood.objects.all(),
         'serializer_class': MonitoringFormLeadsTentamusFoodSerializer},

        {'queryset': MonitoringFormLeadsTentamusPet.objects.all(),
         'serializer_class': MonitoringFormLeadsTentamusPetSerializer},

        {'queryset': TerraceoLeadMonForm.objects.all(),
         'serializer_class': TerraceoLeadMonFormSerializer},

        {'queryset': UpfrontOnlineLLCMonform.objects.all(),
         'serializer_class': UpfrontOnlineLLCMonformSerializer},

        {'queryset': WTUMonForm.objects.all(),
         'serializer_class': WTUMonFormSerializer},

        {'queryset': YesHealthMolinaMonForm.objects.all(),
         'serializer_class': YesHealthMolinaMonFormSerializer},

        {'queryset': ZeroStressMarketingMonForm.objects.all(),
         'serializer_class': ZeroStressMarketingMonFormSerializer},

        {'queryset': ABHindalcoOutboundMonForm.objects.all(),
         'serializer_class': ABHindalcoOutboundMonFormSerializer},

        {'queryset': AdityaBirlaOutboundMonForm.objects.all(),
         'serializer_class': AdityaBirlaOutboundMonFormSerializer},

        {'queryset': AmerisaveoutboundMonForm.objects.all(),
         'serializer_class': AmerisaveoutboundMonFormSerializer},

        {'queryset': BhagyaLakshmiOutbound.objects.all(),
         'serializer_class': BhagyaLakshmiOutboundSerializer},

        {'queryset': ClearViewOutboundMonForm.objects.all(),
         'serializer_class': ClearViewOutboundMonFormSerializer},

        {'queryset': DanielWellingtonOutboundMonForm.objects.all(),
         'serializer_class': DanielWellingtonOutboundMonFormSerializer},

        {'queryset': DigitalSwissGoldOutboundMonForm.objects.all(),
         'serializer_class': DigitalSwissGoldOutboundMonFormSerializer},

        {'queryset': HealthyplusOutboundMonForm.objects.all(),
         'serializer_class': HealthyplusOutboundMonFormSerializer},

        {'queryset': MaxwellPropertiesOutboundMonForm.objects.all(),
         'serializer_class': MaxwellPropertiesOutboundMonFormSerializer},

        {'queryset': MovementofInsuranceOutboundMonForm.objects.all(),
         'serializer_class': MovementofInsuranceOutboundMonFormSerializer},

        {'queryset': SterlingStrategiesOutboundMonForm.objects.all(),
         'serializer_class': SterlingStrategiesOutboundMonFormSerializer},

        {'queryset': TonnCoaOutboundMonForm.objects.all(),
         'serializer_class': TonnCoaOutboundMonFormSerializer},

        {'queryset': WitDigitalOutboundMonForm.objects.all(),
         'serializer_class': WitDigitalOutboundMonFormSerializer},

        {'queryset': PosTechOutboundMonForm.objects.all(),
         'serializer_class': PosTechOutboundMonFormSerializer},

        {'queryset': SchindlerMediaOutboundMonForm.objects.all(),
         'serializer_class': SchindlerMediaOutboundMonFormSerializer},

        {'queryset': UPSOutboundMonForm.objects.all(),
         'serializer_class': UPSOutboundMonFormSerializer},

        {'queryset': PickPackDeliveriesMonForm.objects.all(),
         'serializer_class': PickPackDeliveriesMonFormSerializer},

        {'queryset': MarceloPerezMonForm.objects.all(),
         'serializer_class': MarceloPerezMonFormSerializer},

        {'queryset': MedTechGroupOutboundMonForm.objects.all(),
         'serializer_class': MedTechGroupOutboundMonFormSerializer},

        {'queryset': DigitalSignageOutboundMonForm.objects.all(),
         'serializer_class': DigitalSignageOutboundMonFormSerializer},

        {'queryset': HiveIncubatorsOutboundMonForm.objects.all(),
         'serializer_class': HiveIncubatorsOutboundMonFormSerializer},

        {'queryset': KaapiMachinesOutboundMonForm.objects.all(),
         'serializer_class': KaapiMachinesOutboundMonFormSerializer},

        {'queryset': SomethingsBrewingOutboundMonForm.objects.all(),
         'serializer_class': SomethingsBrewingOutboundMonFormSerializer},

        {'queryset': NaffaOutboundMonForm.objects.all(),
         'serializer_class': NaffaOutboundMonFormSerializer},

        {'queryset': JBNOutboundMonForm.objects.all(),
         'serializer_class': JBNOutboundMonFormSerializer},

        {'queryset': QuickAutoPartsOutboundMonForm.objects.all(),
         'serializer_class': QuickAutoPartsOutboundMonFormSerializer},

        {'queryset': ApexCommunicationsOutboundMonForm.objects.all(),
         'serializer_class': ApexCommunicationsOutboundMonFormSerializer},

        {'queryset': LawOfficesOutboundMonForm.objects.all(),
         'serializer_class': LawOfficesOutboundMonFormSerializer},

        {'queryset': WokeUpEnergyOutboundMonForm.objects.all(),
         'serializer_class': WokeUpEnergyOutboundMonFormSerializer},

        {'queryset': FinnesseMortgageOutboundMonForm.objects.all(),
         'serializer_class': FinnesseMortgageOutboundMonFormSerializer},

        {'queryset': UnitedMortgageOutboundMonForm.objects.all(),
         'serializer_class': UnitedMortgageOutboundMonFormSerializer},

        {'queryset': CleanLivingHealthWellnessOutboundMonForm.objects.all(),
         'serializer_class': CleanLivingHealthWellnessOutboundMonFormSerializer},

        {'queryset': PractoOutboundMonForm.objects.all(),
         'serializer_class': PractoOutboundMonFormSerializer},

        {'queryset': ImaginariumOutboundMonForm.objects.all(),
         'serializer_class': ImaginariumOutboundMonFormSerializer},

        {'queryset': USJacleanOutboundForm.objects.all(),
         'serializer_class': USJacleanOutboundFormSerializer},

        {'queryset': GlobalGalaxyOutboundForm.objects.all(),
         'serializer_class': GlobalGalaxyOutboundFormSerializer},

        {'queryset': CommunityHealthProjectIncOutbound.objects.all(),
         'serializer_class': CommunityHealthProjectIncOutboundSerializer},

        {'queryset': EducatedAnalyticsLLCOutbound.objects.all(),
         'serializer_class': EducatedAnalyticsLLCOutboundSerializer},

        {'queryset': NewDimensionPharmacyOutbound.objects.all(),
         'serializer_class': NewDimensionPharmacyOutboundSerializer},

        {'queryset': StayNChargeOutbound.objects.all(),
         'serializer_class': StayNChargeOutboundSerializer},

        {'queryset': JHEnergyConsultantOutbound.objects.all(),
         'serializer_class': JHEnergyConsultantOutboundSerializer},

        {'queryset': MDRGroupLLCOutbound.objects.all(),
         'serializer_class': MDRGroupLLCOutboundSerializer},

        {'queryset': CoreySmallInsuranceAgencyOutbound.objects.all(),
         'serializer_class': CoreySmallInsuranceAgencyOutboundSerializer},

        {'queryset': EduvocateOutbound.objects.all(),
         'serializer_class': EduvocateOutboundSerializer},

        {'queryset': CrossTowerOutbound.objects.all(),
         'serializer_class': CrossTowerOutboundSerializer},

        {'queryset': DawnFinancialOutbound.objects.all(),
         'serializer_class': DawnFinancialOutboundSerializer},

        {'queryset': XportDigitalOutbound.objects.all(),
         'serializer_class': XportDigitalOutboundSerializer},

        {'queryset': CalistaOutboundMonForm.objects.all(),
         'serializer_class': CalistaOutboundMonFormSerializer},

        {'queryset': GlobalArkOutboundMonform.objects.all(),
         'serializer_class': GlobalArkOutboundMonformSerializer},

        {'queryset': DIDevelopOutbound.objects.all(),
         'serializer_class': DIDevelopOutboundSerializer},

        {'queryset': FreeholdOutboundMonForm.objects.all(),
         'serializer_class': FreeholdOutboundMonFormSerializer},

        {'queryset': ZeamoOutboundMonForm.objects.all(),
         'serializer_class': ZeamoOutboundMonFormSerializer},

        {'queryset': SapphireMedicalsOutboundMonForm.objects.all(),
         'serializer_class': SapphireMedicalsOutboundMonFormSerializer},

        {'queryset': EehhaaaOutboundMonForm.objects.all(),
         'serializer_class': EehhaaaOutboundMonFormSerializer},

        {'queryset': MasterMonitoringFormTonnCoaInboundCalls.objects.all(),
         'serializer_class': MasterMonitoringFormTonnCoaInboundCallsSerializer},

        {'queryset': SomethingsBrewingInbound.objects.all(),
         'serializer_class': SomethingsBrewingInboundSerializer},

        {'queryset': PrinterPixMasterMonitoringFormInboundCalls.objects.all(),
         'serializer_class': PrinterPixMasterMonitoringFormInboundCallsSerializer},

        {'queryset': NuclusInboundCalls.objects.all(),
         'serializer_class': NuclusInboundCallsSerializer},

        {'queryset': NaffaInnovationsInboundCalls.objects.all(),
         'serializer_class': NaffaInnovationsInboundCallsSerializer},

        {'queryset': KappimachineInboundCalls.objects.all(),
         'serializer_class': KappimachineInboundCallsSerializer},

        {'queryset': HealthyplusInboundMonForm.objects.all(),
         'serializer_class': HealthyplusInboundMonFormSerializer},

        {'queryset': FinesseMortgageInboundMonForm.objects.all(),
         'serializer_class': FinesseMortgageInboundMonFormSerializer},

        {'queryset': DigitalSwissGoldInboundMonForm.objects.all(),
         'serializer_class': DigitalSwissGoldInboundMonFormSerializer},

        {'queryset': DanielwellingtoInboundMonForm.objects.all(),
         'serializer_class': DanielwellingtoInboundMonFormSerializer},

        {'queryset': BhagyaLakshmiInboundMonForm.objects.all(),
         'serializer_class': BhagyaLakshmiInboundMonFormSerializer},

        {'queryset': AKDYInboundMonFormNew.objects.all(),
         'serializer_class': AKDYInboundMonFormNewSerializer},

        {'queryset': AdityaBirlainboundMonForm.objects.all(),
         'serializer_class': AdityaBirlainboundMonFormSerializer},

        {'queryset': ABHindalcoInboundMonForm.objects.all(),
         'serializer_class': ABHindalcoInboundMonFormSerializer},

        {'queryset': RainbowDiagnosticsInboundMonForm.objects.all(),
         'serializer_class': RainbowDiagnosticsInboundMonFormSerializer},

        {'queryset': DecentralizedVisionLTDInboundMonForm.objects.all(),
         'serializer_class': DecentralizedVisionLTDInboundMonFormSerializer},
        # completed
        {'queryset': IEDHHInboundMonForm.objects.all(),
         'serializer_class': IEDHHInboundMonFormSerializer},

        {'queryset': AmerisaveInboundMonForm.objects.all(),
         'serializer_class': AmerisaveInboundMonFormSerializer},

        {'queryset': ClearViewInboundMonForms.objects.all(),
         'serializer_class': ClearViewInboundMonFormsSerializer},

        {'queryset': QuickAutoPartsInboundMonForms.objects.all(),
         'serializer_class': QuickAutoPartsInboundMonFormsSerializer},

        {'queryset': LJHubInboundMonForms.objects.all(),
         'serializer_class': LJHubInboundMonFormsSerializer},

        {'queryset': ObtheraIncInboundMonForms.objects.all(),
         'serializer_class': ObtheraIncInboundMonFormsSerializer},

        {'queryset': EduvocateInboundMonForms.objects.all(),
         'serializer_class': EduvocateInboundMonFormsSerializer},

        {'queryset': CrossTowerInboundMonForms.objects.all(),
         'serializer_class': CrossTowerInboundMonFormsSerializer},

        {'queryset': SanaLifeScienceInbound.objects.all(),
         'serializer_class': SanaLifeScienceInboundSerializer},

        {'queryset': MonitoringFormMobile22InboundCalls.objects.all(),
         'serializer_class': MonitoringFormMobile22InboundCallsSerializer},

        {'queryset': XportDigitalInboundMonForm.objects.all(),
         'serializer_class': XportDigitalInboundMonFormSerializer},

        {'queryset': CalistaInboundMonForm.objects.all(),
         'serializer_class': CalistaInboundMonFormSerializer},

        {'queryset': GlobalArkInboundMonForm.objects.all(),
         'serializer_class': GlobalArkInboundMonFormSerializer},

        {'queryset': SuperPlayMonForm.objects.all(),
         'serializer_class': SuperPlayMonFormSerializer},

        {'queryset': DanielWellinChatEmailMonForm.objects.all(),
         'serializer_class': DanielWellinChatEmailMonFormSerializer},

        {'queryset': TerraceoChatEmailMonForm.objects.all(),
         'serializer_class': TerraceoChatEmailMonFormSerializer},

        {'queryset': TonnChatsEmailNewMonForm.objects.all(),
         'serializer_class': TonnChatsEmailNewMonFormSerializer},

        {'queryset': PrinterPixMasterMonitoringFormChatsEmail.objects.all(),
         'serializer_class': PrinterPixMasterMonitoringFormChatsEmailSerializer},

        {'queryset': PractoMonForm.objects.all(),
         'serializer_class': PractoMonFormSerializer},

        {'queryset': FurBabyMonForm.objects.all(),
         'serializer_class': FurBabyMonFormSerializer},

        {'queryset': AKDYEmailMonForm.objects.all(),
         'serializer_class': AKDYEmailMonFormSerializer},

        {'queryset': AmerisaveEmailMonForm.objects.all(),
         'serializer_class': AmerisaveEmailMonFormSerializer},

        {'queryset': ClearViewEmailMonForm.objects.all(),
         'serializer_class': ClearViewEmailMonFormSerializer},

        {'queryset': FinesseMortgageEmailMonForm.objects.all(),
         'serializer_class': FinesseMortgageEmailMonFormSerializer},

        {'queryset': DigitalSwissGoldEmailChatMonForm.objects.all(),
         'serializer_class': DigitalSwissGoldEmailChatMonFormSerializer},

        {'queryset': RainbowDiagnosticsEmailMonForm.objects.all(),
         'serializer_class': RainbowDiagnosticsEmailMonFormSerializer},

        {'queryset': HiveIncubatorEmailMonForm.objects.all(),
         'serializer_class': HiveIncubatorEmailMonFormSerializer},

        {'queryset': MedTechGroupEmailMonForm.objects.all(),
         'serializer_class': MedTechGroupEmailMonFormSerializer},

        {'queryset': Ri8BrainEmailMonForm.objects.all(),
         'serializer_class': Ri8BrainEmailMonFormSerializer},

        {'queryset': ScalaEmailMonForm.objects.all(),
         'serializer_class': ScalaEmailMonFormSerializer},

        {'queryset': KalkiFashionEmailMonForm.objects.all(),
         'serializer_class': KalkiFashionEmailMonFormSerializer},

        {'queryset': MaxwellEmailMonForm.objects.all(),
         'serializer_class': MaxwellEmailMonFormSerializer},

        {'queryset': TanaorJewelryEmailMonForm.objects.all(),
         'serializer_class': TanaorJewelryEmailMonFormSerializer},

        {'queryset': DecentralizedVisionEmailChatMonForm.objects.all(),
         'serializer_class': DecentralizedVisionEmailChatMonFormSerializer},

        {'queryset': USJacleanEmailChatForm.objects.all(),
         'serializer_class': USJacleanEmailChatFormSerializer},

        {'queryset': CrossTowerEmailChatForm.objects.all(),
         'serializer_class': CrossTowerEmailChatFormSerializer},

        {'queryset': SanaLifeScienceEmailChatForm.objects.all(),
         'serializer_class': SanaLifeScienceEmailChatFormSerializer},

        {'queryset': ChatMonitoringFormEva.objects.all(),
         'serializer_class': ChatMonitoringFormEvaSerializer},

        {'queryset': ChatMonitoringFormPodFather.objects.all(),
         'serializer_class': ChatMonitoringFormPodFatherSerializer},

        {'queryset': FameHouseNewMonForm.objects.all(),
         'serializer_class': FameHouseNewMonFormSerializer},

        {'queryset': FLAMonitoringForm.objects.all(),
         'serializer_class': FLAMonitoringFormSerializer},

        {'queryset': PractoNewVersion.objects.all(),
         'serializer_class': PractoNewVersionSerializer},

        {'queryset': GubagooAuditForm.objects.all(),
         'serializer_class': GubagooAuditFormSerializer},

        {'queryset': ILMakiageEmailChatForm.objects.all(),
         'serializer_class': ILMakiageEmailChatFormSerializer},

        {'queryset': WinopolyOutbound.objects.all(),
         'serializer_class': WinopolyOutboundSerializer},

        {'queryset': ABHindalcoMonForm.objects.all(),
         'serializer_class': ABHindalcoMonFormSerializer},

        {'queryset': BhagyalaxmiChatMonForm.objects.all(),
         'serializer_class': BhagyalaxmiChatMonFormSerializer},

        {'queryset': SapphireMedicalsChatMonForm.objects.all(),
         'serializer_class': SapphireMedicalsChatMonFormSerializer},

        {'queryset': AllCarePhysicalTherapyMonform.objects.all(),
         'serializer_class': AllCarePhysicalTherapyMonformSerializer},

        {'queryset': ExecutiveCapitalResourcesmonform.objects.all(),
         'serializer_class': ExecutiveCapitalResourcesmonformSerializer},

        {'queryset': BrightWayOutboundmonform.objects.all(),
         'serializer_class': BrightWayOutboundmonformSerializer},

        {'queryset': BuildinglabLLCOutboundmonform.objects.all(),
         'serializer_class': BuildinglabLLCOutboundmonformSerializer},

        {'queryset': BlazingHogEmailChatmonform.objects.all(),
         'serializer_class': BlazingHogEmailChatmonformSerializer},

        {'queryset': PractoWithSubCategory.objects.all(),
         'serializer_class': PractoWithSubCategorySerializer},

        {'queryset': GlobalPharmaOutboundmonform.objects.all(),
         'serializer_class': GlobalPharmaOutboundmonformSerializer},

        {'queryset': ThirdWaveOutboundmonform.objects.all(),
         'serializer_class': ThirdWaveOutboundmonformSerializer},

        {'queryset': HardHatTechnologiesOutboundmonform.objects.all(),
         'serializer_class': HardHatTechnologiesOutboundmonformSerializer},

        {'queryset': RedefinePlasticsOutboundmonform.objects.all(),
         'serializer_class': RedefinePlasticsOutboundmonformSerializer},

        {'queryset': ThirdWaveInboundMonForm.objects.all(),
         'serializer_class': ThirdWaveInboundMonFormSerializer},

        {'queryset': HardHatTechnologiesInboundMonForm.objects.all(),
         'serializer_class': HardHatTechnologiesInboundMonFormSerializer},

        {'queryset': TKAWDIWOutboundmonform.objects.all(),
         'serializer_class': TKAWDIWOutboundmonformSerializer},

        {'queryset': NerotelInboundmonform.objects.all(),
         'serializer_class': NerotelInboundmonformSerializer},

        {'queryset': SpoiledChildChatmonform.objects.all(),
         'serializer_class': SpoiledChildChatmonformSerializer},

        {'queryset': ESRTechTalentOutboundmonform.objects.all(),
         'serializer_class': ESRTechTalentOutboundmonformSerializer},

        {'queryset': GreenConnectOutboundmonform.objects.all(),
         'serializer_class': GreenConnectOutboundmonformSerializer},

        {'queryset': JumpRydesEmailChatForm.objects.all(),
         'serializer_class': JumpRydesEmailChatFormSerializer},

        {'queryset': CentralMortgageFundingOutboundmonform.objects.all(),
         'serializer_class': CentralMortgageFundingOutboundmonformSerializer},

        {'queryset': RapidMortgageOutboundmonform.objects.all(),
         'serializer_class': RapidMortgageOutboundmonformSerializer},

        {'queryset': BridanAssociatesOutboundmonform.objects.all(),
         'serializer_class': BridanAssociatesOutboundmonformSerializer},

        {'queryset': LinenFinderOutboundmonform.objects.all(),
         'serializer_class': LinenFinderOutboundmonformSerializer},

        {'queryset': BetterEdOutboundmonform.objects.all(),
         'serializer_class': BetterEdOutboundmonformSerializer},

        {'queryset': BetterEdInboundMonForm.objects.all(),
         'serializer_class': BetterEdInboundMonFormSerializer},

        {'queryset': Com98Outboundmonform.objects.all(),
         'serializer_class': Com98OutboundmonformSerializer},

        {'queryset': Com98InboundMonForm.objects.all(),
         'serializer_class': Com98InboundMonFormSerializer},

        {'queryset': GretnaMedicalCentreOutboundmonform.objects.all(),
         'serializer_class': GretnaMedicalCentreOutboundmonformSerializer},

        {'queryset': AristaMDOutboundmonform.objects.all(),
         'serializer_class': AristaMDOutboundmonformSerializer},

        {'queryset': OpenWindsInboundMonForm.objects.all(),
         'serializer_class': OpenWindsInboundMonFormSerializer},

        {'queryset': RobertDamonProductionOutboundmonform.objects.all(),
         'serializer_class': RobertDamonProductionOutboundmonformSerializer},

        {'queryset': EmbassyLuxuryInboundMonForm.objects.all(),
         'serializer_class': EmbassyLuxuryInboundMonFormSerializer},

        {'queryset': VenwizOutboundmonform.objects.all(),
         'serializer_class': VenwizOutboundmonformSerializer},

        {'queryset': AmerisaveMonForm.objects.all(),
         'serializer_class': AmerisaveMonFormSerializer},

        {'queryset': CityHabitatOutboundmonform.objects.all(),
         'serializer_class': CityHabitatOutboundmonformSerializer},

        {'queryset': OptelOutboundmonform.objects.all(),
         'serializer_class': OptelOutboundmonformSerializer},

        {'queryset': SouthCountyInboundMonForm.objects.all(),
         'serializer_class': SouthCountyInboundMonFormSerializer},

        {'queryset': SouthCountyOutboundMonForm.objects.all(),
         'serializer_class': SouthCountyOutboundMonFormSerializer},

        {'queryset': NaffaInnovationEmailChatForm.objects.all(),
         'serializer_class': NaffaInnovationEmailChatFormSerializer},

        {'queryset': InpressOutboundMonForm.objects.all(),
         'serializer_class': InpressOutboundMonFormSerializer},

        {'queryset': InpressEmailChatForm.objects.all(),
         'serializer_class': InpressEmailChatFormSerializer},

        {'queryset': LMEnterprisesOutboundMonForm.objects.all(),
         'serializer_class': LMEnterprisesOutboundMonFormSerializer},
    ]

def correctABH(request):
    update = []
    for i in ABHindalcoMonForm.objects.all():
        a = i.oc_1 + i.oc_2 + i.oc_3
        b = i.softskill_1 + i.softskill_2 + i.softskill_3 + i.softskill_4
        c = i.compliance_1 + i.compliance_2 + i.compliance_3 + i.compliance_4
        i.oc_total = a
        i.softskill_total = b
        i.compliance_total = c
        if i.oc_2 == 0 or i.compliance_2 == 0 or i.compliance_3 == 0 or i.compliance_4 == 0:
            i.overall_score = 0
        else:
            i.overall_score = a + b + c
        update.append(i)
    ABHindalcoMonForm.objects.bulk_update(update, ['oc_total', 'softskill_total', 'compliance_total', 'overall_score'])
    return redirect('/')

def migrateOutbound(request):
    data_outbound = []
    data_inbound = []
    data_email = []
    for i in list_of_monforms:
        cam = i.objects.all()
        if cam:
            if cam[0].type == 'Outbound':
                OutboundExport.objects.all().delete()
                for j in cam:
                    outbound = OutboundExport(
                        campaign=j.process, emp_id=j.emp_id, associate_name=j.associate_name, zone=j.zone,
                        concept=j.concept, customer_name=j.customer_name, customer_contact=j.customer_contact,
                        call_date=j.call_date, call_duration=j.call_duration, audit_date=j.audit_date,
                        quality_analyst=j.qa, team_lead=j.team_lead, manager=j.manager, am=j.am,
                        manager_id=j.manager_id, week=j.week, oc_1=j.oc_1, oc_2=j.oc_2, oc_3=j.oc_3,
                        softskill_1=j.softskill_1, softskill_2=j.softskill_2, softskill_3=j.softskill_3,
                        softskill_4=j.softskill_4, softskill_5=j.softskill_5, compliance_1=j.compliance_1,
                        compliance_2=j.compliance_2, compliance_3=j.compliance_3, compliance_4=j.compliance_4,
                        compliance_5=j.compliance_5, compliance_6=j.compliance_6, areas_improvement=j.areas_improvement,
                        positives=j.positives, comments=j.comments, added_by=j.added_by, status=j.status,
                        closed_date=j.closed_date, emp_comments=j.emp_comments, oc_total=j.ce_total,
                        softskill_total=j.softskill_total, compliance_total=j.compliance_total,
                        overall_score=j.overall_score, fatal=j.fatal, fatal_count=j.fatal_count,
                        dispute_status=j.disput_status
                    )
                    data_outbound.append(outbound)
            if cam[0].type == 'Inbound':
                Inbound.objects.all().delete()
                for j in cam:
                    inbound = Inbound(
                        campaign=j.process, emp_id=j.emp_id, associate_name=j.associate_name, zone=j.zone,
                        concept=j.concept, customer_name=j.customer_name, customer_contact=j.customer_contact,
                        call_date=j.call_date, call_duration=j.call_duration, audit_date=j.audit_date,
                        quality_analyst=j.qa, team_lead=j.team_lead, manager=j.manager, am=j.am,
                        manager_id=j.manager_id, week=j.week, ce_1=j.ce_1, ce_2=j.ce_2, ce_3=j.ce_3, ce_4=j.ce_4,
                        ce_5=j.ce_5, ce_6=j.ce_6, ce_7=j.ce_7, ce_8=j.ce_8, ce_9=j.ce_9, ce_10=j.ce_10, ce_11=j.ce_11,
                        business_1=j.business_1, business_2=j.business_2, compliance_1=j.compliance_1,
                        compliance_2=j.compliance_2, compliance_3=j.compliance_3, compliance_4=j.compliance_4,
                        compliance_5=j.compliance_5, areas_improvement=j.areas_improvement, positives=j.positives,
                        comments=j.comments, added_by=j.added_by, status=j.status, closed_date=j.closed_date,
                        emp_comments=j.emp_comments, ce_total=j.ce_total, business_total=j.business_total,
                        compliance_total=j.compliance_total, overall_score=j.overall_score, fatal=j.fatal,
                        fatal_count=j.fatal_count, dispute_status=j.disput_status
                    )
                    data_inbound.append(inbound)
            if cam[0].type == 'Email - Chat':
                EmailChat.objects.all().delete()
                for j in cam:
                    email = EmailChat(
                        campaign=j.process,emp_id=j.emp_id, associate_name= j.associate_name, zone= j.zone,
                        concept=j.concept, customer_name=j.customer_name, customer_contact=j.customer_contact,
                        audit_date=j.audit_date, quality_analyst=j.qa, team_lead=j.team_lead, manager=j.manager,
                        am=j.am, manager_id=j.manager_id, week=j.week, ce_1=j.ce_1, ce_2=j.ce_2, ce_3=j.ce_3,
                        ce_4=j.ce_4, ce_5=j.ce_5, ce_6=j.ce_6, ce_7=j.ce_7, ce_8=j.ce_8, ce_9=j.ce_9, ce_10=j.ce_10,
                        ce_11=j.ce_11, business_1=j.business_1, business_2=j.business_2, compliance_1=j.compliance_1,
                        compliance_2=j.compliance_2, compliance_3=j.compliance_3, compliance_4=j.compliance_4,
                        compliance_5=j.compliance_5, ce_total=j.ce_total, business_total=j.business_total,
                        compliance_total=j.compliance_total, overall_score=j.overall_score,
                        areas_improvement=j.areas_improvement, positives=j.positives, comments=j.comments,
                        added_by=j.added_by, status=j.status, closed_date=j.closed_date, emp_comments=j.emp_comments,
                        fatal=j.fatal, fatal_count=j.fatal_count, dispute_status=j.disput_status
                    )
                    data_email.append(email)
    OutboundExport.objects.bulk_create(data_outbound)
    Inbound.objects.bulk_create(data_inbound)
    EmailChat.objects.bulk_create(data_email)

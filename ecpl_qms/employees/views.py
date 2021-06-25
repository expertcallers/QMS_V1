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
        mon_forms = []


        associate_data=[]
        associate_data_fatal=[]
        associate_data_errors=[]

        # Score in All forms
        for i in mon_forms:
            coaching = i.objects.filter(emp_id=emp_id, audit_date__year=currentYear,
                                        audit_date__month=currentMonth)
            if coaching.count() > 0:

                emp_wise = i.objects.filter(emp_id=emp_id,audit_date__year=currentYear, audit_date__month=currentMonth).values(
                    'process').annotate(dcount=Count('associate_name')).annotate(
                    davg=Avg('overall_score'))
                emp_wise_fatal = i.objects.filter(emp_id=emp_id, audit_date__year=currentYear,
                                            audit_date__month=currentMonth).values(
                    'process').annotate(dsum=Sum('fatal_count'))

                emp_wise_errors = i.objects.filter(emp_id=emp_id, audit_date__year=currentYear,
                                                  audit_date__month=currentMonth,overall_score__lt=100).values(
                    'process').annotate(dcount=Count('process'))

                associate_data.append(emp_wise)
                associate_data_fatal.append(emp_wise_fatal)
                associate_data_errors.append(emp_wise_errors)


            else:
                pass


        data = {'profile':profile,'associate_data':associate_data,
                'associate_data_fatal':associate_data_fatal,
                'associate_data_errors':associate_data_errors,
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
        mon_forms = []

        associate_data = []
        associate_data_fatal = []
        associate_data_errors = []

        # Score in All forms
        for i in mon_forms:
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

    mon_forms = []

    campaigns = None
    import datetime
    user_id = request.user.id
    employees = Profile.objects.filter(emp_desi='CRO')
    managers = Profile.objects.filter(emp_desi='Manager')
    teams = Team.objects.all()

    # Date Time
    if request.method=='POST':

        month =request.POST['month']
        year = request.POST['year']

        ###### Campaign-quick-report ########
        camp_wise_tot=[]

        for i in mon_forms:

            camp_wise_total = i.objects.filter(audit_date__year=year, audit_date__month=month).values(
                'process').annotate(dcount=Count('process')).annotate(davg=Avg('overall_score'))
            camp_wise_tot.append(camp_wise_total)

        data = {'employees':employees,'managers':managers,'campaigns':campaigns,
                'teams':teams,'camp_total':camp_wise_tot}

        return render(request, 'quality-dashboard-management.html',data)

    else:

        d = datetime.datetime.now()
        month = d.strftime("%m")
        year = d.strftime("%Y")

        ###### Campaign-quick-report ########

        camp_wise_tot = []
        for i in mon_forms:
            camp_wise_total = i.objects.filter(audit_date__year=year, audit_date__month=month).values(
                'process').annotate(dcount=Count('process')).annotate(davg=Avg('overall_score'))
            camp_wise_tot.append(camp_wise_total)

        data = {'employees': employees, 'managers': managers, 'campaigns': campaigns,
            'teams': teams, 'camp_total': camp_wise_tot}

        return render(request, 'quality-dashboard-management.html', data)



def agenthome(request):

    if request.method=='POST':

        agent_name = request.user.profile.emp_name
        team_name=request.user.profile.team
        team = Team.objects.get(name=team_name)

        teams=Team.objects.all()
        currentMonth = request.POST['month']
        currentYear = request.POST['year']

        ################### opn_count #############

        list_of_monforms = []

        all_coaching_list = []
        open_coaching_list=[]
        disput_list=[]


        def openCampaigns(monforms):
            open_obj = monforms.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,associate_name=agent_name).order_by('-audit_date')
            all_obj = monforms.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,associate_name=agent_name,status=False,disput_status=False).order_by('-audit_date')
            disp_obj = monforms.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,associate_name=agent_name,disput_status=True).order_by('-audit_date')

            all_coaching_list.append(open_obj)
            open_coaching_list.append(all_obj)

            disput_list.append(disp_obj)

        for i in list_of_monforms:
            openCampaigns(i)

        ###################  Avg Campaignwise

        avg_campaignwise=[]
        campaign_wise_count=[]
        fatal_list=[]

        for i in list_of_monforms:

            emp_wise = i.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,associate_name=agent_name).values('process').annotate(davg=Avg('overall_score'))
            camp_wise_count = i.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth, associate_name=agent_name, overall_score__lt=100).values('process').annotate(dcount=Count('associate_name'))
            fatal_count = i.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,associate_name=agent_name).values('process').annotate(dcount=Sum('fatal_count'))

            avg_campaignwise.append(emp_wise)
            campaign_wise_count.append(camp_wise_count)
            fatal_list.append(fatal_count)




        list_of_open_count = []

        for i in list_of_monforms:
            count = i.objects.filter(associate_name=agent_name,audit_date__year=currentYear,audit_date__month=currentMonth,status=False).count()

            list_of_open_count.append(count)

        total_open_coachings = sum(list_of_open_count)

        data = {'all_coachings':all_coaching_list,
                'open_coaching':open_coaching_list,
                'disput_coaching':disput_list,
                'avg_campaignwise':avg_campaignwise,
                'camp_wise_count':campaign_wise_count,
                'fatal_list':fatal_list,
                'total_open': total_open_coachings,
                'team':team,
                'teams':teams
                }


        return render(request, 'agent-home.html',data)

    else:
        agent_name = request.user.profile.emp_name
        team_name = request.user.profile.team
        team = Team.objects.get(name=team_name)

        teams = Team.objects.all()
        currentMonth = datetime.now().month
        currentYear = datetime.now().year

        ################### opn_count #############

        list_of_monforms = [

                        ]

        all_coaching_list = []
        open_coaching_list = []
        disput_list = []

        def openCampaigns(monforms):
            open_obj = monforms.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,
                                               associate_name=agent_name).order_by('-audit_date')
            all_obj = monforms.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,
                                              associate_name=agent_name, status=False, disput_status=False).order_by(
                '-audit_date')
            disp_obj = monforms.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,
                                               associate_name=agent_name, disput_status=True).order_by('-audit_date')

            all_coaching_list.append(open_obj)
            open_coaching_list.append(all_obj)

            disput_list.append(disp_obj)

        for i in list_of_monforms:
            openCampaigns(i)

        ###################  Avg Campaignwise

        avg_campaignwise = []
        campaign_wise_count = []
        fatal_list = []

        for i in list_of_monforms:
            emp_wise = i.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,
                                        associate_name=agent_name).values('process').annotate(davg=Avg('overall_score'))
            camp_wise_count = i.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,
                                               associate_name=agent_name, overall_score__lt=100).values(
                'process').annotate(dcount=Count('associate_name'))
            fatal_count = i.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,
                                           associate_name=agent_name).values('process').annotate(
                dcount=Sum('fatal_count'))

            avg_campaignwise.append(emp_wise)
            campaign_wise_count.append(camp_wise_count)
            fatal_list.append(fatal_count)

            #############################################

        list_of_open_count = []

        for i in list_of_monforms:
            count = i.objects.filter(associate_name=agent_name, audit_date__year=currentYear,
                                     audit_date__month=currentMonth, status=False).count()

            list_of_open_count.append(count)

        total_open_coachings = sum(list_of_open_count)

        data = {'all_coachings': all_coaching_list,
                'open_coaching': open_coaching_list,
                'disput_coaching': disput_list,
                'avg_campaignwise': avg_campaignwise,
                'camp_wise_count': campaign_wise_count,
                'fatal_list': fatal_list,
                'total_open': total_open_coachings,
                'team': team,
                'teams': teams
                }

        return render(request, 'agent-home.html', data)

# Coaching View ---------------------------- !!!

def coachingViewAgents(request,process,pk):

    process_name=process

    if process_name == 'EVA Chat':
        coaching = ChatMonitoringFormEva.objects.get(id=pk)
        data = {'coaching': coaching}
        return render(request, 'coaching-views/emp-coaching-view-eva-chat.html', data)

    else:
        pass

def coachingViewQaDetailed(request,process,pk):

    process_name = process

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

        list_of_monforms = [

                        ]

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
        status=request.POST['status']

        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        qa = request.POST['qa']

        list_of_monforms = [ ]

        if start_date and end_date:

            if status=='all':

                coaching_list=[]

                def dateAll(monform):
                    obj=monform.objects.filter(qa=qa,process=campaign,audit_date__range=[start_date, end_date])
                    return obj

                for i in list_of_monforms:

                    obj=dateAll(i)
                    coaching_list.append(obj)

            else:

                coaching_list = []

                def datestatusAll(monform):
                    obj = monform.objects.filter(qa=qa,process=campaign,status=status,audit_date__range=[start_date, end_date])
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
                    obj=monform.objects.filter(qa=qa,process=campaign)
                    return obj

                for i in list_of_monforms:

                    obj=dateAll(i)
                    coaching_list.append(obj)

            else:

                coaching_list = []

                def datestatusAll(monform):
                    obj = monform.objects.filter(qa=qa,process=campaign,status=status)
                    return obj

                for i in list_of_monforms:
                    obj = datestatusAll(i)
                    coaching_list.append(obj)

            data={'coaching_list':coaching_list,
                 }

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

            emp_wise = monform.objects.filter(audit_date__year=currentYear,audit_date__month=currentMonth).values('associate_name').annotate(dcount=Count('associate_name')).annotate(davg=Avg('overall_score')).order_by('-dcount')
            #emp_wise_avg = monform.objects.filter(audit_date__year=currentYear,audit_date__month=currentMonth).values('associate_name').annotate(dcount=Avg('overall_score')).order_by('-dcount')
            emp_wise_fatal = monform.objects.filter(fatal=True, audit_date__year=currentYear,audit_date__month=currentMonth).values('associate_name').annotate(dcount=Sum('fatal_count'))
            fame_all = monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth)
            total_errors = monform.objects.filter(overall_score__lt=100, audit_date__year=currentYear,audit_date__month=currentMonth).count()
            total_fatal_obj = monform.objects.filter(fatal=True, audit_date__year=currentYear,audit_date__month=currentMonth)
            total_fata_list=[]

            for i in total_fatal_obj:
                total_fata_list.append(i.fatal_count)

            total_fatal = sum(total_fata_list)

            total_audit_count = monform.objects.filter(audit_date__year=currentYear,audit_date__month=currentMonth).count()

            avg=monform.objects.filter(audit_date__year=currentYear,audit_date__month=currentMonth).aggregate(Avg('overall_score'))
            processavg=avg['overall_score__avg']

            if processavg==None:
                process_avg = 0
            else:
                process_avg = float("{:.2f}".format(processavg))


            week_wise_avg = monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth).values('week').annotate(davg=Avg('overall_score')).annotate(dcount=Count('week'))


            #week_wise_fatal_count=monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,fatal=True).values('week').annotate(dcount=Count('fatal'))

            if total_audit_count>0:
                error_percentage = (total_errors / total_audit_count) * 100
            else:
                error_percentage=0
            error_perc = float("{:.2f}".format(error_percentage))

            if total_audit_count>0:
                error_percentage_fatal = (total_fatal / total_audit_count) * 100
            else:
                error_percentage_fatal=0
            error_perc_fatal = float("{:.2f}".format(error_percentage_fatal))

            ########  -- Weekwise Calculations

            week_list=['week1','week2','week3','week4','week5']
            week_wise_report=[]
            for i in week_list:
                weekdict={}

                week_fatal_obj=monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,fatal=True,week=i)

                week_fatal_list=[]
                for j in week_fatal_obj:
                    week_fatal_list.append(j.fatal_count)
                week_fatal_count=sum(week_fatal_list)

                week_nonfatal=monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,week=i,overall_score__lt=100,fatal=False).count()
                week_total_audits=monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,week=i).count()
                if week_total_audits>0:
                    fatal_avg=round(float((week_fatal_count/week_total_audits)*100),2)
                    nonfatal_avg=round(float((week_nonfatal/week_total_audits)*100),2)

                else:
                    fatal_avg='NA'
                    nonfatal_avg='NA'

                weekdict['week']=i
                weekdict['fatal_count']=week_fatal_count
                weekdict['fatal_avg']=fatal_avg
                weekdict['total_audits']=week_total_audits
                weekdict['non_fatal_avg']=nonfatal_avg
                weekdict['non_fatal_count']=week_nonfatal

                week_wise_report.append(weekdict)

                ########  -- Weekwise Calculations End

            #### --- QA Wise

            qa_wise=[]
            for i in week_list:
                qa_wise_avg = monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,week=i).values('added_by','week').annotate(davg=Avg('overall_score')).annotate(dcount=Count('added_by'))
                qa_wise.append(qa_wise_avg)

            am_wise = []
            for i in week_list:
                am_wise_avg = monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,week=i).values('am', 'week').annotate(davg=Avg('overall_score')).annotate(dcount=Count('am'))
                am_wise.append(am_wise_avg)

            tl_wise = []
            for i in week_list:
                tl_wise_avg = monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,week=i).values('team_lead', 'week').annotate(davg=Avg('overall_score')).annotate(dcount=Count('am'))
                tl_wise.append(tl_wise_avg)


            #Week-wise Emp Fatal
            pivot_test=pivot(monform.objects.filter(fatal=True),'associate_name','week','fatal_count',aggregation=Sum)

            # Parameter wise ########

            open_coaching_employee_wise=monform.objects.filter(status=False).values('associate_name').annotate(dcount=Count('status'))


            data = {'fame_all': fame_all,
                    'emp_wise': emp_wise,
                    'emp_wise_fatal': emp_wise_fatal,
                    #'emp_wise_avg': emp_wise_avg,
                    'total_errors': total_errors,
                    'total_fatal':total_fatal,
                    'total_audit_count': total_audit_count,
                    'error_perc': error_perc,
                    'error_perc_fatal':error_perc_fatal,
                    'process_avg':process_avg,
                    'week_wise_avg':week_wise_avg,
                    #'week_wise_fatal_count':week_wise_fatal_count
                    'week_wise_report':week_wise_report,
                    'qa_wise_avg':qa_wise,
                    'am_wise_avg':am_wise,
                    'tl_wise_avg':tl_wise,
                    'pivot_test':pivot_test,
                    'process':campaign,
                    'emp_coaching':open_coaching_employee_wise,
                    'cmonth':currentMonth,
                    'cyear':currentYear
                    }

            return data

        if campaign=='Fame House':
            data=campaignWiseCalculator(FameHouseNewMonForm)
            return render(request, 'campaign-report/detailed.html',data)

        if campaign=='Noom-POD':
            data = campaignWiseCalculator(ChatMonitoringFormPodFather)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign=='Noom-EVA':
            data = campaignWiseCalculator(ChatMonitoringFormEva)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign=='FLA':
            data = campaignWiseCalculator(FLAMonitoringForm)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign=='MT Cosmetic':
            data = campaignWiseCalculator(MTCosmeticsMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign=='Printer Pix Chat Email':
            data = campaignWiseCalculator(PrinterPixMasterMonitoringFormChatsEmail)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign=='Printer Pix Inbound':
            data = campaignWiseCalculator(PrinterPixMasterMonitoringFormInboundCalls)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign=='AAdya':
            data = campaignWiseCalculator(MonitoringFormLeadsAadhyaSolution)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign=='Insalvage':
            data = campaignWiseCalculator(MonitoringFormLeadsInsalvage)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign=='Medicare':
            data = campaignWiseCalculator(MonitoringFormLeadsMedicare)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign=='CTS':
            data = campaignWiseCalculator(MonitoringFormLeadsCTS)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign=='Tentamus Food':
            data = campaignWiseCalculator(MonitoringFormLeadsTentamusFood)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign=='Tentamus Pet':
            data = campaignWiseCalculator(MonitoringFormLeadsTentamusPet)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign=='City Security':
            data = campaignWiseCalculator(MonitoringFormLeadsCitySecurity)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign == 'Allen Consulting':
            data = campaignWiseCalculator(MonitoringFormLeadsAllenConsulting)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign == 'System4':
            data = campaignWiseCalculator(MonitoringFormLeadsSystem4)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign == 'Louisville':
            data = campaignWiseCalculator(MonitoringFormLeadsLouisville)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign == 'Info Think LLC':
            data = campaignWiseCalculator(MonitoringFormLeadsInfothinkLLC)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign == 'PSECU':
            data = campaignWiseCalculator(MonitoringFormLeadsPSECU)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign == 'Get A Rates':
            data = campaignWiseCalculator(MonitoringFormLeadsGetARates)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign == 'Advance Consultants':
            data = campaignWiseCalculator(MonitoringFormLeadsAdvanceConsultants)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign == 'Fur Baby':
            data = campaignWiseCalculator(FurBabyMonForm)
            return render(request, 'campaign-report/detailed.html', data)


        if campaign == 'Upfront Online LLC':
            data = campaignWiseCalculator(UpfrontOnlineLLCMonform)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Micro Distributing':
            data = campaignWiseCalculator(MicroDistributingMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'JJ Studio':
            data = campaignWiseCalculator(JJStudioMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Zero Stress Marketing':
            data = campaignWiseCalculator(ZeroStressMarketingMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'WTU':
            data = campaignWiseCalculator(WTUMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Roof Well':
            data = campaignWiseCalculator(RoofWellMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Glyde App':
            data = campaignWiseCalculator(GlydeAppMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Millennium Scientific':
            data = campaignWiseCalculator(MillenniumScientificMonForm)
            return render(request, 'campaign-report/detailed.html', data)


        if campaign == 'Stand Spot':
            data = campaignWiseCalculator(StandSpotMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Cam Industrial':
            data = campaignWiseCalculator(CamIndustrialMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Optimal Student Loan':
            data = campaignWiseCalculator(OptimalStudentLoanMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Navigator Bio':
            data = campaignWiseCalculator(NavigatorBioMonForm)
            return render(request, 'campaign-report/detailed.html', data)



        if campaign == 'AKDY - Email':
            data = campaignWiseCalculator(AKDYEmailMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Ibiz':
            data = campaignWiseCalculator(IbizMonForm)
            return render(request, 'campaign-report/detailed.html', data)






        if campaign == 'Daniel Wellington - Chat - Email':
            data = campaignWiseCalculator(DanielWellinChatEmailMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Protostar':
            data = campaignWiseCalculator(ProtostarMonForm)
            return render(request, 'campaign-report/detailed.html', data)



        if campaign == 'Embassy Luxury':
            data = campaignWiseCalculator(EmbassyLuxuryMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'IIB':
            data = campaignWiseCalculator(IIBMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Terraceo - Lead':
            data = campaignWiseCalculator(TerraceoLeadMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Terraceo - Chat - Email':
            data = campaignWiseCalculator(TerraceoChatEmailMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Kalki Fashions':
            data = campaignWiseCalculator(KalkiFashions)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Super Play':
            data = campaignWiseCalculator(SuperPlayMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Practo':
            data = campaignWiseCalculator(PractoMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Scala':
            data = campaignWiseCalculator(ScalaMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Citizen Capital':
            data = campaignWiseCalculator(CitizenCapitalMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Golden East':
            data = campaignWiseCalculator(GoldenEastMonForm)
            return render(request, 'campaign-report/detailed.html', data)


        if campaign == 'Ri8Brain':
            data = campaignWiseCalculator(RitBrainMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Restaurant Solution Group':
            data = campaignWiseCalculator(RestaurentSolMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'QBIQ':
            data = campaignWiseCalculator(QBIQMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Accutime':
            data = campaignWiseCalculator(AccutimeMonForm)
            return render(request, 'campaign-report/detailed.html', data)


        if campaign == 'Solar Campaign':
            data = campaignWiseCalculator(SolarCampaignMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Yes Health Molina':
            data = campaignWiseCalculator(YesHealthMolinaMonForm)
            return render(request, 'campaign-report/detailed.html', data)


        else:
            return render(request,'')

    else:
        from datetime import datetime

        currentMonth = datetime.now().month
        currentYear = datetime.now().year

        campaign = cname

        def campaignWiseCalculator(monform):

            emp_wise = monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth).values(
                'associate_name').annotate(dcount=Count('associate_name')).annotate(davg=Avg('overall_score')).order_by(
                '-dcount')
            # emp_wise_avg = monform.objects.filter(audit_date__year=currentYear,audit_date__month=currentMonth).values('associate_name').annotate(dcount=Avg('overall_score')).order_by('-dcount')
            emp_wise_fatal = monform.objects.filter(fatal=True, audit_date__year=currentYear,
                                                    audit_date__month=currentMonth).values('associate_name').annotate(
                dcount=Sum('fatal_count'))
            fame_all = monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth)
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

            # week_wise_fatal_count=monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,fatal=True).values('week').annotate(dcount=Count('fatal'))

            if total_audit_count > 0:
                error_percentage = (total_errors / total_audit_count) * 100
            else:
                error_percentage = 0
            error_perc = float("{:.2f}".format(error_percentage))

            if total_audit_count > 0:
                error_percentage_fatal = (total_fatal / total_audit_count) * 100
            else:
                error_percentage_fatal = 0
            error_perc_fatal = float("{:.2f}".format(error_percentage_fatal))

            ########  -- Weekwise Calculations

            week_list = ['week1', 'week2', 'week3', 'week4', 'week5']
            week_wise_report = []
            for i in week_list:
                weekdict = {}

                week_fatal_obj = monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,
                                                        fatal=True, week=i)

                week_fatal_list = []
                for j in week_fatal_obj:
                    week_fatal_list.append(j.fatal_count)
                week_fatal_count = sum(week_fatal_list)

                week_nonfatal = monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,
                                                       week=i, overall_score__lt=100, fatal=False).count()
                week_total_audits = monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,
                                                           week=i).count()
                if week_total_audits > 0:
                    fatal_avg = round(float((week_fatal_count / week_total_audits) * 100), 2)
                    nonfatal_avg = round(float((week_nonfatal / week_total_audits) * 100), 2)

                else:
                    fatal_avg = 'NA'
                    nonfatal_avg = 'NA'

                weekdict['week'] = i
                weekdict['fatal_count'] = week_fatal_count
                weekdict['fatal_avg'] = fatal_avg
                weekdict['total_audits'] = week_total_audits
                weekdict['non_fatal_avg'] = nonfatal_avg
                weekdict['non_fatal_count'] = week_nonfatal

                week_wise_report.append(weekdict)

                ########  -- Weekwise Calculations End

            #### --- QA Wise

            qa_wise = []
            for i in week_list:
                qa_wise_avg = monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,
                                                     week=i).values('added_by', 'week').annotate(
                    davg=Avg('overall_score')).annotate(dcount=Count('added_by'))
                qa_wise.append(qa_wise_avg)

            am_wise = []
            for i in week_list:
                am_wise_avg = monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,
                                                     week=i).values('am', 'week').annotate(
                    davg=Avg('overall_score')).annotate(dcount=Count('am'))
                am_wise.append(am_wise_avg)

            tl_wise = []
            for i in week_list:
                tl_wise_avg = monform.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,
                                                     week=i).values('team_lead', 'week').annotate(
                    davg=Avg('overall_score')).annotate(dcount=Count('am'))
                tl_wise.append(tl_wise_avg)

            # Week-wise Emp Fatal
            pivot_test = pivot(monform.objects.filter(fatal=True), 'associate_name', 'week', 'fatal_count',
                               aggregation=Sum)

            # Parameter wise ########

            open_coaching_employee_wise = monform.objects.filter(status=False).values('associate_name').annotate(
                dcount=Count('status'))

            data = {'fame_all': fame_all,
                    'emp_wise': emp_wise,
                    'emp_wise_fatal': emp_wise_fatal,
                    # 'emp_wise_avg': emp_wise_avg,
                    'total_errors': total_errors,
                    'total_fatal': total_fatal,
                    'total_audit_count': total_audit_count,
                    'error_perc': error_perc,
                    'error_perc_fatal': error_perc_fatal,
                    'process_avg': process_avg,
                    'week_wise_avg': week_wise_avg,
                    # 'week_wise_fatal_count':week_wise_fatal_count
                    'week_wise_report': week_wise_report,
                    'qa_wise_avg': qa_wise,
                    'am_wise_avg': am_wise,
                    'tl_wise_avg': tl_wise,
                    'pivot_test': pivot_test,
                    'process': campaign,
                    'emp_coaching': open_coaching_employee_wise,
                    'cmonth': currentMonth,
                    'cyear': currentYear
                    }

            return data

        if campaign == 'Fame House':
            data = campaignWiseCalculator(FameHouseNewMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Noom-POD':
            data = campaignWiseCalculator(ChatMonitoringFormPodFather)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign == 'Noom-EVA':
            data = campaignWiseCalculator(ChatMonitoringFormEva)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign == 'FLA':
            data = campaignWiseCalculator(FLAMonitoringForm)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign == 'MT Cosmetic':
            data = campaignWiseCalculator(MTCosmeticsMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Printer Pix Chat Email':
            data = campaignWiseCalculator(PrinterPixMasterMonitoringFormChatsEmail)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign == 'Printer Pix Inbound':
            data = campaignWiseCalculator(PrinterPixMasterMonitoringFormInboundCalls)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign == 'AAdya':
            data = campaignWiseCalculator(MonitoringFormLeadsAadhyaSolution)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign == 'Insalvage':
            data = campaignWiseCalculator(MonitoringFormLeadsInsalvage)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign == 'Medicare':
            data = campaignWiseCalculator(MonitoringFormLeadsMedicare)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign == 'CTS':
            data = campaignWiseCalculator(MonitoringFormLeadsCTS)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign == 'Tentamus Food':
            data = campaignWiseCalculator(MonitoringFormLeadsTentamusFood)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign == 'Tentamus Pet':
            data = campaignWiseCalculator(MonitoringFormLeadsTentamusPet)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign == 'City Security':
            data = campaignWiseCalculator(MonitoringFormLeadsCitySecurity)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign == 'Allen Consulting':
            data = campaignWiseCalculator(MonitoringFormLeadsAllenConsulting)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign == 'System4':
            data = campaignWiseCalculator(MonitoringFormLeadsSystem4)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign == 'Louisville':
            data = campaignWiseCalculator(MonitoringFormLeadsLouisville)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign == 'Info Think LLC':
            data = campaignWiseCalculator(MonitoringFormLeadsInfothinkLLC)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign == 'PSECU':
            data = campaignWiseCalculator(MonitoringFormLeadsPSECU)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign == 'Get A Rates':
            data = campaignWiseCalculator(MonitoringFormLeadsGetARates)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign == 'Advance Consultants':
            data = campaignWiseCalculator(MonitoringFormLeadsAdvanceConsultants)
            return render(request, 'campaign-report/detailed.html', data)
        if campaign == 'Fur Baby':
            data = campaignWiseCalculator(FurBabyMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Upfront Online LLC':
            data = campaignWiseCalculator(UpfrontOnlineLLCMonform)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Micro Distributing':
            data = campaignWiseCalculator(MicroDistributingMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'JJ Studio':
            data = campaignWiseCalculator(JJStudioMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Zero Stress Marketing':
            data = campaignWiseCalculator(ZeroStressMarketingMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'WTU':
            data = campaignWiseCalculator(WTUMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Roof Well':
            data = campaignWiseCalculator(RoofWellMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Glyde App':
            data = campaignWiseCalculator(GlydeAppMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Millennium Scientific':
            data = campaignWiseCalculator(MillenniumScientificMonForm)
            return render(request, 'campaign-report/detailed.html', data)


        if campaign == 'Stand Spot':
            data = campaignWiseCalculator(StandSpotMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Cam Industrial':
            data = campaignWiseCalculator(CamIndustrialMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Optimal Student Loan':
            data = campaignWiseCalculator(OptimalStudentLoanMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Navigator Bio':
            data = campaignWiseCalculator(NavigatorBioMonForm)
            return render(request, 'campaign-report/detailed.html', data)



        if campaign == 'AKDY - Email':
            data = campaignWiseCalculator(AKDYEmailMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Ibiz':
            data = campaignWiseCalculator(IbizMonForm)
            return render(request, 'campaign-report/detailed.html', data)


        if campaign == 'Daniel Wellington - Chat - Email':
            data = campaignWiseCalculator(DanielWellinChatEmailMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Protostar':
            data = campaignWiseCalculator(ProtostarMonForm)
            return render(request, 'campaign-report/detailed.html', data)


        if campaign == 'Embassy Luxury':
            data = campaignWiseCalculator(EmbassyLuxuryMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'IIB':
            data = campaignWiseCalculator(IIBMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Terraceo - Lead':
            data = campaignWiseCalculator(TerraceoLeadMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Terraceo - Chat - Email':
            data = campaignWiseCalculator(TerraceoChatEmailMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Kalki Fashions':
            data = campaignWiseCalculator(KalkiFashions)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Super Play':
            data = campaignWiseCalculator(SuperPlayMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Practo':
            data = campaignWiseCalculator(PractoMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Scala':
            data = campaignWiseCalculator(ScalaMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Citizen Capital':
            data = campaignWiseCalculator(CitizenCapitalMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Golden East':
            data = campaignWiseCalculator(GoldenEastMonForm)
            return render(request, 'campaign-report/detailed.html', data)


        if campaign == 'Ri8Brain':
            data = campaignWiseCalculator(RitBrainMonForm)
            return render(request, 'campaign-report/detailed.html', data)


        if campaign == 'Restaurant Solution Group':
            data = campaignWiseCalculator(RestaurentSolMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'QBIQ':
            data = campaignWiseCalculator(QBIQMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Accutime':
            data = campaignWiseCalculator(AccutimeMonForm)
            return render(request, 'campaign-report/detailed.html', data)



        if campaign == 'Solar Campaign':
            data = campaignWiseCalculator(SolarCampaignMonForm)
            return render(request, 'campaign-report/detailed.html', data)

        if campaign == 'Yes Health Molina':
            data = campaignWiseCalculator(YesHealthMolinaMonForm)
            return render(request, 'campaign-report/detailed.html', data)


        else:
            return render(request, '')




def signCoaching(request,pk):
    now = datetime.now()
    category=request.POST['category']
    emp_comments=request.POST['emp_comments']

    if category == 'eva-chat':
        coaching=ChatMonitoringFormEva.objects.get(id=pk)
        coaching.status=True
        coaching.closed_date=now
        coaching.emp_comments=emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'pod-chat':
        coaching=ChatMonitoringFormPodFather.objects.get(id=pk)
        coaching.status=True
        coaching.closed_date=now
        coaching.emp_comments=emp_comments
        coaching.save()
        return redirect('/employees/agenthome')

    elif category == 'fla':
        coaching = FLAMonitoringForm.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'mt':
        coaching = MTCosmeticsMonForm.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')


    elif category == 'pix-inbound':
        coaching = PrinterPixMasterMonitoringFormInboundCalls.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'pix-chat':
        coaching = PrinterPixMasterMonitoringFormChatsEmail.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'aadya':
        coaching = MonitoringFormLeadsAadhyaSolution.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'insalvage':
        coaching = MonitoringFormLeadsInsalvage.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'medicare':
        coaching = MonitoringFormLeadsMedicare.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'cts':
        coaching = MonitoringFormLeadsCTS.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'tfood':
        coaching = MonitoringFormLeadsTentamusFood.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'tpet':
        coaching = MonitoringFormLeadsTentamusPet.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'city':
        coaching = MonitoringFormLeadsCitySecurity.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')

    elif category == 'allen':
        coaching = MonitoringFormLeadsAllenConsulting.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'system4':
        coaching = MonitoringFormLeadsSystem4.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'louis':
        coaching = MonitoringFormLeadsLouisville.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'info':
        coaching = MonitoringFormLeadsInfothinkLLC.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'psecu':
        coaching = MonitoringFormLeadsPSECU.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')
    elif category == 'get':
        coaching = MonitoringFormLeadsGetARates.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')

    elif category == 'advance':
        coaching = MonitoringFormLeadsAdvanceConsultants.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')

    elif category == 'furbaby':
        coaching = FurBabyMonForm.objects.get(id=pk)
        coaching.status = True
        coaching.closed_date = now
        coaching.emp_comments = emp_comments
        coaching.save()
        return redirect('/employees/agenthome')


    else:
        return redirect('/employees/agenthome')


def coachingSuccess(request):

    return render(request,'coaching-success-message.html')

def coachingDispute(request,pk):

    emp_comments = request.POST['emp_comments_dispute']
    emp_name=request.user.profile.emp_name
    manager_name = request.user.profile.manager
    manager_mail=Profile.objects.get(emp_name=manager_name)
    manager_email=manager_mail.email

    # Email Contents
    subject_of_email='Coaching dispute of -'+emp_name
    body_of_email = 'Hello ,'+ '\n' + 'The QA socre for the following call is being disputed by '+' - '+emp_name +'\n for the following reasons -- >\n' + emp_comments +'\n -- Request you to follow up on this with the concerned as the coaching will remain OPEN until resolved, and will not reflect in the QA Scorecard.'

    def sendEmail(email):

        send_mail(subject_of_email, #Subject
                  body_of_email,#Body
                  'qms@expertcallers.com',# From
                  ['kalesh.cv@expertcallers.com','aravindh.s@expertcallers.com'],# To
                  fail_silently=False)

    if request.method == 'POST':

        #Sending Mail
        sendEmail(manager_email)

        team = request.user.profile.team
        team = Team.objects.get(name=team)

        cid=pk
        campaign=request.POST['campaign']

        def disputeStatusChange(monform):

            obj=monform.objects.get(id=cid)
            obj.disput_status=True
            obj.emp_comments=emp_comments
            obj.save()


        if campaign == 'Noom-POD':
            disputeStatusChange(ChatMonitoringFormPodFather)

        if campaign == 'Noom-EVA':
            disputeStatusChange(ChatMonitoringFormEva)

        if campaign == 'FLA':
            disputeStatusChange(FLAMonitoringForm)

        if campaign == 'MT Cosmetic':
            disputeStatusChange(MTCosmeticsMonForm)


        if campaign == 'Printer Pix Chat Email':
            disputeStatusChange(PrinterPixMasterMonitoringFormChatsEmail)

        if campaign == 'Printer Pix Inbound':
            disputeStatusChange(PrinterPixMasterMonitoringFormInboundCalls)

        if campaign == 'AAdya':
            disputeStatusChange(MonitoringFormLeadsAadhyaSolution)

        if campaign == 'Insalvage':
            disputeStatusChange(MonitoringFormLeadsInsalvage)

        if campaign == 'Medicare':
            disputeStatusChange(MonitoringFormLeadsMedicare)

        if campaign == 'CTS':
            disputeStatusChange(MonitoringFormLeadsCTS)

        if campaign == 'Tentamus Food':
            disputeStatusChange(MonitoringFormLeadsTentamusFood)

        if campaign == 'Tentamus Pet':
            disputeStatusChange(MonitoringFormLeadsTentamusPet)

        if campaign == 'City Security':
            disputeStatusChange(MonitoringFormLeadsCitySecurity)

        if campaign == 'Allen Consulting':
            disputeStatusChange(MonitoringFormLeadsAllenConsulting)

        if campaign == 'System4':
            disputeStatusChange(MonitoringFormLeadsSystem4)

        if campaign == 'Louisville':
            disputeStatusChange(MonitoringFormLeadsLouisville)

        if campaign == 'Info Think LLC':
            disputeStatusChange(MonitoringFormLeadsInfothinkLLC)

        if campaign == 'PSECU':
            disputeStatusChange(MonitoringFormLeadsPSECU)

        if campaign == 'Get A Rates':
            disputeStatusChange(MonitoringFormLeadsGetARates)

        if campaign == 'Advance Consultants':
            disputeStatusChange(MonitoringFormLeadsAdvanceConsultants)

        if campaign == 'Fur Baby':
            disputeStatusChange(FurBabyMonForm)


        else:
            pass

        data={'team':team}
        return render(request,'coaching-dispute-message.html',data)
    else:
        return redirect('/employees/agenthome')

def qahome(request):



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
                        ClearViewEmailMonForm,FinesseMortgageEmailMonForm,DigitalSwissGoldEmailChatMonForm

                        ]

    empw_list = []

    if request.method=='POST':

        qa_name=request.user.profile.emp_name
        user_id=request.user.id
        teams=Team.objects.all()

        currentMonth = request.POST['month']
        currentYear = request.POST['year']



        for i in list_of_monforms:
            emp_wise = i.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,added_by=qa_name).values(
            'associate_name','process').annotate(dcount=Count('associate_name')).annotate(davg=Avg('overall_score')).order_by(
            '-davg')
            empw_list.append(emp_wise)


        # Total NO of Coachings
        total_coaching_ids=[]

        for i in list_of_monforms:
            x=i.objects.filter(added_by=qa_name)

            for i in x:
                total_coaching_ids.append(i.id)

        total_coaching=len(total_coaching_ids)

        # All coaching objects

        all_coaching_obj=[]

        for i in list_of_monforms:
            x=i.objects.filter(added_by=qa_name,audit_date__year=currentYear, audit_date__month=currentMonth).order_by('audit_date')
            all_coaching_obj.append(x)

    ##### Open_campaigns_objects  ############

        list_open_campaigns=[]

        for i in list_of_monforms:
            opn_cmp_obj=i.objects.filter(status=False,added_by=qa_name,audit_date__year=currentYear, audit_date__month=currentMonth)
            list_open_campaigns.append(opn_cmp_obj)

    ################### opn_count #############

        list_of_open_count=[]

        for i in list_of_monforms:

            count=i.objects.filter(added_by=qa_name,status=False,audit_date__year=currentYear, audit_date__month=currentMonth).count()
            list_of_open_count.append(count)

        total_open_coachings=sum(list_of_open_count)

        ######## Quality Score

        ###################  Avg Campaignwise

        avg_campaignwise = []
        campaign_wise_count = []
        fatal_list = []

        for i in list_of_monforms:
            emp_wise = i.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,qa=qa_name).values('process').annotate(davg=Avg('overall_score'))
            camp_wise_count = i.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth, overall_score__lt=100).values('process').annotate(
                dcount=Count('associate_name'))
            fatal_count = i.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth).values('process').annotate(dcount=Sum('fatal_count'))

            avg_campaignwise.append(emp_wise)
            campaign_wise_count.append(camp_wise_count)
            fatal_list.append(fatal_count)

            #############################################

        campaigns_from_db = Campaigns.objects.all()

        data={'teams':teams,

              'total_open':total_open_coachings,'total_coaching':total_coaching,
              'all_c_obj':all_coaching_obj,

              'open_campaigns':list_open_campaigns,
              'emp_wise_score':empw_list,

              'avg_campaignwise': avg_campaignwise,
              'camp_wise_count': campaign_wise_count,
              'fatal_list': fatal_list,
              'campaigns':campaigns_from_db,

              }

        return render(request,'qa-home.html',data)

    else:
        qa_name = request.user.profile.emp_name
        user_id = request.user.id
        teams = Team.objects.all()

        currentMonth = datetime.now().month
        currentYear = datetime.now().year

        ######### List of All Coachings ##############3


        empw_list = []

        for i in list_of_monforms:
            emp_wise = i.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,
                                        added_by=qa_name).values(
                'associate_name','process').annotate(dcount=Count('associate_name')).annotate(davg=Avg('overall_score')).order_by(
                '-davg')[:10]
            empw_list.append(emp_wise)

        # Total NO of Coachings
        total_coaching_ids = []

        for i in list_of_monforms:
            x = i.objects.filter(added_by=qa_name)

            for i in x:
                total_coaching_ids.append(i.id)

        total_coaching = len(total_coaching_ids)

        # All coaching objects

        all_coaching_obj = []

        for i in list_of_monforms:
            x = i.objects.filter(added_by=qa_name, audit_date__year=currentYear,
                                 audit_date__month=currentMonth).order_by('audit_date')
            all_coaching_obj.append(x)

        ##### Open_campaigns_objects  ###############

        list_open_campaigns = []

        for i in list_of_monforms:
            opn_cmp_obj = i.objects.filter(status=False, added_by=qa_name, audit_date__year=currentYear,
                                           audit_date__month=currentMonth)
            list_open_campaigns.append(opn_cmp_obj)

        ################### opn_count #############

        list_of_open_count = []

        for i in list_of_monforms:
            count = i.objects.filter(added_by=qa_name, status=False, audit_date__year=currentYear,
                                     audit_date__month=currentMonth).count()
            list_of_open_count.append(count)

        total_open_coachings = sum(list_of_open_count)

        ######## Quality Score

        ###################  Avg Campaignwise

        avg_campaignwise = []
        campaign_wise_count = []
        fatal_list = []

        for i in list_of_monforms:
            emp_wise = i.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,qa=qa_name).values(
                'process').annotate(davg=Avg('overall_score'))
            camp_wise_count = i.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth,
                                               overall_score__lt=100).values('process').annotate(
                dcount=Count('associate_name'))
            fatal_count = i.objects.filter(audit_date__year=currentYear, audit_date__month=currentMonth).values(
                'process').annotate(dcount=Sum('fatal_count'))

            avg_campaignwise.append(emp_wise)
            campaign_wise_count.append(camp_wise_count)
            fatal_list.append(fatal_count)

            #############################################
        campaigns_from_db = Campaigns.objects.all()

        data = {'teams': teams,

                'total_open': total_open_coachings, 'total_coaching': total_coaching,
                'all_c_obj': all_coaching_obj,

                'open_campaigns': list_open_campaigns,
                'emp_wise_score': empw_list,

                'avg_campaignwise': avg_campaignwise,
                'camp_wise_count': campaign_wise_count,
                'fatal_list': fatal_list,

                'campaigns':campaigns_from_db

                }

        return render(request, 'qa-home.html', data)

# Final Forms

def chatCoachingformEva(request):
    if request.method == 'POST':
        category='chat'
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
        category='chat'
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
        category='Email'
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
        return render(request, 'mon-forms/Fame-house-mon-form.html', data)



def flaMonForm(request):
    if request.method == 'POST':
        category='other'
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



#campaign View

def campaignView(request):

    if request.method=='POST':

        campaign_id = request.POST['campaign_id']
        campaign = Campaigns.objects.get(id=campaign_id)
        agents=Profile.objects.all().order_by('emp_name')

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



        '''if audit_form=='Noom-EVA':
            agent=Profile.objects.get(emp_id=agent_id)
            data = {'agent':agent,'team':team}
            return render(request, 'mon-forms/ECPL-EVA&NOVO-Monitoring-Form-chat.html', data)

        elif audit_form=='Noom-POD':
            agent = Profile.objects.get(emp_id=agent_id)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/ECPL-Pod-Father-Monitoring-Form-chat.html', data)

        elif audit_form=='Nucleus':
            agent = Profile.objects.get(emp_id=agent_id)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/ECPL-INBOUND-CALL-MONITORING-FORM.html', data)

        elif audit_form=='Fame House':

            agent = Profile.objects.get(emp_id=agent_id)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/fame-house-new.html', data)

        elif audit_form=='FLA':
            agent = Profile.objects.get(emp_id=agent_id)
            data = {'agent': agent, 'team': team, 'date': new_today_date}

            return render(request, 'mon-forms/FLA-mon-form.html', data)



        elif audit_form=='Tonn Chat Email':
            agent = Profile.objects.get(emp_id=agent_id)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/ECPL-Chat-Email-MONITORING-FORM.html', data)


        elif audit_form=='Movement of Insurance':
            agent = Profile.objects.get(emp_id=agent_id)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/Master-Monitoring-Form-Movement-Insurance.html', data)

        elif audit_form=='Wit Digital':
            agent = Profile.objects.get(emp_id=agent_id)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/Wit-Digital-Mastering-Monitoring-Form.html', data)

        elif audit_form == 'Printer Pix Chat Email':
            agent = Profile.objects.get(emp_id=agent_id)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/Printer-Pix-Master-Monitoring-Form-Chats-Email.html', data)

        elif audit_form == 'Printer Pix Inbound':
            agent = Profile.objects.get(emp_id=agent_id)
            data = {'agent': agent, 'team': team}
            return render(request, 'mon-forms/Printer-Pix-Master-Monitoring-Form-Inbound-Calls.html', data)

        elif audit_form == 'AAdya' or audit_form == 'Insalvage' or audit_form == 'Medicare' or audit_form == 'CTS' or audit_form == 'Tentamus Food' or audit_form == 'Tentamus Pet' or audit_form == 'City Security' or audit_form == 'Allen Consulting' or audit_form == 'System4' or audit_form == 'Louisville' or audit_form == 'Info Think LLC' or audit_form == 'PSECU' or audit_form == 'Get A Rates' or audit_form == 'Advance Consultants' or audit_form == 'Upfront Online LLC' or audit_form == 'Micro Distributing' or audit_form == 'JJ Studio':



        elif audit_form == 'Zero Stress Marketing' or audit_form =='WTU' or audit_form =='Roof Well' or audit_form == 'Glyde App' or audit_form == 'Millennium Scientific' or audit_form == 'Finesse Mortgage' or audit_form == 'Stand Spot' or audit_form == 'Cam Industrial' or audit_form == 'Optimal Student Loan' or audit_form == 'Navigator Bio' or audit_form == 'AKDY - Inbound':
            agent = Profile.objects.get(emp_id=agent_id)
            data = {'agent': agent, 'team': team,'date':new_today_date}
            return render(request, 'mon-forms/new-series-common.html', data)

        elif audit_form == 'Ibiz' or audit_form == 'Aditya Birla Cellulose' or audit_form == 'Bhagyalaxmi Industries' or audit_form == 'Digital Swiss Gold' or audit_form == 'Naffa Innovations' or audit_form =='Daniel Wellington - Inbound' or audit_form =='Protostar' or audit_form == 'Kappi machine' or audit_form == 'Somethings Brewing' or audit_form == 'AB - Hindalco' or audit_form == 'Embassy Luxury' or audit_form == 'IIB' or audit_form == 'Terraceo - Lead' or audit_form == 'Kalki Fashions':
            agent = Profile.objects.get(emp_id=agent_id)
            data = {'agent': agent, 'team': team,'date':new_today_date}
            return render(request, 'mon-forms/new-series-common.html', data)

        elif audit_form=='MT Cosmetic':
            agent = Profile.objects.get(emp_id=agent_id)
            data = {'agent': agent, 'team': team, 'date': new_today_date}
            return render(request, 'mon-forms/new-series-common.html', data)

        elif audit_form=='Scala' or audit_form=='Citizen Capital' or audit_form=='Golden East':
            agent = Profile.objects.get(emp_id=agent_id)
            data = {'agent': agent, 'team': team, 'date': new_today_date}
            return render(request, 'mon-forms/new-series-common.html', data)


        elif audit_form == 'Super Play' or audit_form =='Daniel Wellington - Chat - Email' or audit_form =='Terraceo - Chat - Email' or audit_form =='Practo':
            agent = Profile.objects.get(emp_id=agent_id)
            data = {'agent': agent, 'team': team,'date':new_today_date}
            return render(request, 'mon-forms/email-chat.html', data)

        elif audit_form == 'Fur Baby' or audit_form == 'Maxwell Properties'or audit_form == 'AKDY - Email':
            agent = Profile.objects.get(emp_id=agent_id)
            data = {'agent': agent, 'team': team, 'date': new_today_date}
            return render(request, 'mon-forms/inter-email-chat.html', data)

        elif audit_form == 'Clear View':
            agent = Profile.objects.get(emp_id=agent_id)
            data = {'agent': agent, 'team': team, 'date': new_today_date}
            return render(request, 'mon-forms/clear-view.html', data)
        elif audit_form == 'PrinterPix':
            agent = Profile.objects.get(emp_id=agent_id)
            data = {'agent': agent, 'team': team, 'date': new_today_date}
            return render(request, 'mon-forms/printer-pix.html', data)

        elif audit_form == 'Pluto Management':
            agent = Profile.objects.get(emp_id=agent_id)
            data = {'agent': agent, 'team': team, 'date': new_today_date}
            return render(request, 'mon-forms/pluto-management.html', data)

        elif audit_form == 'Sterling Strategies':
            agent = Profile.objects.get(emp_id=agent_id)
            data = {'agent': agent, 'team': team, 'date': new_today_date}
            return render(request, 'mon-forms/sterling-strategies.html', data)

        elif audit_form == 'Ri8Brain':
            agent = Profile.objects.get(emp_id=agent_id)
            data = {'agent': agent, 'team': team, 'date': new_today_date}
            return render(request, 'mon-forms/new-series-common.html', data)

        elif audit_form == 'Healthy Plus' or audit_form == 'Solar Campaign' or audit_form == 'Yes Health Molina':
            agent = Profile.objects.get(emp_id=agent_id)
            data = {'agent': agent, 'team': team, 'date': new_today_date}
            return render(request, 'mon-forms/new-series-common.html', data)

        elif audit_form == 'Restaurant Solution Group' or audit_form =='QBIQ' or audit_form =='Accutime' or audit_form =='Tonn Coa - Inbound':
            agent = Profile.objects.get(emp_id=agent_id)
            data = {'agent': agent, 'team': team, 'date': new_today_date}
            return render(request, 'mon-forms/new-series-common.html', data)

        elif audit_form == 'Amerisave - Call':
            agent = Profile.objects.get(emp_id=agent_id)
            data = {'agent': agent, 'team': team, 'date': new_today_date}
            return render(request, 'mon-forms/amerisave-calls.html', data)

        elif audit_form == 'Amerisave - Email':
            agent = Profile.objects.get(emp_id=agent_id)
            data = {'agent': agent, 'team': team, 'date': new_today_date}
            return render(request, 'mon-forms/amerisave-email.html', data)'''



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
                       'Fatal Count', 'qa', 'am', 'team_lead', 'manager','ticket_no','ticket_type',

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
            rows = FameHouseNewMonForm.objects.filter(audit_date__range=[start_date, end_date],).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am', 'team_lead', 'manager','ticket_no','ticket_type',

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


        elif campaign == 'Noom-POD':

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
                       'qa', 'am', 'team_lead', 'manager','ticket_no',

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
                'team_lead', 'manager','ticket_no',

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

        elif campaign == 'Noom-EVA':

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
                       'qa', 'am', 'team_lead', 'manager','ticket_no',

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
            rows = ChatMonitoringFormEva.objects.filter(audit_date__range=[start_date, end_date], ).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager','ticket_no',

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



        elif campaign == 'Printer Pix Inbound':

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
            rows = PrinterPixMasterMonitoringFormInboundCalls.objects.filter(audit_date__range=[start_date, end_date],
                                                                             ).values_list(
                'process', 'emp_id', 'associate_name', 'call_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager',

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



        elif campaign == 'Printer Pix Chat Email':

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

                       'Associate used the standard greeting format',
                       'Appropriate responses ( acknowledging at the right time)',
                       'Ownership on Emails / Chat',
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
            rows = PrinterPixMasterMonitoringFormChatsEmail.objects.filter(
                audit_date__range=[start_date, end_date], ).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager',

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

        elif campaign == 'Fur Baby':

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

                       'Associate used the standard greeting format',
                       'Appropriate responses ( acknowledging at the right time)',
                       'Ownership on Emails / Chat Answered within 30',
                       'Personalization ( building a Raport, Addressing by name)',
                       'Empathy/Sympathy',
                       'Sentence structure',
                       'Punctuation (full stop, comma, and brackets, used in writing to separate sentences)',
                       'Grammar (Tense, Noun, etc.)',
                       'Probing done whenever necessary',
                       'Recap (Summarization of the conversation)',
                       'Associate used the standard closing format',

                       'Accurate Resolution/Information is provided as per the process',
                       'Worked on the Ticket Assigned / Chat Responded within 3 mins',

                       'Professional / Courtesy',
                       'Follow up done on the Pending Tickets( Chats & Email)',
                       'Retruns Updated in the google sheet',
                       'Process & Procedure Followed (Refund Process Followed)',
                       'First Chat / Email Resolution',

                       'status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = FurBabyMonForm.objects.filter(
                audit_date__range=[start_date, end_date], ).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager',

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



        elif campaign == 'AKDY - Email':

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

                       'Associate used the standard greeting format',
                       'Appropriate responses ( acknowledging at the right time)',
                       'Ownership on Emails / Chat Answered within 30',
                       'Personalization ( building a Raport, Addressing by name)',
                       'Empathy/Sympathy',
                       'Sentence structure',
                       'Punctuation (full stop, comma, and brackets, used in writing to separate sentences)',
                       'Grammar (Tense, Noun, etc.)',
                       'Probing done whenever necessary',
                       'Recap (Summarization of the conversation)',
                       'Associate used the standard closing format',

                       'Accurate Resolution/Information is provided as per the process',
                       'Worked on the Ticket Assigned / Chat Responded within 3 mins',

                       'Professional / Courtesy',
                       'Follow up done on the Pending Tickets( Chats & Email)',
                       'Retruns Updated in the google sheet',
                       'Process & Procedure Followed (Refund Process Followed)',
                       'First Chat / Email Resolution',

                       'status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = AKDYEmailMonForm.objects.filter(
                audit_date__range=[start_date, end_date], ).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager',

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

        elif campaign == 'Daniel Wellington - Chat - Email':

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

                       'Associate used the standard greeting format',
                       'Appropriate responses ( acknowledging at the right time)',
                       'Ownership on Emails / Chat',
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
            rows = DanielWellinChatEmailMonForm.objects.filter(
                audit_date__range=[start_date, end_date], ).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager',

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

        elif campaign == 'Terraceo - Chat - Email':

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

                       'Associate used the standard greeting format',
                       'Appropriate responses ( acknowledging at the right time)',
                       'Ownership on Emails / Chat',
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
            rows = TerraceoChatEmailMonForm.objects.filter(
                audit_date__range=[start_date, end_date], ).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager',

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

        elif campaign == 'Super Play':

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

                       'Associate used the standard greeting format',
                       'Appropriate responses ( acknowledging at the right time)',
                       'Ownership on Emails / Chat',
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
            rows = SuperPlayMonForm.objects.filter(
                audit_date__range=[start_date, end_date], ).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager',

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
                       'qa', 'am', 'team_lead', 'manager', 'customer_name','customer_contact',

                       'Associate used the standard greeting format',
                       'Appropriate responses ( acknowledging at the right time)',
                       'Ownership on Emails / Chat',
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
            rows = PractoMonForm.objects.filter(
                audit_date__range=[start_date, end_date], ).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager', 'customer_name','customer_contact',

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
                audit_date__range=[start_date, end_date], ).values_list(
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
                       'Fatal Count', 'qa', 'am', 'team_lead', 'manager','ticket_no','ticket_type',

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
                'am', 'team_lead', 'manager','ticket_no','ticket_type',

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



        elif campaign == 'Noom-POD':

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
                       'qa', 'am', 'team_lead', 'manager','ticket_no',

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
                'team_lead', 'manager','ticket_no',

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

        elif campaign == 'Noom-EVA':

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
                       'qa', 'am', 'team_lead', 'manager','ticket_no',

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
                'team_lead', 'manager','ticket_no',

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



        elif campaign == 'Printer Pix Inbound':

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
            rows = PrinterPixMasterMonitoringFormInboundCalls.objects.filter(audit_date__range=[start_date, end_date], qa=qa
                                                                             ).values_list(
                'process', 'emp_id', 'associate_name', 'call_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager',

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





        elif campaign == 'Printer Pix Chat Email':

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

                       'Associate used the standard greeting format',
                       'Appropriate responses ( acknowledging at the right time)',
                       'Ownership on Emails / Chat',
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
            rows = PrinterPixMasterMonitoringFormChatsEmail.objects.filter(
                audit_date__range=[start_date, end_date], qa=qa).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager',

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

        elif campaign == 'Fur Baby':

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

                       'Associate used the standard greeting format',
                       'Appropriate responses ( acknowledging at the right time)',
                       'Ownership on Emails / Chat Answered within 30',
                       'Personalization ( building a Raport, Addressing by name)',
                       'Empathy/Sympathy',
                       'Sentence structure',
                       'Punctuation (full stop, comma, and brackets, used in writing to separate sentences)',
                       'Grammar (Tense, Noun, etc.)',
                       'Probing done whenever necessary',
                       'Recap (Summarization of the conversation)',
                       'Associate used the standard closing format',

                       'Accurate Resolution/Information is provided as per the process',
                       'Worked on the Ticket Assigned / Chat Responded within 3 mins',

                       'Professional / Courtesy',
                       'Follow up done on the Pending Tickets( Chats & Email)',
                       'Retruns Updated in the google sheet',
                       'Process & Procedure Followed (Refund Process Followed)',
                       'First Chat / Email Resolution',

                       'status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = FurBabyMonForm.objects.filter(
                audit_date__range=[start_date, end_date], qa=qa).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager',

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


        elif campaign == 'AKDY - Email':

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

                       'Associate used the standard greeting format',
                       'Appropriate responses ( acknowledging at the right time)',
                       'Ownership on Emails / Chat Answered within 30',
                       'Personalization ( building a Raport, Addressing by name)',
                       'Empathy/Sympathy',
                       'Sentence structure',
                       'Punctuation (full stop, comma, and brackets, used in writing to separate sentences)',
                       'Grammar (Tense, Noun, etc.)',
                       'Probing done whenever necessary',
                       'Recap (Summarization of the conversation)',
                       'Associate used the standard closing format',

                       'Accurate Resolution/Information is provided as per the process',
                       'Worked on the Ticket Assigned / Chat Responded within 3 mins',

                       'Professional / Courtesy',
                       'Follow up done on the Pending Tickets( Chats & Email)',
                       'Retruns Updated in the google sheet',
                       'Process & Procedure Followed (Refund Process Followed)',
                       'First Chat / Email Resolution',

                       'status',
                       'closed_date', 'fatal', 'areas_improvement', 'positives', 'comments']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()
            rows = AKDYEmailMonForm.objects.filter(
                audit_date__range=[start_date, end_date], qa=qa).values_list(
                'process', 'emp_id', 'associate_name', 'trans_date', 'audit_date', 'overall_score', 'fatal_count', 'qa',
                'am',
                'team_lead', 'manager',

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

        elif campaign == 'Daniel Wellington - Chat - Email':

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
                       'Ownership on Emails / Chat',
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
            rows = DanielWellinChatEmailMonForm.objects.filter(
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

        elif campaign == 'Terraceo - Chat - Email':

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
                       'Ownership on Emails / Chat',
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
            rows = TerraceoChatEmailMonForm.objects.filter(
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

        elif campaign == 'Super Play':

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
                       'Ownership on Emails / Chat',
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
            rows = SuperPlayMonForm.objects.filter(
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
                       'qa', 'am', 'team_lead', 'manager','customer_name','customer_contact',

                       'Associate used the standard greeting format',
                       'Appropriate responses ( acknowledging at the right time)',
                       'Ownership on Emails / Chat',
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
            rows = PractoMonForm.objects.filter(
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
                                week=week,am=am,fatal_count=no_of_fatals,fatal=fatal
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




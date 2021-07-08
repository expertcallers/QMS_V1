
from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    #Guidelines
    path('outbound-monitoring-guidelines',outboundGuidelines),
    path('inbound-monitoring-guidelines',inboundGuidelines),
    path('chat-monitoring-guidelines',chatGuidelines),
    path('email-monitoring-guidelines',emailGuidelines),

    # Monitoring Forms
    path('ECPL-EVA&NOVO-Monitoring-Form-chat',chatCoachingformEva),
    path('ECPL-Pod-Father-Monitoring-Form-chat',chatCoachingformPodFather),

    path('fame-house-new',fameHouseNew),
    path('gubagoo-audit-submit',gubaGooNew),

    path('ECPL-FLA-MONITORING_FORM',flaMonForm),


    path('Monitoring-Form-new-series-common',newSeriesMonForms),
    path('new-series-inbound',newSeriesInboundForms),

    path('email-chat-mon-form',domesticChatEmail),




#### Credentials
    path('accounts/login/',login_view),
    path('signup',signup),
    path('login',login_view),
    path('logout',logout_view),
    path('change_password',change_password),

    path('agenthome',agenthome),
    path('qahome',qahome),
    path('manager-home',qualityDashboardMgt),
    path('quality-dashboard-mgt',qualityDashboardMgt),


    path('quality-dashboard',qualityDashboard),


    # Coaching Views
    path('coaching-view-emp/<str:process>/<int:pk>',coachingViewAgents),
    path('coaching-view-qa-all/<str:process>/<int:pk>',coachingViewQaDetailed),

    path('campaign-wise-coaching-view',campaignwiseCoachings),
    path('campaign-wise-coaching-view-qa',campaignwiseCoachingsQA),
    path('campaign-wise-coaching-view-agent',campaignwiseCoachingsAgent),
    path('employee-wise-report', employeeWiseReport),
    path('manager-wise-report', managerWiseReport),


    path('coaching/signcoaching/<int:pk>',signCoaching),
    path('campaign-view',campaignView),
    path('add-coaching',selectCoachingForm),
    path('coaching-summary-view',coachingSummaryView),
    path('coaching-success',coachingSuccess),
    path('coaching-dispute/<int:pk>',coachingDispute),

    # Summary

    ##############3
    path('campaign-detailed-view/<str:cname>',campaignwiseDetailedReport),


    path('export-data',exportAuditReport),
    path('export-data-qa',exportAuditReportQA),

    path('adduser',addtoUserModel),
    path('update-email-address/<int:pk>',updateEmailAddress),

    path('update-profile',updateProfile),
    path('checkprofile',checkProfile),

    #path('add-single-profile',addSingleProfile),

    ## Admin

    path('add-new-campaign',addNewCampaign),


    #############3

    path('powerbi-test',powerBITest),

    path('process-change',processNameChanger),

    path('desi-changer',desiChanger),

    path('change-password',changePassword),

    path('delete',deleteData),
    path('campaigns',campaignDetails),

    path('allprofileupdate',AllProfileUpdate),

]

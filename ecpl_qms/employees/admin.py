from django.contrib import admin

from .models import *


class CampaignSearch(admin.ModelAdmin):
    search_fields = ('name','type')
    list_display = ('name','type')

class profileSearch(admin.ModelAdmin):
    search_fields = ('emp_id','emp_name')
    list_display = ('emp_id','emp_name')
class Search(admin.ModelAdmin):
    search_fields = ('qa','emp_id','associate_name')
    list_display = ('associate_name','emp_id','qa')

admin.site.register(Team)
admin.site.register(Profile,profileSearch)
admin.site.register(Process)
admin.site.register(Empdata)
admin.site.register(Campaigns,CampaignSearch)
admin.site.register(ProfileCreatedByManagers)
admin.site.register(PractoWithSubCategory)

admin.site.register(ProfileNewtoAddUserandProfile)

# Monitoring Forms

admin.site.register(ChatMonitoringFormEva,Search)     # view done
admin.site.register(ChatMonitoringFormPodFather,Search)     # view done
admin.site.register(FameHouseNewMonForm,Search)
admin.site.register(FLAMonitoringForm,Search)     # view done
admin.site.register(MTCosmeticsMonForm,Search)      # view done
admin.site.register(MasterMonitoringFormTonnCoaInboundCalls,Search)
admin.site.register(MonitoringFormLeadsAadhyaSolution,Search)
admin.site.register(PrinterPixMasterMonitoringFormInboundCalls,Search)
admin.site.register(PrinterPixMasterMonitoringFormChatsEmail,Search)
admin.site.register(MonitoringFormLeadsInsalvage,Search)
admin.site.register(MonitoringFormLeadsMedicare,Search)
admin.site.register(MonitoringFormLeadsCTS,Search)
admin.site.register(MonitoringFormLeadsTentamusFood,Search)
admin.site.register(MonitoringFormLeadsTentamusPet,Search)
admin.site.register(MonitoringFormLeadsCitySecurity,Search)
admin.site.register(MonitoringFormLeadsAllenConsulting,Search)
admin.site.register(MonitoringFormLeadsSystem4,Search)
admin.site.register(MonitoringFormLeadsLouisville,Search)
admin.site.register(MonitoringFormLeadsInfothinkLLC,Search)
admin.site.register(MonitoringFormLeadsPSECU,Search)
admin.site.register(MonitoringFormLeadsGetARates,Search)
admin.site.register(MonitoringFormLeadsAdvanceConsultants,Search)
admin.site.register(FurBabyMonForm,Search)
admin.site.register(UpfrontOnlineLLCMonform,Search)
admin.site.register(MicroDistributingMonForm,Search)
admin.site.register(JJStudioMonForm,Search)
admin.site.register(ZeroStressMarketingMonForm,Search)
admin.site.register(WTUMonForm,Search)
admin.site.register(RoofWellMonForm,Search)
admin.site.register(GlydeAppMonForm,Search)
admin.site.register(MillenniumScientificMonForm,Search)
admin.site.register(StandSpotMonForm,Search)
admin.site.register(CamIndustrialMonForm,Search)
admin.site.register(OptimalStudentLoanMonForm,Search)
admin.site.register(NavigatorBioMonForm,Search)
admin.site.register(AKDYEmailMonForm,Search)
admin.site.register(IbizMonForm,Search)
admin.site.register(DanielWellinChatEmailMonForm,Search)
admin.site.register(ProtostarMonForm,Search)
admin.site.register(ABHindalcoInboundMonForm,Search)
admin.site.register(AmerisaveEmailMonForm,Search)
admin.site.register(DanielWellingtonOutboundMonForm,Search)
admin.site.register(DigitalSwissGoldOutboundMonForm,Search)
admin.site.register(EmbassyLuxuryMonForm,Search)
admin.site.register(IIBMonForm,Search)
admin.site.register(TerraceoLeadMonForm,Search)
admin.site.register(TerraceoChatEmailMonForm,Search)
admin.site.register(KalkiFashions,Search)
admin.site.register(SuperPlayMonForm,Search)
admin.site.register(PractoMonForm,Search)
admin.site.register(ScalaMonForm,Search)
admin.site.register(GoldenEastMonForm,Search)
admin.site.register(CitizenCapitalMonForm,Search)
admin.site.register(RitBrainMonForm,Search)
admin.site.register(RestaurentSolMonForm,Search)
admin.site.register(QBIQMonForm,Search)
admin.site.register(AccutimeMonForm,Search)
admin.site.register(latest)
admin.site.register(HiveIncubatorsOutboundMonForm,Search)
admin.site.register(IEDHHInboundMonForm,Search)
admin.site.register(Ri8BrainEmailMonForm,Search)
admin.site.register(QuickAutoPartsOutboundMonForm,Search)
admin.site.register(PractoNewVersion,Search)
admin.site.register(GubagooAuditForm,Search)
admin.site.register(CleanLivingHealthWellnessOutboundMonForm,Search)
admin.site.register(PractoOutboundMonForm,Search)
admin.site.register(LJHubInboundMonForms,Search)
admin.site.register(ILMakiageEmailChatForm,Search)
admin.site.register(DigitalSwissGoldEmailChatMonForm,Search)
admin.site.register(DawnFinancialOutbound,Search)
admin.site.register(WinopolyOutbound,Search)
admin.site.register(MonitoringFormMobile22InboundCalls,Search)
admin.site.register(XportDigitalOutbound,Search)
admin.site.register(XportDigitalInboundMonForm,Search)
admin.site.register(ABHindalcoMonForm,Search)
admin.site.register(CalistaOutboundMonForm,Search)
admin.site.register(GlobalArkOutboundMonform,Search)
admin.site.register(DIDevelopOutbound,Search)
admin.site.register(FreeholdOutboundMonForm,Search)
admin.site.register(ZeamoOutboundMonForm,Search)
admin.site.register(SapphireMedicalsOutboundMonForm,Search)
admin.site.register(EehhaaaOutboundMonForm,Search)
admin.site.register(CalistaInboundMonForm,Search)
admin.site.register(GlobalArkInboundMonForm,Search)
admin.site.register(AllCarePhysicalTherapyMonform,Search)
admin.site.register(ExecutiveCapitalResourcesmonform,Search)
admin.site.register(BrightWayOutboundmonform,Search)
admin.site.register(BuildinglabLLCOutboundmonform,Search)
admin.site.register(BlazingHogEmailChatmonform,Search)
admin.site.register(HardHatTechnologiesInboundMonForm,Search)
admin.site.register(ThirdWaveInboundMonForm,Search)
admin.site.register(HardHatTechnologiesOutboundmonform,Search)
admin.site.register(GretnaMedicalCenterInboundMonForm,Search)
admin.site.register(ThirdWaveOutboundmonform,Search)
admin.site.register(GlobalPharmaOutboundmonform,Search)
admin.site.register(RedefinePlasticsOutboundmonform,Search)
admin.site.register(K7Outboundmonform,Search)
admin.site.register(TrialMappingOutboundmonform,Search)
admin.site.register(GretnaMedicalCenterEmailChatForm,Search)
admin.site.register(EduClassOutboundmonform,Search)
admin.site.register(CredAvenueOutboundmonform,Search)
admin.site.register(TKAWDIWOutboundmonform,Search)
admin.site.register(DreamPickOutboundmonform,Search)
admin.site.register(NerotelInboundmonform,Search)
admin.site.register(SpoiledChildChatmonform,Search)
admin.site.register(KheloyarOutboundmonform,Search)
admin.site.register(MaxTradingOutboundmonform,Search)
admin.site.register(ESRTechTalentOutboundmonform,Search)
admin.site.register(GreenConnectOutboundmonform,Search)

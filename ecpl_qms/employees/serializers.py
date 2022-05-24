from rest_framework import serializers
from .models import *

class ChatMonitoringSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChatMonitoringFormPodFather
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class adhyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringFormLeadsAadhyaSolution
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class AccutimeMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccutimeMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']

class MonitoringFormLeadsAdvanceConsultantsSerializer(serializers.ModelSerializer):
        class Meta:
            model = MonitoringFormLeadsAdvanceConsultants
            fields = ['audit_date','associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                      'status']


class MonitoringFormLeadsAllenConsultingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringFormLeadsAllenConsulting
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class CamIndustrialMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CamIndustrialMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class CitizenCapitalMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitizenCapitalMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class MonitoringFormLeadsCitySecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringFormLeadsCitySecurity
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']

class MonitoringFormLeadsCTSSerializer(serializers.ModelSerializer):
        class Meta:
            model = MonitoringFormLeadsCTS
            fields = ['audit_date','associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                      'status']


class EmbassyLuxuryMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmbassyLuxuryMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']



class MonitoringFormLeadsGetARatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringFormLeadsGetARates
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']



class GlydeAppMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlydeAppMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class GoldenEastMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoldenEastMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']

class IbizMonFormSerializer(serializers.ModelSerializer):
        class Meta:
            model = IbizMonForm
            fields = ['audit_date','associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                      'status']


class IIBMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = IIBMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']



class MonitoringFormLeadsInfothinkLLCSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringFormLeadsInfothinkLLC
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class MonitoringFormLeadsInsalvageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringFormLeadsInsalvage
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class JJStudioMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = JJStudioMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']

class KalkiFashionsSerializer(serializers.ModelSerializer):
        class Meta:
            model = KalkiFashions
            fields = ['audit_date','associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                      'status']


class MonitoringFormLeadsLouisvilleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringFormLeadsLouisville
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']



class MonitoringFormLeadsMedicareSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringFormLeadsMedicare
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']

class MicroDistributingMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = MicroDistributingMonForm
        fields = ['audit_date','associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                      'status']

class MillenniumScientificMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = MillenniumScientificMonForm
        fields = ['audit_date','associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                      'status']

class MTCosmeticsMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = MTCosmeticsMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class NavigatorBioMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavigatorBioMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class OptimalStudentLoanMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptimalStudentLoanMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class ProtostarMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProtostarMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class MonitoringFormLeadsPSECUSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringFormLeadsPSECU
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class QBIQMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = QBIQMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class RestaurentSolMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurentSolMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class RitBrainMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = RitBrainMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class RoofWellMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoofWellMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class ScalaMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScalaMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class SolarCampaignMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolarCampaignMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class StandSpotMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = StandSpotMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class MonitoringFormLeadsSystem4Serializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringFormLeadsSystem4
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class MonitoringFormLeadsTentamusFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringFormLeadsTentamusFood
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class MonitoringFormLeadsTentamusPetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringFormLeadsTentamusPet
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class TerraceoLeadMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = TerraceoLeadMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class UpfrontOnlineLLCMonformSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpfrontOnlineLLCMonform
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class WTUMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = WTUMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class YesHealthMolinaMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = YesHealthMolinaMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class ZeroStressMarketingMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZeroStressMarketingMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class ABHindalcoOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ABHindalcoOutboundMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class AdityaBirlaOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdityaBirlaOutboundMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class AmerisaveoutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmerisaveoutboundMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class BhagyaLakshmiOutboundSerializer(serializers.ModelSerializer):
    class Meta:
        model = BhagyaLakshmiOutbound
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class ClearViewOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClearViewOutboundMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class DanielWellingtonOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = DanielWellingtonOutboundMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class DigitalSwissGoldOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalSwissGoldOutboundMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class HealthyplusOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthyplusOutboundMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class MaxwellPropertiesOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaxwellPropertiesOutboundMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class MovementofInsuranceOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovementofInsuranceOutboundMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class SterlingStrategiesOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SterlingStrategiesOutboundMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class TonnCoaOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = TonnCoaOutboundMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class WitDigitalOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = WitDigitalOutboundMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class PosTechOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = PosTechOutboundMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class SchindlerMediaOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchindlerMediaOutboundMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class UPSOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = UPSOutboundMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class PickPackDeliveriesMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickPackDeliveriesMonForm
        fields = ['audit_date','associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class MarceloPerezMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarceloPerezMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class MedTechGroupOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedTechGroupOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class DigitalSignageOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalSignageOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class HiveIncubatorsOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = HiveIncubatorsOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class KaapiMachinesOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = KaapiMachinesOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class SomethingsBrewingOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SomethingsBrewingOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class NaffaOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = NaffaOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class JBNOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = JBNOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class QuickAutoPartsOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuickAutoPartsOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class ApexCommunicationsOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApexCommunicationsOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class LawOfficesOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = LawOfficesOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class WokeUpEnergyOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = WokeUpEnergyOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class FinnesseMortgageOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinnesseMortgageOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class UnitedMortgageOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitedMortgageOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class CleanLivingHealthWellnessOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CleanLivingHealthWellnessOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']



class PractoOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = PractoOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class ImaginariumOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImaginariumOutboundMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                      'status']



class USJacleanOutboundFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = USJacleanOutboundForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class GlobalGalaxyOutboundFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalGalaxyOutboundForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                      'status']



class CommunityHealthProjectIncOutboundSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityHealthProjectIncOutbound
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']



class EducatedAnalyticsLLCOutboundSerializer(serializers.ModelSerializer):
        class Meta:
            model = EducatedAnalyticsLLCOutbound
            fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                      'status']


class NewDimensionPharmacyOutboundSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewDimensionPharmacyOutbound
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class StayNChargeOutboundSerializer(serializers.ModelSerializer):
    class Meta:
        model = StayNChargeOutbound
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class JHEnergyConsultantOutboundSerializer(serializers.ModelSerializer):
    class Meta:
        model = JHEnergyConsultantOutbound
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class MDRGroupLLCOutboundSerializer(serializers.ModelSerializer):
    class Meta:
        model = MDRGroupLLCOutbound
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class CoreySmallInsuranceAgencyOutboundSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreySmallInsuranceAgencyOutbound
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class EduvocateOutboundSerializer(serializers.ModelSerializer):
    class Meta:
        model = EduvocateOutbound
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class CrossTowerOutboundSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrossTowerOutbound
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class DawnFinancialOutboundSerializer(serializers.ModelSerializer):
    class Meta:
        model = DawnFinancialOutbound
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class XportDigitalOutboundSerializer(serializers.ModelSerializer):
    class Meta:
        model = XportDigitalOutbound
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class CalistaOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalistaOutboundMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class GlobalArkOutboundMonformSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalArkOutboundMonform
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class DIDevelopOutboundSerializer(serializers.ModelSerializer):
    class Meta:
        model = DIDevelopOutbound
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class FreeholdOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeholdOutboundMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class ZeamoOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZeamoOutboundMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class SapphireMedicalsOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SapphireMedicalsOutboundMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class EehhaaaOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = EehhaaaOutboundMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class MasterMonitoringFormTonnCoaInboundCallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterMonitoringFormTonnCoaInboundCalls
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class SomethingsBrewingInboundSerializer(serializers.ModelSerializer):
    class Meta:
        model = SomethingsBrewingInbound
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class PrinterPixMasterMonitoringFormInboundCallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrinterPixMasterMonitoringFormInboundCalls
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class NuclusInboundCallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NuclusInboundCalls
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class NaffaInnovationsInboundCallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NaffaInnovationsInboundCalls
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class KappimachineInboundCallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = KappimachineInboundCalls
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class HealthyplusInboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthyplusInboundMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class FinesseMortgageInboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinesseMortgageInboundMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class DigitalSwissGoldInboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalSwissGoldInboundMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class DanielwellingtoInboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = DanielwellingtoInboundMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']
#
#
class BhagyaLakshmiInboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = BhagyaLakshmiInboundMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class AKDYInboundMonFormNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = AKDYInboundMonFormNew
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class AdityaBirlainboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdityaBirlainboundMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class ABHindalcoInboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ABHindalcoInboundMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class RainbowDiagnosticsInboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = RainbowDiagnosticsInboundMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class DecentralizedVisionLTDInboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = DecentralizedVisionLTDInboundMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class IEDHHInboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = IEDHHInboundMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class AmerisaveInboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmerisaveInboundMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class ClearViewInboundMonFormsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClearViewInboundMonForms
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class QuickAutoPartsInboundMonFormsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuickAutoPartsInboundMonForms
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class LJHubInboundMonFormsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LJHubInboundMonForms
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class ObtheraIncInboundMonFormsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObtheraIncInboundMonForms
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class EduvocateInboundMonFormsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EduvocateInboundMonForms
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class CrossTowerInboundMonFormsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrossTowerInboundMonForms
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class SanaLifeScienceInboundSerializer(serializers.ModelSerializer):
    class Meta:
        model = SanaLifeScienceInbound
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class MonitoringFormMobile22InboundCallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringFormMobile22InboundCalls
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class XportDigitalInboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = XportDigitalInboundMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class CalistaInboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalistaInboundMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class GlobalArkInboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalArkInboundMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class SuperPlayMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperPlayMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class DanielWellinChatEmailMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = DanielWellinChatEmailMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class TerraceoChatEmailMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = TerraceoChatEmailMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class TonnChatsEmailNewMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = TonnChatsEmailNewMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class PrinterPixMasterMonitoringFormChatsEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrinterPixMasterMonitoringFormChatsEmail
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class PractoMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = PractoMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class FurBabyMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FurBabyMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class AKDYEmailMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = AKDYEmailMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class AmerisaveEmailMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmerisaveEmailMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class ClearViewEmailMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClearViewEmailMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class FinesseMortgageEmailMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinesseMortgageEmailMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class DigitalSwissGoldEmailChatMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalSwissGoldEmailChatMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class RainbowDiagnosticsEmailMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = RainbowDiagnosticsEmailMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class HiveIncubatorEmailMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = HiveIncubatorEmailMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class MedTechGroupEmailMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedTechGroupEmailMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class Ri8BrainEmailMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ri8BrainEmailMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class ScalaEmailMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScalaEmailMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class KalkiFashionEmailMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = KalkiFashionEmailMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class MaxwellEmailMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaxwellEmailMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class TanaorJewelryEmailMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = TanaorJewelryEmailMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class DecentralizedVisionEmailChatMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = DecentralizedVisionEmailChatMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class USJacleanEmailChatFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = USJacleanEmailChatForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class CrossTowerEmailChatFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrossTowerEmailChatForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class SanaLifeScienceEmailChatFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SanaLifeScienceEmailChatForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class ChatMonitoringFormEvaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMonitoringFormEva
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class ChatMonitoringFormPodFatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMonitoringFormPodFather
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class FameHouseNewMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FameHouseNewMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class FLAMonitoringFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FLAMonitoringForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class PractoNewVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PractoNewVersion
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class GubagooAuditFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = GubagooAuditForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class ILMakiageEmailChatFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ILMakiageEmailChatForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class WinopolyOutboundSerializer(serializers.ModelSerializer):
    class Meta:
        model = WinopolyOutbound
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                  'status']


class ABHindalcoMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ABHindalcoMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']

class BhagyalaxmiChatMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = BhagyalaxmiChatMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']

class SapphireMedicalsChatMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SapphireMedicalsChatMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']

class AllCarePhysicalTherapyMonformSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllCarePhysicalTherapyMonform
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class ExecutiveCapitalResourcesmonformSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutiveCapitalResourcesmonform
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class BrightWayOutboundmonformSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrightWayOutboundmonform
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']

class BuildinglabLLCOutboundmonformSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildinglabLLCOutboundmonform
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']



class BlazingHogEmailChatmonformSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlazingHogEmailChatmonform
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class PractoWithSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PractoWithSubCategory
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']

class GlobalPharmaOutboundmonformSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalPharmaOutboundmonform
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']


class ThirdWaveOutboundmonformSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThirdWaveOutboundmonform
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']

class HardHatTechnologiesOutboundmonformSerializer(serializers.ModelSerializer):
    class Meta:
        model = HardHatTechnologiesOutboundmonform
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']

class RedefinePlasticsOutboundmonformSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedefinePlasticsOutboundmonform
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']

class ThirdWaveInboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThirdWaveInboundMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']

class HardHatTechnologiesInboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = HardHatTechnologiesInboundMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']

class TKAWDIWOutboundmonformSerializer(serializers.ModelSerializer):
    class Meta:
        model = TKAWDIWOutboundmonform
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']

class NerotelInboundmonformSerializer(serializers.ModelSerializer):
    class Meta:
        model = NerotelInboundmonform
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']

class SpoiledChildChatmonformSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpoiledChildChatmonform
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']

class ESRTechTalentOutboundmonformSerializer(serializers.ModelSerializer):
    class Meta:
        model = ESRTechTalentOutboundmonform
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']

class GreenConnectOutboundmonformSerializer(serializers.ModelSerializer):
    class Meta:
        model = GreenConnectOutboundmonform
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']

class JumpRydesEmailChatFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = JumpRydesEmailChatForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']

class CentralMortgageFundingOutboundmonformSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentralMortgageFundingOutboundmonform
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']

class RapidMortgageOutboundmonformSerializer(serializers.ModelSerializer):
    class Meta:
        model = RapidMortgageOutboundmonform
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']

class BridanAssociatesOutboundmonformSerializer(serializers.ModelSerializer):
    class Meta:
        model = BridanAssociatesOutboundmonform
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']

class LinenFinderOutboundmonformSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinenFinderOutboundmonform
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']

class BetterEdOutboundmonformSerializer(serializers.ModelSerializer):
    class Meta:
        model = BetterEdOutboundmonform
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']

class BetterEdInboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = BetterEdInboundMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']

class Com98OutboundmonformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Com98Outboundmonform
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']

class Com98InboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Com98InboundMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']

class GretnaMedicalCentreOutboundmonformSerializer(serializers.ModelSerializer):
    class Meta:
        model = GretnaMedicalCentreOutboundmonform
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']

class AristaMDOutboundmonformSerializer(serializers.ModelSerializer):
    class Meta:
        model = AristaMDOutboundmonform
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']

class OpenWindsInboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenWindsInboundMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status', 'status']
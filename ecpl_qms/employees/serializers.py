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

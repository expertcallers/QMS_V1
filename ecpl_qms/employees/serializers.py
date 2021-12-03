from rest_framework import serializers
from .models import *

class ChatMonitoringSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChatMonitoringFormPodFather
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class adhyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringFormLeadsAadhyaSolution
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class AccutimeMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccutimeMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']

class MonitoringFormLeadsAdvanceConsultantsSerializer(serializers.ModelSerializer):
        class Meta:
            model = MonitoringFormLeadsAdvanceConsultants
            fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                      'status']


class MonitoringFormLeadsAllenConsultingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringFormLeadsAllenConsulting
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class CamIndustrialMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CamIndustrialMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class CitizenCapitalMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitizenCapitalMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class MonitoringFormLeadsCitySecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringFormLeadsCitySecurity
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']

class MonitoringFormLeadsCTSSerializer(serializers.ModelSerializer):
        class Meta:
            model = MonitoringFormLeadsCTS
            fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                      'status']


class EmbassyLuxuryMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmbassyLuxuryMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']



class MonitoringFormLeadsGetARatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringFormLeadsGetARates
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']



class GlydeAppMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlydeAppMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class GoldenEastMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoldenEastMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']

class IbizMonFormSerializer(serializers.ModelSerializer):
        class Meta:
            model = IbizMonForm
            fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                      'status']


class IIBMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = IIBMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']



class MonitoringFormLeadsInfothinkLLCSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringFormLeadsInfothinkLLC
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class MonitoringFormLeadsInsalvageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringFormLeadsInsalvage
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class JJStudioMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = JJStudioMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']

class KalkiFashionsSerializer(serializers.ModelSerializer):
        class Meta:
            model = KalkiFashions
            fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                      'status']


class MonitoringFormLeadsLouisvilleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringFormLeadsLouisville
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']



class MonitoringFormLeadsMedicareSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringFormLeadsMedicare
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']

class MicroDistributingMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = MicroDistributingMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                      'status']

class MillenniumScientificMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = MillenniumScientificMonForm
        fields = ['associate_name', 'process', "overall_score", 'qa', 'team_lead', 'fatal', 'disput_status',
                      'status']

class MTCosmeticsMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = MTCosmeticsMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class NavigatorBioMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavigatorBioMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class OptimalStudentLoanMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptimalStudentLoanMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class ProtostarMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProtostarMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class MonitoringFormLeadsPSECUSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringFormLeadsPSECU
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class QBIQMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = QBIQMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class RestaurentSolMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurentSolMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class RitBrainMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = RitBrainMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class RoofWellMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoofWellMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class ScalaMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScalaMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class SolarCampaignMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolarCampaignMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class StandSpotMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = StandSpotMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class MonitoringFormLeadsSystem4Serializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringFormLeadsSystem4
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class MonitoringFormLeadsTentamusFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringFormLeadsTentamusFood
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class MonitoringFormLeadsTentamusPetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringFormLeadsTentamusPet
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class TerraceoLeadMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = TerraceoLeadMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class UpfrontOnlineLLCMonformSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpfrontOnlineLLCMonform
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class WTUMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = WTUMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class YesHealthMolinaMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = YesHealthMolinaMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class ZeroStressMarketingMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZeroStressMarketingMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class ABHindalcoOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ABHindalcoOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class AdityaBirlaOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdityaBirlaOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class AmerisaveoutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmerisaveoutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class BhagyaLakshmiOutboundSerializer(serializers.ModelSerializer):
    class Meta:
        model = BhagyaLakshmiOutbound
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class ClearViewOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClearViewOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class DanielWellingtonOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = DanielWellingtonOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class DigitalSwissGoldOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalSwissGoldOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class HealthyplusOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthyplusOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class MaxwellPropertiesOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaxwellPropertiesOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class MovementofInsuranceOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovementofInsuranceOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class SterlingStrategiesOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SterlingStrategiesOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class TonnCoaOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = TonnCoaOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class WitDigitalOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = WitDigitalOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class PosTechOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = PosTechOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class SchindlerMediaOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchindlerMediaOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class UPSOutboundMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = UPSOutboundMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']


class PickPackDeliveriesMonFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = PickPackDeliveriesMonForm
        fields = ['associate_name','process',"overall_score",'qa','team_lead','fatal','disput_status','status']

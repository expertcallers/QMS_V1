from rest_framework import serializers
from .models import *

class ChatMonitoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringFormLeadsAadhyaSolution
        fields = "__all__"
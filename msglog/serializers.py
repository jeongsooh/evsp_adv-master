from rest_framework import serializers
from msglog.models import Msglog

class MsglogSerializer(serializers.ModelSerializer):
  msg_content = serializers.JSONField()
  class Meta:
    model = Msglog
    fields = '__all__'
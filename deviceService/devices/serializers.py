from rest_framework import serializers
from .models import Device, User, Reading

class UserSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = User
    # fields = ('id','personal_account','sent_reading','serial_number')
    fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
  user = UserSerializer()
  class Meta:
    model = Device
    fields = ('id','personal_account','sent_reading','serial_number','user')
    
  #def get_user(self,obj):
  #  return str(obj.user.id)
  #def set_user(self,obj):
  #  return null
    
    
class ReadingSerializer(serializers.ModelSerializer):
  device = DeviceSerializer()
  class Meta:
    model = Reading
    fields = '__all__'
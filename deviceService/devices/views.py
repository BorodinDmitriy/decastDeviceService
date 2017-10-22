# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Device, User, Reading
from .serializers import DeviceSerializer, UserSerializer, ReadingSerializer

# Create your views here.

# List all devices or create a new one
# devices/
class DeviceList(APIView):
  
  def get(self, request):
    devices = Device.objects.all()
    serializer = DeviceSerializer(devices, many=True)
    return Response(serializer.data)
    
  def post(self,request):
    serializer = DeviceSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
# devices/<id>
class DeviceDetail(APIView):
  def get_object(self,id):
    try:
      return Device.objects.get(id=id)
    except Device.DoesNotExist:
      raise Http404

  def get(self,request,id):
    snippet = self.get_object(id)
    serializer = DeviceSerializer(snippet)
    return Response(serializer.data)
  
  def put(self,request,id):
    snippet = self.get_object(id)
    serializer = DeviceSerializer(snippet,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self,request,id):
    snippet = self.get_object(id)
    snippet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
# users/<id>/devices/
class DevicesByUserId(APIView):
  def get(self, request, id):
    user = User.objects.get(id=id)
    devices = user.device_set.all()
    serializer = DeviceSerializer(devices, many=True)
    return Response(serializer.data)
  
  def post(self,request,id):
    user = User.objects.get(id=id)
    
    if user:
      Device.objects.create(
	personal_account=request.data["personal_account"],
	serial_number=request.data["serial_number"],
	user=user
      )
      return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
  
  def put(self,request,id):
    user = User.objects.get(id=id)
    
    if user:
      Device.objects.save(
	personal_account=request.data["personal_account"],
	serial_number=request.data["serial_number"],
	user=user
      )
      return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)
  
# devices/<id>/readings
class DeviceReadings(APIView):
  def get(self, request, id):
    device = Device.objects.get(id=id)
    #devices = user.device_set.all()
    if request.GET.get('start_date') is None:
      readings = device.reading_set.all()
    else:
      readings = device.reading_set.get(date > request.data["start_date"])
    serializer = ReadingSerializer(readings, many=True)
    #print(id)
    return Response(serializer.data)
  
  def post(self,request,id):
    device = Device.objects.get(id=id)
    
    if device:
      Reading.objects.create(
	value=request.data["value"],
	device=device
      )
      return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

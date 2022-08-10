from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MsglogSerializer

from msglog.models import Msglog

import json

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
  api_urls = {
    'List':'/msglog-list/',
    'Detail View':'/msglog-detail/<str:pk>/',
    'Create':'/msglog-create/',
    'Update':'/msglog-update/<str:pk>/',
    'Delete':'/msglog-delete/<str:pk>/',
    }

  return Response(api_urls)

@api_view(['GET'])
def msglogList(request):
  msglogs = Msglog.objects.all()
  serializer = MsglogSerializer(msglogs, many=True)

  return Response(serializer.data)

@api_view(['GET'])
def msglogDetail(request, pk):
  msglogs = Msglog.objects.get(id=pk)
  serializer = MsglogSerializer(msglogs, many=False)

  return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def msglogCreate(request):

  try:
    data = json.loads(request.body)
  except:
    return Response({"message":"ERROR DETECT"})

  serializer = MsglogSerializer(data=data)
  # print(serializer)
  if serializer.is_valid():
    serializer.save()
    print("serializer is valid")
  else:
    print("serializer is NOT valid")
    print(serializer.errors)

  return Response(serializer.data)

@api_view(['POST'])
def msglogUpdate(request, pk):
  msglog = Msglog.objects.get(id=pk)
  serializer = MsglogSerializer(instance=msglog, data=request.data)
  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)

@api_view(['DELETE'])
def msglogDelete(request, pk):
  msglog = Msglog.objects.get(id=pk)
  msglog.delete()

  return Response("Item is successfully deleted!")

class MsglogList(ListView):
  model = Msglog
  template_name='msglog.html'
  context_object_name = 'msglogList'
  paginate_by = 10
  queryset = Msglog.objects.all()

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_id = self.request.session['user']
    context['loginuser'] = user_id
    return context

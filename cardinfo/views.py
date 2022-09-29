from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.views.generic.edit import FormView

import json
import uuid

from .models import Cardinfo
from .forms import CardinfoCreateRemoteForm

from ocpp16.client_gateway import get_cardtag
from ocpp16.consumers import Ocpp16Consumer
from ocpp16.models import Ocpp16

# Create your views here.

class CardinfoList(ListView):
  model = Cardinfo
  template_name='cardinfo.html'
  context_object_name = 'cardinfoList'
  paginate_by = 2
  queryset = Cardinfo.objects.all()


  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_id = self.request.session['user']
    context['loginuser'] = user_id
    return context

class CardinfoDetail(DetailView):
  template_name='cardinfo_detail.html'
  queryset = Cardinfo.objects.all()
  context_object_name = 'cardinfo'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_id = self.request.session['user']
    context['loginuser'] = user_id
    
    return context

class CardinfoCreateView(CreateView):
  model = Cardinfo
  template_name = 'cardinfo_register.html'
  fields = ['cardname', 'userid', 'cardtag', 'cardstatus']
  success_url = '/cardinfo'    

# class CardinfoCreateRemoteView(CreateView):
#   model = Cardinfo
#   template_name = 'cardinfo_register_remote.html'
#   fields = ['cardname', 'userid', 'cardtag', 'cardstatus']
#   success_url = '/cardinfo'   

class CardinfoCreateRemoteView(FormView):
  template_name = 'cardinfo_register_remote.html'
  form_class = CardinfoCreateRemoteForm
  success_url = '/cardinfo'

  def form_valid(self, form):
    cardname = form.data.get('cardname')
    userid = form.data.get('userid')
    cpnumber = form.data.get('cpnumber')
    cardinfo = Cardinfo(
      cardname = form.cardname,
      userid=form.data.get('userid'),
      cardstatus="처리중"
    )
    cardinfo.save()

    cardtag = get_cardtag(cpnumber, userid)

    return super().form_valid(form) 

class CardinfoDeleteView(DeleteView):
  model = Cardinfo
  template_name='cardinfo_confirm_delete.html'
  success_url = '/cardinfo'

class CardinfoUpdateView(UpdateView):
  model = Cardinfo
  template_name='cardinfo_update.html'
  fields = ['cardname', 'userid', 'cardtag', 'cardstatus']
  success_url = '/cardinfo'
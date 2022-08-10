from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Evcharger

# Create your views here.

class EvchargerList(ListView):
  model = Evcharger
  template_name='evcharger.html'
  context_object_name = 'evchargerList'
  paginate_by = 2
  queryset = Evcharger.objects.all()

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_id = self.request.session['user']
    context['loginuser'] = user_id
    return context

class EvchargerDetail(DetailView):
  template_name='evcharger_detail.html'
  queryset = Evcharger.objects.all()
  context_object_name = 'evcharger'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_id = self.request.session['user']
    context['loginuser'] = user_id
    
    return context

class EvchargerUpdateView(UpdateView):
  model = Evcharger
  template_name='evcharger_update.html'
  fields = ['cpnumber', 'cpname', 'cpstatus', 'address', 'partner_id']
  success_url = '/evcharger'

class EvchargerCreateView(CreateView):
  model = Evcharger
  template_name = 'evcharger_register.html'
  fields = ['cpnumber', 'cpname', 'cpstatus', 'address', 'partner_id']
  success_url = '/evcharger'

class EvchargerDeleteView(DeleteView):
    model = Evcharger
    template_name='evcharger_confirm_delete.html'
    success_url = '/evcharger'
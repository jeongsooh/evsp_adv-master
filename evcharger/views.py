from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.views.generic.edit import FormView
from .models import Evcharger
from .forms import EvchargerResetForm

from ocpp16.client_gateway import reset_evcharger, update_evcharger

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

class EvchargerResetView(FormView):
  template_name = 'evcharger_reset.html'
  form_class = EvchargerResetForm
  success_url = '/evcharger'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    reset_evcharger(cpnumber)

    return super().form_valid(form) 

class EvchargerFwupdateView(FormView):
  template_name = 'evcharger_fwupdate.html'
  form_class = EvchargerResetForm
  success_url = '/evcharger'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    update_evcharger(cpnumber)

    return super().form_valid(form) 


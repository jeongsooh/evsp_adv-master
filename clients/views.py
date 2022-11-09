from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.views.generic.edit import FormView
from .models import Clients
from .forms import ClientsResetForm

from ocpp16.client_gateway import ( reset_evcharger, update_evcharger, clearcache_evcharger, 
      remotestart_evcharger, remotestop_evcharger, unlock_connector, get_conf, set_conf)

# Create your views here.

class ClientsList(ListView):
  model = Clients
  template_name='clients.html'
  context_object_name = 'clientsList'
  paginate_by = 5
  queryset = Clients.objects.all()

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_id = self.request.session['user']
    context['loginuser'] = user_id
    return context

class ClientsDetail(DetailView):
  template_name='clients_detail.html'
  queryset = Clients.objects.all()
  context_object_name = 'clients'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_id = self.request.session['user']
    context['loginuser'] = user_id
    
    return context

class ClientsClearcacheView(FormView):
  template_name = 'clients_reset.html'
  form_class = ClientsResetForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    clearcache_evcharger(cpnumber)

    return super().form_valid(form) 

class RemoStartChargeView(FormView):
  template_name = 'clients_reset.html'
  form_class = ClientsResetForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    remotestart_evcharger(cpnumber)

    return super().form_valid(form) 

class RemoStopChargeView(FormView):
  template_name = 'clients_reset.html'
  form_class = ClientsResetForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    remotestop_evcharger(cpnumber)

    return super().form_valid(form) 

class UnlockConnView(FormView):
  template_name = 'clients_reset.html'
  form_class = ClientsResetForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    unlock_connector(cpnumber)

    return super().form_valid(form) 

class GetConfView(FormView):
  template_name = 'clients_reset.html'
  form_class = ClientsResetForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    get_conf(cpnumber)

    return super().form_valid(form) 

class SetConfView(FormView):
  template_name = 'clients_reset.html'
  form_class = ClientsResetForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    set_conf(cpnumber)

    return super().form_valid(form) 


# class ClientsUpdateView(UpdateView):
#   model = Clients
#   template_name='clients_update.html'
#   fields = ['cpnumber', 'cpname', 'cpstatus', 'address', 'partner_id']
#   success_url = '/clients'

# class ClientsCreateView(CreateView):
#   model = Clients
#   template_name = 'clients_register.html'
#   fields = ['cpnumber', 'cpname', 'cpstatus', 'address', 'partner_id']
#   success_url = '/clients'

# class ClientsDeleteView(DeleteView):
#     model = Clients
#     template_name='clients_confirm_delete.html'
#     success_url = '/clients'

class ClientsResetView(FormView):
  template_name = 'clients_reset.html'
  form_class = ClientsResetForm
  success_url = '/clients'

  def form_valid(self, form):
    cpnumber = form.data.get('cpnumber')
    reset_evcharger(cpnumber)

    return super().form_valid(form) 

# class ClientsFwupdateView(FormView):
#   template_name = 'clients_fwupdate.html'
#   form_class = ClientsResetForm
#   success_url = '/clients'

#   def form_valid(self, form):
#     cpnumber = form.data.get('cpnumber')
#     update_clients(cpnumber)

#     return super().form_valid(form) 



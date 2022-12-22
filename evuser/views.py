from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from evuser.models import Evuser
from .forms import RegisterForm, LoginForm

# Create your views here.

def index(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      request.session['user'] = form.data.get('userid')
      return redirect('/evuser')
  else:
    form = LoginForm()
  return render(request, 'index.html', {'form': form})

def test(request):

  return render(request, 'test.html')


class EvuserCreateView(CreateView):
  model = Evuser
  template_name = 'evuser_register.html'
  fields = ['userid', 'password', 'name', 'email', 'phone', 'address', 'category', 'status', 'level']
  success_url = '/evuser'

class EvuserDeleteView(DeleteView):
    model = Evuser
    template_name='evuser_confirm_delete.html'
    success_url = '/evuser'

class EvuserUpdateView(UpdateView):
  model = Evuser
  template_name='evuser_update.html'
  fields = [ 'userid', 'name', 'phone']
  success_url = '/evuser'

class EvuserList(ListView):
  model = Evuser
  template_name='evuser.html'
  context_object_name = 'evuserList'
  paginate_by = 2
  # queryset = Evuser.objects.all()

  def get_queryset(self):
    queryset = Evuser.objects.all()
    query = self.request.GET.get("q", None)
    if query is not None:
      queryset = queryset.filter(
        Q(userid__icontains=query) |
        Q(name__icontains=query) |
        Q(phone__icontains=query)
      )
    return queryset

  def get_context_data(self, **kwargs):
    context = super(EvuserList, self).get_context_data(**kwargs)
    user_id = self.request.session['user']
    context['loginuser'] = user_id
    return context

class EvuserDetail(DetailView):
  template_name='evuser_detail.html'
  queryset = Evuser.objects.all()
  context_object_name = 'evuser'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_id = self.request.session['user']
    context['loginuser'] = user_id
    
    return context

class LoginView(FormView):
  template_name = 'login.html'
  form_class = LoginForm
  success_url = '/'

  def form_valid(self, form):
    self.request.session['user'] = form.user_id

    return super().form_valid(form)


def logout(request):
  if 'user' in request.session:
    del(request.session['user'])

  return redirect('/')




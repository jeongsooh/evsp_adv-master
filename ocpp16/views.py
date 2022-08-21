from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView
from django.views.generic import ListView
import uuid

from .models import Ocpp16
from .forms import MessageForm
from .central_system import ocpp_request

# Create your views here.
def index(request):
  if request.method == 'POST':
    form = MessageForm(request.POST)
    if form.is_valid():
      ocpp_req = {
        "msg_direction" : 2,
        "connection_id" : str(uuid.uuid4()),
        "msg_name": form.data.get('msg_name'),
        "msg_content": form.data.get('msg_content'),
        'cpnumber': form.data.get('cpnumber'),
      }
      ocpp_conf = ocpp_request(ocpp_req)
      # print('Request.session: %s' % dir(request.session))
      # request.session['user'] = form.data.get('userid')
      return render(request, 'test_index.html', {'form': form, 'conf': ocpp_conf})
      # return redirect('/evuser')
  else:
    form = MessageForm()
  return render(request, 'test_index.html', {'form': form})

class Ocpp16List(ListView):
  model = Ocpp16
  template_name='ocpp16.html'
  context_object_name = 'ocpp16List'
  paginate_by = 10
  queryset = Ocpp16.objects.all()

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_id = self.request.session['user']
    context['loginuser'] = user_id
    return context

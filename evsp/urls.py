from django.contrib import admin
from django.urls import path, include

from evuser.views import (
    index, EvuserUpdateView,
    EvuserList, logout, EvuserDetail, EvuserCreateView, EvuserDeleteView, test
    )
from charginginfo.views import (
    CharginginfoList, CharginginfoCreateView, CharginginfoDetail,
    CharginginfoUpdateView
    )   
from cardinfo.views import (
    CardinfoList, CardinfoCreateView, CardinfoDeleteView, CardinfoUpdateView,
    CardinfoDetail, CardinfoCreateRemoteView
    )
from evcharger.views import (
    EvchargerList, EvchargerDetail, EvchargerUpdateView, EvchargerFwupdateView,
    EvchargerCreateView, EvchargerDeleteView, EvchargerResetView
    )
from msglog.views import (
    MsglogList,
)
from variables.views import (
    VariablesList, VariablesDetail, VariablesUpdateView, 
    VariablesCreateView, VariablesDeleteView
)

from evsp import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('test/', test),
    path('update/<int:pk>/', EvuserUpdateView.as_view(), name='update'),
    path('evuser/', EvuserList.as_view()),
    # path('evuser/filtered/', EvuserFilteredList.as_view()),
    path('evuser/<int:pk>/delete/', EvuserDeleteView.as_view()),
    path('evuser/<int:pk>/', EvuserDetail.as_view()),
    path('evuser/register/', EvuserCreateView.as_view()),
    path('charginginfo/', CharginginfoList.as_view()),
    path('charginginfo/<int:pk>/', CharginginfoDetail.as_view()),
    path('charginginfo/register/', CharginginfoCreateView.as_view()),
    path('charginginfoupdate/<int:pk>/', CharginginfoUpdateView.as_view(), name='charginginfoupdate'),
    path('cardinfo/', CardinfoList.as_view()),
    path('cardinfo/<int:pk>/', CardinfoDetail.as_view()),
    path('cardinfo/register/', CardinfoCreateView.as_view()),
    path('cardinfo/registerremote/', CardinfoCreateRemoteView.as_view()),
    path('cardinfo/<int:pk>/delete/', CardinfoDeleteView.as_view()),
    path('cardupdate/<int:pk>/', CardinfoUpdateView.as_view(), name='cardupdate'),
    path('evcharger/', EvchargerList.as_view()),
    path('evcharger/<int:pk>/delete/', EvchargerDeleteView.as_view()),
    path('evcharger/<int:pk>/reset/', EvchargerResetView.as_view()),
    path('evcharger/<int:pk>/', EvchargerDetail.as_view()),
    path('evcharger/register/', EvchargerCreateView.as_view()),
    path('evcharger/fwupdate/', EvchargerFwupdateView.as_view()),
    path('cpupdate/<int:pk>/', EvchargerUpdateView.as_view(), name='cpupdate'),
    path('msglog/', MsglogList.as_view()),
    path('variables/', VariablesList.as_view()),
    path('variables/<int:pk>/delete/', VariablesDeleteView.as_view()),
    path('variables/<int:pk>/', VariablesDetail.as_view()),
    path('variables/register/', VariablesCreateView.as_view()),
    path('variablesupdate/<int:pk>/', VariablesUpdateView.as_view(), name='variablesupdate'),
    path('logout/', logout),
]

urlpatterns += [
    path('ocpp16/', include('ocpp16.urls')),
    path('clients/', include('clients.urls')),
]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [path('__debug__', include('debug_toolbar.urls'))] 
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from django.views.generic import TemplateView
from .views import SyslogInputList, SyslogInputDetail, SyslogInputDelete, SyslogInputCreate, SyslogInputUpdate, SyslogInputStatus, status

urlpatterns = [
    path('list/', SyslogInputList.as_view(), name='in_syslog_list'),
    path('create/', SyslogInputCreate.as_view(), name='in_syslog_create'),
    path('update/<int:pk>', SyslogInputUpdate.as_view(), name='in_syslog_update'),
    path('status/<int:pk> <int:status>', status, name='in_syslog_status'),
    path('delete/<int:pk>', SyslogInputDelete.as_view(), name='in_syslog_delete'),
    path('detail/<int:pk>', SyslogInputDetail.as_view(), name='in_syslog_detail'),
]

from django.urls import path
from django.views.generic import TemplateView
from .views import SplunkHECInputList, SplunkHECInputDetail, SplunkHECInputDelete, SplunkHECInputCreate, SplunkHECInputUpdate, status

urlpatterns = [
    path('list/', SplunkHECInputList.as_view(), name='in_splunk_hec_list'),
    path('create/', SplunkHECInputCreate.as_view(), name='in_splunk_hec_create'),
    path('update/<int:pk>', SplunkHECInputUpdate.as_view(), name='in_splunk_hec_update'),
    path('status/<int:pk> <int:status>', status, name='in_splunk_hec_status'),
    path('delete/<int:pk>', SplunkHECInputDelete.as_view(), name='in_splunk_hec_delete'),
    path('detail/<int:pk>', SplunkHECInputDetail.as_view(), name='in_splunk_hec_detail'),
]

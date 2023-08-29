from django.urls import path
from django.views.generic import TemplateView
from .views import KafkaOutputList, KafkaOutputDetail, KafkaOutputDelete, KafkaOutputCreate, KafkaOutputUpdate, status

urlpatterns = [
    path('list/', KafkaOutputList.as_view(), name='out_kafka_list'),
    path('create/', KafkaOutputCreate.as_view(), name='out_kafka_create'),
    path('update/<int:pk>', KafkaOutputUpdate.as_view(), name='out_kafka_update'),
    path('status/<int:pk> <int:status>', status, name='out_kafka_status'),
    path('delete/<int:pk>', KafkaOutputDelete.as_view(), name='out_kafka_delete'),
    path('detail/<int:pk>', KafkaOutputDetail.as_view(), name='out_kafka_detail'),
]

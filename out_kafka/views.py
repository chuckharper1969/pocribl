from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import KafkaOutput
from .forms import KafkaOutputCreateForm, KafkaOutputUpdateForm
from datetime import datetime

class KafkaOutputCreate(CreateView):
    form_class = KafkaOutputCreateForm
    #model = SyslogInput
    #fields = ['input_id', 'udp_port', 'tcp_port']
    template_name = "out_kafka_create.html"
    success_url = reverse_lazy('out_kafka_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.status = 0
        form.instance.message = "Created output"
        form.instance.modified_at = datetime.now()
        messages.success(self.request, "The output was created successfully.")
        return super(KafkaOutputCreate,self).form_valid(form)

class KafkaOutputList(ListView):
    model = KafkaOutput
    template_name = "out_kafka_list.html"

class KafkaOutputUpdate(UpdateView):
    form_class = KafkaOutputUpdateForm
    model = KafkaOutput
    template_name = "out_kafka_update.html"
    #fields = ['input_id', 'udp_port', 'tcp_port']
    success_url = reverse_lazy('out_kafka_list')

    def form_valid(self, form):
        #form.instance.input_id = self.request.input_id
        form.instance.modified_at = datetime.now()
        messages.success(self.request, "The output was updated successfully.")
        return super(KafkaOutputUpdate,self).form_valid(form)

class KafkaOutputDetail(DetailView):
    model = KafkaOutput
    template_name = "out_kafka_detail.html"

class KafkaOutputDelete(DeleteView):
    model = KafkaOutput
    template_name = "out_kafka_delete.html"
    success_url = reverse_lazy('out_kafka_list')

class KafkaOutputStatus(UpdateView):
    model = KafkaOutput
    template_name = "out_kafka_create.html"

def status(request, pk, status):
    if request.user.is_authenticated:
        record = KafkaOutput.objects.get(id=pk)
        if record.status != status:
            record.status = status
            record.message = f" Status changed to {record.status}"
            record.save()
            messages.success(request, f"Input  has been {'enabled' if record.status == 0 else 'disabled'}...")
        return redirect("out_kafka_list")
    else:
        messages.success(request, "You must be logged in to view that page...")
        return redirect("login")
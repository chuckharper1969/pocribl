from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import SplunkHECInput
from .forms import SplunkHECInputCreateForm, SplunkHECInputUpdateForm
from datetime import datetime

class SplunkHECInputCreate(CreateView):
    form_class = SplunkHECInputCreateForm
    #model = SplunkHECInput
    #fields = ['input_id', 'udp_port', 'tcp_port']
    template_name = "in_splunk_hec_create.html"
    success_url = reverse_lazy('in_splunk_hec_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.status = 0
        form.instance.message = "Created input"
        form.instance.modified_at = datetime.now()
        messages.success(self.request, "The input was created successfully.")
        return super(SplunkHECInputCreate,self).form_valid(form)

class SplunkHECInputList(ListView):
    model = SplunkHECInput
    template_name = "in_splunk_hec_list.html"

class SplunkHECInputUpdate(UpdateView):
    form_class = SplunkHECInputUpdateForm
    model = SplunkHECInput
    template_name = "in_splunk_hec_update.html"
    #fields = ['input_id', 'udp_port', 'tcp_port']
    success_url = reverse_lazy('in_splunk_hec_list')

    def form_valid(self, form):
        #form.instance.input_id = self.request.input_id
        form.instance.modified_at = datetime.now()
        messages.success(self.request, "The task was updated successfully.")
        return super(SplunkHECInputUpdate,self).form_valid(form)

class SplunkHECInputDetail(DetailView):
    model = SplunkHECInput
    template_name = "in_splunk_hec_detail.html"

class SplunkHECInputDelete(DeleteView):
    model = SplunkHECInput
    template_name = "in_splunk_hec_delete.html"
    success_url = reverse_lazy('in_splunk_hec_list')

class SplunkHECInputStatus(UpdateView):
    model = SplunkHECInput
    template_name = "in_splunk_hec_create.html"

def status(request, pk, status):
    if request.user.is_authenticated:
        record = SplunkHECInput.objects.get(id=pk)
        if record.status != status:
            record.status = status
            record.message = f" Status changed to {record.status}"
            record.save()
            messages.success(request, f"Input  has been {'enabled' if record.status == 0 else 'disabled'}...")
        return redirect("in_splunk_hec_list")
    else:
        messages.success(request, "You must be logged in to view that page...")
        return redirect("login")
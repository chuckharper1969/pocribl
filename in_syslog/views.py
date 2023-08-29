from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import SyslogInput
from .forms import SyslogInputCreateForm, SyslogInputUpdateForm
from datetime import datetime

class SyslogInputCreate(CreateView):
    form_class = SyslogInputCreateForm
    #model = SyslogInput
    #fields = ['input_id', 'udp_port', 'tcp_port']
    template_name = "in_syslog_create.html"
    success_url = reverse_lazy('in_syslog_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.status = 0
        form.instance.message = "Created input"
        form.instance.modified_at = datetime.now()
        messages.success(self.request, "The input was created successfully.")
        return super(SyslogInputCreate,self).form_valid(form)

class SyslogInputList(ListView):
    model = SyslogInput
    template_name = "in_syslog_list.html"

class SyslogInputUpdate(UpdateView):
    form_class = SyslogInputUpdateForm
    model = SyslogInput
    template_name = "in_syslog_update.html"
    #fields = ['input_id', 'udp_port', 'tcp_port']
    success_url = reverse_lazy('in_syslog_list')

    def form_valid(self, form):
        #form.instance.input_id = self.request.input_id
        form.instance.modified_at = datetime.now()
        messages.success(self.request, "The task was updated successfully.")
        return super(SyslogInputUpdate,self).form_valid(form)

class SyslogInputDetail(DetailView):
    model = SyslogInput
    template_name = "in_syslog_detail.html"

class SyslogInputDelete(DeleteView):
    model = SyslogInput
    template_name = "in_syslog_delete.html"
    success_url = reverse_lazy('in_syslog_list')

class SyslogInputStatus(UpdateView):
    model = SyslogInput
    template_name = "in_syslog_create.html"

def status(request, pk, status):
    if request.user.is_authenticated:
        record = SyslogInput.objects.get(id=pk)
        if record.status != status:
            record.status = status
            record.message = f" Status changed to {record.status}"
            record.save()
            messages.success(request, f"Input  has been {'enabled' if record.status == 0 else 'disabled'}...")
        return redirect("in_syslog_list")
    else:
        messages.success(request, "You must be logged in to view that page...")
        return redirect("login")
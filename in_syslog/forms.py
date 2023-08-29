from django import forms
from .models import SyslogInput

class SyslogInputCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SyslogInputCreateForm, self).__init__(*args, **kwargs)

        self.fields['input_id'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['udp_port'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['tcp_port'].widget.attrs = {
            'class': 'form-control'
        }
    
    class Meta:
        model = SyslogInput
        fields = ['input_id', 'udp_port', 'tcp_port']

class SyslogInputUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SyslogInputUpdateForm, self).__init__(*args, **kwargs)

        self.fields['udp_port'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['tcp_port'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['input_id'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['input_id'].disabled = True
    
    class Meta:
        model = SyslogInput
        fields = ['input_id', 'udp_port', 'tcp_port']

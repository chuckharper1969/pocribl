from django import forms
from .models import SplunkHECInput

class SplunkHECInputCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SplunkHECInputCreateForm, self).__init__(*args, **kwargs)

        self.fields['token'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['description'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['index'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['sourcetype'].widget.attrs = {
            'class': 'form-control'
        }
    
    class Meta:
        model = SplunkHECInput
        fields = ['token', 'description', 'index', 'sourcetype']

class SplunkHECInputUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SplunkHECInputUpdateForm, self).__init__(*args, **kwargs)

        self.fields['token'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['description'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['index'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['sourcetype'].widget.attrs = {
            'class': 'form-control'
        }
    
    class Meta:
        model = SplunkHECInput
        fields = ['token', 'description', 'index', 'sourcetype']

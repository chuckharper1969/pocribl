from django import forms
from .models import KafkaOutput

class KafkaOutputCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(KafkaOutputCreateForm, self).__init__(*args, **kwargs)

        self.fields['output_id'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['broker'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['topic'].widget.attrs = {
            'class': 'form-control'
        }
    
    class Meta:
        model = KafkaOutput
        fields = ['output_id', 'broker', 'topic']

class KafkaOutputUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(KafkaOutputUpdateForm, self).__init__(*args, **kwargs)

        self.fields['broker'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['topic'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['output_id'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['output_id'].disabled = True
    
    class Meta:
        model = KafkaOutput
        fields = ['output_id', 'broker', 'topic']

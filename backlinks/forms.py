from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from .models import Backlinks

class YeniForm(forms.ModelForm):
    class Meta:
        model = Backlinks
        fields = ['link','keyword','source','created_date', 'end_date','description','author']
        widgets = {
            'created_date': DatePickerInput(format='%Y-%m-%d %H:%M:%S'), # default date-format %m/%d/%Y will be used
            'end_date': DatePickerInput(format='%Y-%m-%d %H:%M:%S'), # specify date-frmat
        }

    def clean(self, *args, **kwargs):
        cleaned_data = super(YeniForm, self).clean(*args,**kwargs)
        return cleaned_data

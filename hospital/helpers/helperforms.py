from ..models import PatientDetails,HospitalDetails
from django.forms import ModelForm

class PatientDetailsForm(ModelForm):
    class Meta:
        model = PatientDetails
        exclude = ['patient']

    def __init__(self, *args, **kwargs):
        super(PatientDetailsForm, self).__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class HospitalDetailForm(ModelForm):
    class Meta:
        model = HospitalDetails
        exclude = ["hospital",'ratings','total_ratings',"speech_ratings"]

        def __init__(self, *args, **kwargs):
            super(HospitalDetailForm, self).__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })

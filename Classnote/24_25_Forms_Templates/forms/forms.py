# --------------- Form -------------- #
from django import forms

class BasicForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    number = forms.IntegerField(required=False)

# --------------- ModelForm -------------- #
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        # fields = '__all__'
        # fields = ('first_name', 'last_name')
        exclude = []
        labels = {
            'first_name': 'Adınız',
            'last_name': 'Soyadınız',
            'number': 'Numara',
            'image': 'Resim'
        }

from django.forms import ModelForm
from django import forms
from .models import *

class FormPelelangan(ModelForm):
    class Meta:
        model = pelelangan
        fields = '__all__'

        widgets = {
            'nama'    : forms.TextInput({'class':'form-control', 'placeholder':'Nama Pelelangan', 'required':'required'}),
            'lintang' : forms.NumberInput({'class':'form-control', 'placeholder':'Garis Lintang', 'required':'required', 'step' : '0.0000000001', 'type' : 'number',}),
            'bujur'   : forms.NumberInput({'class':'form-control', 'placeholder':'Garis Bujur', 'required':'required', 'step' : '0.0000000001', 'type' : 'number',}),
        }


class FormIkan(ModelForm):
    class Meta:
        model = Ikan
        fields = '__all__'

        widgets = {
            'nama_Ikan'  : forms.TextInput({'class':'form-control', 'placeholder':'Nama Pelelangan', 'required':'required'}),
            'harga'      : forms.TextInput({'class':'form-control', 'placeholder':'Harga Ikan', 'required':'required'}),
            'gambar'     : forms.FileInput({'class':'form-control', 'required':'required'}),
        }
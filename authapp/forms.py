from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import ShopUser


# class MyForm(forms.ModelForm):
#     model = Product

class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')
        #fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

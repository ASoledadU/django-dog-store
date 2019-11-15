from django import forms


class NewDogTagForm(forms.Form):
    owner_name = forms.CharField()
    dog_name = forms.CharField()
    dog_birthday = forms.DateField()
    owner_phone = forms.CharField()

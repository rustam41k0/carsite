from django import forms


class CartAddCarForm(forms.Form):
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)


class UserContactForm(forms.Form):
    name = forms.CharField(label='Your Name', required=True)
    email = forms.EmailField(label='Email', required=True)

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Nombre y apellido',
            'class': 'form-control form__input',
            'id': 'nombre'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'ejemplo@gmail.com',
            'class': 'form-control form__input',
            'id': 'email'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': '0/1000',
            'class': 'form-control form__textarea',
            'id': 'mensaje'
        })
    )

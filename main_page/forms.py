from django import forms
from .models import UserReservation, Contact




class UserReservationForm(forms.ModelForm):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={
                               'type': "text",
                               'name': 'name',
                               'class': 'form-control',
                               'id': 'name',
                               'placeholder': 'Your Name'
                            }))

    email = forms.CharField(max_length=50,
                            widget=forms.EmailInput(attrs={
                                    'type': 'email',
                                    'class': 'form-control',
                                    'name': 'email',
                                    'id': 'email',
                                    'placeholder': 'Your Email',
                            }))

    phone = forms.CharField(max_length=15,
                            widget=forms.TextInput(attrs={
                                'type': 'tel',
                                'class': 'form-control',
                                'name': 'phone',
                                'id': 'phone',
                                'placeholder': 'Your Phone',
                            }))
    message = forms.CharField(max_length=15,
                              widget=forms.Textarea(attrs={
                                'class': 'form-control',
                                'name': 'message',
                                'rows': '5',
                                'placeholder': 'Message (Optional)'
                            }))






    class Meta:
        model = UserReservation
        fields = ('name', 'phone', 'email', 'message')



class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={
                               'type': "text",
                               'name': 'name',
                               'class': 'form-control',
                               'id': 'name',
                               'placeholder': 'Your Name',
                           }))

    email = forms.CharField(max_length=50,
                            widget=forms.EmailInput(attrs={
                                    'type': 'email',
                                    'class': 'form-control',
                                    'name': 'email',
                                    'id': 'email',
                                    'placeholder': 'Your Email',
                            }))
    message = forms.CharField(max_length=15,
                              widget=forms.Textarea(attrs={
                                'class': 'form-control',
                                'name': 'message',
                                'rows': '5',
                                'placeholder': 'Message (Optional)',
                            }))
    subject = forms.CharField(max_length=15,
                              widget=forms.Textarea(attrs={
                                'type': 'text',
                                'class': 'form-control',
                                'name': 'subject',
                                'id': 'subject',
                                'placeholder': 'Subject',
                            }))

    class Meta:
        model = Contact
        fields = ('name', 'subject', 'email', 'message')
from django import forms
from django.db import models
from .models import Member, Country, City
from functools import partial

DateInput = partial(
    forms.DateInput,
    {'class': 'datepicker'},
    format=('%d/%m/%Y')
)

class CreateNewMemberForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = (
            'first_name',
            'last_name',
            'country',
            'city',
            'gender',
            'birth_date',
            'phone_number',
            'email',
            'notes',
            'status',
            'profile_image'
        )
    
    def __init__(self, *args, **kwargs):
        super(CreateNewMemberForm, self).__init__(*args, **kwargs)

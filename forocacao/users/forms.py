# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _

from django_countries import countries

from forocacao.app.models import Event, Profession

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label=_('First name'))
    last_name = forms.CharField(max_length=30, label=_('Last name'))
    document = forms.CharField(max_length=30, label=_('Document ID'))
    #country = forms.CountryField(verbose_name=_('Country'), blank=True, null=True)
    country = forms.ChoiceField(countries, label=_('Pais'))
    AGE_CHOICES = (('A', '<=29'), ('B', '30-64'), ('C', '>=65'))
    age = forms.ChoiceField(choices=AGE_CHOICES, label=_('Edad'))
    SEX_CHOICES = (('M',_('Masculino')), ('F', _('Femenino')))
    sex = forms.ChoiceField(choices=SEX_CHOICES, label=_('Sexo'))
    phone = forms.CharField(max_length=30, label=_('Telephone'))
    organization = forms.CharField(max_length=30, label=_('Organization'))
    professions = Profession.objects.all()
    profession = forms.ModelChoiceField(queryset=professions, label=_('Position'), required=False)
    position = forms.CharField(max_length=30, label=_('Otro'), required=False)

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'autofocus': 'autofocus'})
        self.keyOrder = ['firs_name', 'last_name', 'country', 'document', 'phone', 'email', 'password']

    def signup(self, request, user):
        user.username = self.cleaned_data['email'][:30]
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.organization = self.cleaned_data['organization']
        user.position = self.cleaned_data['position']
        user.profession = self.cleaned_data['profession']
        user.phone = self.cleaned_data['phone']
        user.country = self.cleaned_data['country']
        user.age = self.cleaned_data['age']
        user.sex = self.cleaned_data['sex']
        user.document = self.cleaned_data['document']
        event = Event.objects.filter(status='frontpage')[0]
        if event:
            user.event = event
        user.save()

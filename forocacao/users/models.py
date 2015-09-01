# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from filer.fields.image import FilerImageField
from django_countries.fields import CountryField
from model_utils import Choices
from smart_selects.db_fields import ChainedForeignKey


@python_2_unicode_compatible
class User(AbstractUser):

    #name = models.CharField(_("Name of User"), blank=True, max_length=255)
    event = models.ForeignKey('app.Event', null=True, verbose_name=_('Event'))
    profession = models.ForeignKey('app.Profession', null=True, verbose_name=_('Profession'))
    phone = models.CharField(max_length=50, verbose_name=_('Phone'))
    extra = models.BooleanField(verbose_name=_('Extra Activity'), default=False)
    country = CountryField(verbose_name=_('Country'))
    nationality = CountryField(verbose_name=_('Nationality'))
    sponsored = models.BooleanField(verbose_name=_('Soponsored'), default=False)
    # FIXME: sponsor always == 3?
    sponsor = models.ForeignKey('User', limit_choices_to = {'type': 3}, null=True, blank=True, verbose_name=_('Sponsor'))
    document = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('Document'))
    organization = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('Organization'))
    position = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('Position'))
    #TYPE = Choices(('regular',_('Regular')), ('speaker', _('Speaker')), ('sponsor', _('Sponsor')), ('organizer',_('Oganizer')), ('special',_('Special')))
    #type = models.ForeignKey('app.AttendeeType', default='regular', verbose_name=_('Type'))
    type = models.ForeignKey('app.AttendeeType', null=True, verbose_name=_('Type'))
    #payment_method = models.ForeignKey('app.PaymentMethod', null=True, verbose_name=_('Payment Method'))
    photo = models.ImageField(null=True, blank=True, verbose_name=_('Photo'))
    text = models.TextField(blank=True,
                                 verbose_name=_('Biography'),
                                 help_text='Try and enter few some more lines')
    activities = models.ManyToManyField('app.Activity', blank=True, verbose_name=_('Activity'))

    class Meta:
        verbose_name = _("Attendee")
        verbose_name_plural = _("Attendees")
        permissions = (
            ("can_print_badge", "Can print badge"),
            ("can_approve_participant", "Can approve participant"),
        )

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

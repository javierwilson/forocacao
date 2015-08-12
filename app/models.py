from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _

from filer.fields.image import FilerImageField
from django_countries.fields import CountryField

class Conference(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField()
    text = models.TextField(blank=True,
                                 verbose_name=_('Conference description'),
                                 help_text='Try and enter few some more lines')
    logo = FilerImageField(blank=True, null=True, related_name='conference_logos')
    image = FilerImageField(blank=True, null=True, related_name='conference_images')
    image_footer = FilerImageField(blank=True, null=True, related_name='conference_footers')
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = _("Concerence")
        verbose_name_plural = _("Conferences")

    def __unicode__(self):
        return self.name

class Activity(models.Model):
    conference = models.ForeignKey('Conference')
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    text = models.TextField(blank=True,
                                 verbose_name=_('Activity description'),
                                 help_text='Try and enter few some more lines')
    image = FilerImageField(blank=True, null=True, related_name='activity_images')
    image_footer = FilerImageField(blank=True, null=True, related_name='activity_footers')
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = _("Activity")
        verbose_name_plural = _("Activities")

    def __unicode__(self):
        return self.name

class Profession(models.Model):
    conference = models.ForeignKey('Conference')
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    text = models.TextField(blank=True,
                                 verbose_name=_('Profession description'),
                                 help_text='Try and enter few some more lines')

    class Meta:
        verbose_name = _("Profession")
        verbose_name_plural = _("Professions")

    def __unicode__(self):
        return self.name

class AttendeeType(models.Model):
    conference = models.ForeignKey('Conference')
    name = models.CharField(max_length=200)
    is_speaker = models.BooleanField()

    class Meta:
        verbose_name = _("Type")
        verbose_name_plural = _("Types")

    def __unicode__(self):
        return self.name

class Attendee(models.Model):
    conference = models.ForeignKey('Conference')
    profession = models.ForeignKey('Profession')
    phone = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    country = CountryField(null=True, blank=True)
    document = models.CharField(max_length=50, null=True, blank=True)
    attendee_type = models.ForeignKey('AttendeeType', null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    photo = models.ImageField(null=True, blank=True)
    text = models.TextField(blank=True,
                                 verbose_name=_('Biography'),
                                 help_text='Try and enter few some more lines')
    activities = models.ManyToManyField('Activity', null=True)

    class Meta:
        verbose_name = _("Attendee")
        verbose_name_plural = _("Attendee")

    def __unicode__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)
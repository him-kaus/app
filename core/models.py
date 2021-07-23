import datetime
from django.db import models
from django.contrib.auth.models import User
from .choices import SLOT_STATUS_CHOICES, MEETING_STATUS_CHOICES, ALGO_TRADING_PLATFORM, TIME_CHOICES, SEGMENT_CHOICES
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Day(models.Model):
    Name = models.CharField(max_length=10, default='Monday')

    def __str__(self):
        return f' {self.Name} '

    class Meta:
        verbose_name = 'Day'
        verbose_name_plural = 'Days'


class Slot(models.Model):
    Day = models.ForeignKey(Day, on_delete=models.CASCADE)
    From = models.TimeField(choices=TIME_CHOICES)
    To = models.TimeField(choices=TIME_CHOICES)
    Status = models.CharField(max_length=15, choices=SLOT_STATUS_CHOICES)

    def __str__(self):
        return f'{self.From} - {self.To}'

    class Meta:
        verbose_name = 'Slot'
        verbose_name_plural = 'Slots'


# class Language(models.Model):
#     Name = models.CharField(max_length=128, null=True, blank=True)
#
#     def __str__(self):
#         return f'{self.Name}'
#
#     class Meta:
#         verbose_name = 'Language'
#         verbose_name_plural = 'Languages'


class Meeting(models.Model):
    Slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    Date = models.DateField(null=True, blank=True)

    Client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    Link = models.CharField(max_length=512, null=True, blank=True, verbose_name='Meeting Link')
    Status = models.CharField(max_length=20, choices=MEETING_STATUS_CHOICES, default='Requested')
    PaymentLink = models.CharField(max_length=512, null=True, blank=True)

    # LanguageChoice = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True)
    # LanguageInput = models.CharField(max_length=128, default=' ', null=True, blank=True)

    AlgoTradingPlatform = models.CharField(max_length=128, choices=ALGO_TRADING_PLATFORM, default='Python', null=True,
                                           blank=True)
    Comment = models.TextField(default=' ')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateField(auto_now=True, editable=False)

    def __str__(self):
        return f'{self.Slot} {self.Client} {self.Status}'

    class Meta:
        verbose_name = 'Meeting'
        verbose_name_plural = 'Meetings'


class CustomerQueries(models.Model):
    Name = models.CharField(max_length=256, default='Name')
    Email = models.EmailField()
    Subject = models.CharField(max_length=1024, default='Subject')
    Message = models.TextField(max_length=6000)

    def __str__(self):
        return f'{self.Name} {self.Email} {self.Subject}'

    class Meta:
        verbose_name = 'Customer Query'
        verbose_name_plural = 'Customer Queries'


class Shop(models.Model):
    UploaderName = models.CharField(max_length=126)
    UploaderEmail = models.EmailField()
    UploaderPhone = PhoneNumberField()
    StrategyName = models.CharField(max_length=300)
    CapitalRequired = models.CharField(max_length=300)
    Segment = models.CharField(max_length=300, choices=SEGMENT_CHOICES)
    Price = models.PositiveIntegerField()
    Image = models.FileField(upload_to='Images/')
    Youtube = models.CharField(max_length=300, null=True, blank=True)
    Website = models.CharField(max_length=300, null=True, blank=True)
    Tradingview = models.CharField(max_length=300, null=True, blank=True)
    Telegram = models.CharField(max_length=300, null=True, blank=True)

    Platform = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f'{self.UploaderName} {self.StrategyName} {self.Price}'

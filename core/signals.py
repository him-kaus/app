from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Meeting


@receiver(post_save, sender=Meeting)
def meeting_booked(sender, instance, created, **kwargs):
    if created == False and instance.Status == 'Booked':
        send_mail(
            'Meeting Booked',
            f'Hello {instance.Client.username},\nyour meeting on {instance.Date} at {instance.Slot.From} - '
            f'{instance.Slot.To} has been booked.\nhere is you meeting link {instance.Link}, it has also been updated on your QuantChef Dashboard'
            f'\nregards',
            'contact@quantchef.in',
            [f'{instance.Client.email}'],
            fail_silently=False,
        )
        print('meeting post save signal working as intended')




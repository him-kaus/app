from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Day, Slot, Meeting, Shop
from .forms import MeetingForm, QueriesForm, ShopForm

import calendar
from datetime import datetime


# Create your views here.
def landing(request):
    if request.method == 'POST':
        form = QueriesForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = QueriesForm
    return render(request, 'landingpage.html', {'form': form})


def privacypolicy(request):
    return render(request, 'core/privacypolicy.html')


def cookiespolicy(request):
    return render(request, 'core/cookiespolicy.html')


def termsnconditions(request):
    return render(request, 'core/termsnconditions.html')


@login_required(login_url='accounts:login')
def appointment(request):
    obj = Meeting.objects.filter(Client=request.user)
    return render(request, 'core/index.html', {'obj': obj})


@login_required(login_url='accounts:login')
def book(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            meet = form.save(commit=False)
            meet.Client = request.user
            meet.save()
            send_mail(
                'Request Received',
                f'Hello {request.user.username},\nWe have received your meeting request on {meet.Date} at {meet.Slot.From} - '
                f'{meet.Slot.To}.\nWe will update you via email as well as on the Website when your meeting has been booked.'
                f'\nregards',
                'contact@quantchef.in',
                [f'{meet.Client.email}', ],
                fail_silently=False,
            )
            send_mail(
                'Meeting Request Received',
                f'Hello admin,\nNew meeting request received from {request.user.username} {meet.Date} at {meet.Slot.From} - '
                f'{meet.Slot.To}.\n request received at {datetime.now()}',
                'contact@quantchef.in',
                ['contact@quantchef.in', ],
                fail_silently=False,
            )
            return redirect('core:appointments')
    else:
        form = MeetingForm

    return render(request, 'core/book-appointment.html', {'form': form, })


def load_slots(request):
    datestr = request.GET.get('Date')  # get selected date
    date = datetime.strptime(datestr, '%m/%d/%Y')  # convert received input from str to datetime obj
    day = calendar.day_name[date.weekday()]  # get Name of day corresponding to date
    if Meeting.objects.filter(Date=date).exists():  # check id any meeting exists on user selected date
        slotid = Meeting.objects.filter(Date=date, Status__in=['Requested', 'Booked']).values(
            'Slot')  # get list of slots occupied on user selected date
        slots = Slot.objects.filter(Day__Name=day, Status='Available').exclude(
            id__in=slotid)  # get available slots for users day and exclude occupied slots
    else:
        slots = Slot.objects.filter(Day__Name=day, Status='Available')  # query to get available slots on specified day

    return render(request, 'core/slot_dropdown_list_options.html', {'slots': slots})


# bot market

def ShopView(request):
    if request.method == 'POST':
        form = ShopForm(request.POST, request.FILES)
        print("------In View------")

        if form.is_valid():
            print("------Form Valid------")
            form.save()
            return redirect('core:appointments')
    else:
        form = ShopForm
    return render(request, 'core/Shop.html', {'form': form, })


def AdsView(request):
    obj = Shop.objects.all()
    context = {
        'obj': obj,
    }
    return render(request, 'core/adsview.html', context)

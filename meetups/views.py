from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from .models import Meetup,Participant
from .forms import RegistrationForm


def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html',{
        'meetups':meetups
    })

def meetups_details(request,slug):
    meetup = get_object_or_404(Meetup,slug=slug)
    if request.method == 'GET':
        registration_form = RegistrationForm()

    else:
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            user_email = registration_form.cleaned_data['email']
            participant, _ = Participant.objects.get_or_create(email=user_email)
            meetup.participant.add(participant)

            return redirect('success-page',slug=slug)

    meetup_is_found = True
    if meetup is None:
        meetup_is_found = False

    context = {
        'meetup':meetup,
        'slug':meetup.slug,
        'meetup_found':meetup_is_found,
        'form':registration_form
    }
    return render(request, 'meetups/meetup-detail.html',context)

def confirm_registration(request,slug):
    meetup = get_object_or_404(Meetup,slug=slug)

    return render(request, 'meetups/registration-success.html',{'email':meetup.organizer_email})
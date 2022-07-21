from django.shortcuts import render, redirect
from .models import Doctors, Services, Departaments, About_Us, Awards, Pricing, Questions, Info, Features, Testimonials
from .forms import UserReservationForm, ContactForm


def main_page(request):
    if request.method == 'POST':
        reservation = UserReservationForm(request.POST)
        contact_form = ContactForm(request.POST)
        if reservation.is_valid():
            reservation.save()
        if contact_form.is_valid():
            contact_form.save()
            return redirect('/')


    reservation = UserReservationForm()
    contact_form = ContactForm()
    doctors = Doctors.objects.filter(is_visible=True).order_by('position')
    services = Services.objects.filter(is_visible=True).order_by('position')
    departments = Departaments.objects.filter(is_visible=True).order_by('position')
    about_us = About_Us.objects.all
    awards = Awards.objects.all
    pricing = Pricing.objects.filter(is_visible=True)
    questions = Questions.objects.filter(is_visible=True)
    info = Info.objects.all
    features = Features.objects.all
    testimonials = Testimonials.objects.all

    return render(request, 'main.html', context={
        'doctors': doctors,
        'services': services,
        'reservation': reservation,
        'departments': departments,
        'about_us': about_us,
        'awards': awards,
        'pricing': pricing,
        'questions': questions,
        'info': info,
        'contact_form': contact_form,
        'features': features,
        'testimonials': testimonials,

        })


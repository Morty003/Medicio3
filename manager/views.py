from django.shortcuts import render, redirect
from main_page.models import UserReservation, Contact
from django.contrib.auth.decorators import login_required, user_passes_test


def is_manager(user):
    return user.groups.filter(name='manager').exists()

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def reservation_list(request):
    lst = UserReservation.objects.filter(is_processed=False)
    return render(request, 'reservation_list.html', context={'lst': lst})


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_reservation(request, pk):
    UserReservation.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:reservations_list')


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def contact_list(request):
    lst2 = Contact.objects.filter(is_processed=False)
    return render(request, 'contact_message.html', context={'lst2': lst2})


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_contact(request, pk):
    Contact.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:contact_list')
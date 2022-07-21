from django.urls import path
from .views import reservation_list, update_reservation, contact_list, update_contact

app_name = 'manager'

urlpatterns = [
    path('reservations/', reservation_list, name='reservations_list'),
    path('reservations/update/<int:pk>/', update_reservation, name='update_reserve'),
    path('contact_form/', contact_list, name='contact_list'),
    path('contact_form/update/<int:pk>/', update_contact, name='update_contact'),
]
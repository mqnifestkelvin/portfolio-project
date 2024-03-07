from django.urls import path

from . import views

urlpatterns = [
    path('payment-success', views.payment_successs, name='payment_success'),
    path('payment-failed', views.payment_failed, name='payment_failed')
]
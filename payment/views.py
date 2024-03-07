from django.shortcuts import render

def payment_successs(request):
    return render(request, 'payment/payment-success.html')

def payment_failed(request):
    return render(request, 'payment/payment-failed.html')

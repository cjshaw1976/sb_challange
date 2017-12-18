from django.shortcuts import render, redirect

from .forms import AccountForm
from account.models import Customer

def home(request):
    return render(request, 'home.html', {})

def customer_login(request):
    form = AccountForm()
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            customer = Customer.objects.filter(
                user_name=form.cleaned_data['user_name'],
                password=form.cleaned_data['password']
            ).first()

            if customer:
                # create session
                return redirect('home')

            # create error message
            form.add_error(None, 'Invalid username and password combination.')

    return render(request, 'customer_login.html', { 'form': form })

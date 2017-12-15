from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AccountForm
from .models import Customer

# List all customers accounts
def listAccounts(request):
    customer_list = Customer.objects.order_by('user_name')
    page = request.GET.get('page', 1)

    paginator = Paginator(customer_list, 10)

    try:
        customers = paginator.page(page)
    except PageNotAnInteger:
        customers = paginator.page(1)
    except EmptyPage:
        customers = paginator.page(paginator.num_pages)

    return render(request, 'account_list.html', {'customers': customers})


# Create a new customer account
def newAccount(request):
    form = AccountForm()
    if request.method == "POST":
        form = AccountForm(request.POST, request.FILES)
        if form.is_valid():
            account = form.save(commit=False)
            account.created_by = request.user
            account.save()
            # Todo, send sms here
            return redirect('view_account', user_name=account.user_name)

    return render(request, 'account_edit.html', {'form': form})


# View a customer account
def viewAccount(request, user_name):
    customer = get_object_or_404(Customer, user_name=user_name)
    return render(request, 'account_view.html', {'customer': customer})


# Edit a customer account
def editAccount(request, user_name):
    return render(request, 'start.html', {})

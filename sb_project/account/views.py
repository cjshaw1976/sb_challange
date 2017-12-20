from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AccountForm
from .models import Customer, AccessLog

from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

"""
I am using a free account with no credit, so it not actually going to send
an SMS, otherwise putting these detail publically on github is a bad idea.
"""

# Your Account SID from twilio.com/console
account_sid = "AC819e285399a13897370bcc8f7f160ffa"
# Your Auth Token from twilio.com/console
auth_token  = "c516d4d8c58b54da9422271521fa2a81"

# List all customers accounts
@login_required
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
@login_required
def newAccount(request):
    form = AccountForm()
    if request.method == "POST":
        form = AccountForm(request.POST, request.FILES)
        if form.is_valid():
            account = form.save(commit=False)
            account.created_by = request.user
            account.save()

            messages.success(request, 'Account for {} {} has been successfully created!'.format(account.first_name, account.last_name))
            AccessLog.objects.create(customer=account,
                                     user=request.user,
                                     level=AccessLog.SUCCESS,
                                     notes='Account created successfully!')

            # Send SMS
            try:
                client = Client(account_sid, auth_token)
                message = client.messages.create(
                    to=form.cleaned_data['phone_number'],
                    from_="+13345642095",
                    body="Your SB account {} has been opened.".format(account.pk))
                messages.success(request, 'SMS sent to {} successfully!'.format(form.cleaned_data['phone_number']))
                AccessLog.objects.create(customer=account,
                                         level=AccessLog.SUCCESS,
                                         notes='SMS sent to {} successfully!'.format(form.cleaned_data['phone_number']))

            except TwilioRestException as e:
                print(e)
                messages.warning(request, 'SMS sent to {} Failed! Please see error console.'.format(form.cleaned_data['phone_number']))
                AccessLog.objects.create(customer=account,
                                         level=AccessLog.WARNING,
                                         notes="SMS sending failed. {}".format(e))

            return redirect('view_account', user_name=account.user_name)

    return render(request, 'account_edit.html', {'form': form})


# View a customer account
@login_required
def viewAccount(request, user_name):
    customer = get_object_or_404(Customer, user_name=user_name)
    return render(request, 'account_view.html', {'customer': customer})


# Edit a customer account
@login_required
def editAccount(request, user_name):
    return render(request, 'start.html', {})

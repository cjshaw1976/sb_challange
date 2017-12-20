from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import AccountForm
from account.models import Customer, CustomerSession

from django.contrib.sessions.models import Session

from datetime import datetime
from django.utils import timezone
import pytz

def home(request):
    return render(request, 'home.html', {})

def customer_home(request):
    # Redirect if not logged in
    if not 'user_name' in request.session:
        return redirect('home')

    # Set the session to automatically expire in 5 minutes
    request.session.set_expiry(300)
    return render(request, 'home.html', {})

def customer_logout(request):
    if 'user_name' in request.session:
        # Delete session from db
        messages.info(request, 'User {} logged out.'.format(request.session['display_name']))
        # log db here
        customer_sessions = CustomerSession.objects.filter(customer__user_name=request.session['user_name'])
        for customer_session in customer_sessions:
            customer_session.session.delete()

    return redirect('home')

def customer_login(request):
    form = AccountForm()
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            # Check username and password match
            customer = Customer.objects.filter(
                user_name=form.cleaned_data['user_name'],
                password=form.cleaned_data['password']
            ).first()

            if customer:
                # Check user is not yet logged in
                logged_in = CustomerSession.objects.filter(customer=customer).first()

                # If the customer is logged in and the session has not expired
                if logged_in and timezone.now() < logged_in.session.expire_date:

                    print(Session.objects.get(pk=logged_in.session))
                    #error already logged in
                    # log db here
                    form.add_error(None,
                                   "Customer '{} {}' is already logged in. Timestamp: {}. IP: {}. Agent: {}.".format(
                                        customer.first_name,
                                        customer.last_name,
                                        logged_in.start_time,
                                        logged_in.ip,
                                        logged_in.agent)
                                    )
                else:
                    # Delete any expired sessions
                    if logged_in and timezone.now() > logged_in.session.expire_date:
                        # log db here
                        messages.info(request, 'User {} logged out due to period of inactivity.'.format(request.session['display_name']))
                        logged_in.session.delete()


                    # Start a session
                    if not request.session.session_key:
                        request.session.create()

                    # Get the session object
                    session = Session.objects.get(pk=request.session.session_key)

                    # Get the user IP
                    ip = request.META.get('HTTP_X_FORWARDED_FOR')
                    if ip == None:
                        ip=request.META.get('REMOTE_ADDR')

                    # Create an entry in the database
                    log_in = CustomerSession.objects.create(
                        customer=customer,
                        session=session,
                        ip=ip,
                        agent=request.META.get('HTTP_USER_AGENT')
                    )

                    log_in.save()
                        # log db here

                    # Set session Variable
                    request.session['user_name'] = customer.user_name
                    request.session['display_name'] = '{} {}'.format(customer.first_name, customer.last_name)

                    # Redirect to home
                    return redirect('customer_home')

            else:
                # create error message if invalid
                # log db here
                form.add_error(None, 'Invalid username and password combination.')

    return render(request, 'customer_login.html', { 'form': form })

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.shortcuts import render

from account.models import AccessLog, Customer

@login_required
def totals(request):
    # Count of customers created by staff_login, order by count desc
    created = Customer.objects.values('created_by__username').annotate(created_count=Count('user_name'))
    created.order_by('-created_count')

    # All customers in reverse created date order
    customers_list = Customer.objects.order_by('-created_date')

    # Apply Pagenation to customer list
    page = request.GET.get('page', 1)
    paginator = Paginator(customers_list, 10)

    try:
        customers = paginator.page(page)
    except PageNotAnInteger:
        customers = paginator.page(1)
    except EmptyPage:
        customers = paginator.page(paginator.num_pages)

    # Log View
    AccessLog.objects.create(user=request.user,
                             level=AccessLog.INFO,
                             notes="Viewed totals backend: {}".format(request.META.get('QUERY_STRING')))

    return render(request, 'backend_totals.html', {'created': created,
                                                    'customers': customers,
                                                    })


@login_required
def logs(request):
    # Get data
    customers = Customer.objects.order_by('last_name', 'first_name')
    users = User.objects.order_by('last_name', 'first_name')
    log_list = AccessLog.objects.order_by('-timestamp')

    if request.GET.get('severity') and request.GET['severity'] != '':
        log_list = log_list.filter(level=request.GET['severity'])

    if request.GET.get('staff') and request.GET['staff'] != '':
        log_list = log_list.filter(user__username=request.GET['staff'])

    if request.GET.get('customer') and request.GET['customer'] != '':
        log_list = log_list.filter(customer__user_name=request.GET['customer'])

    page = request.GET.get('page', 1)
    paginator = Paginator(log_list, 20)

    try:
        log = paginator.page(page)
    except PageNotAnInteger:
        log = paginator.page(1)
    except EmptyPage:
        log = paginator.page(paginator.num_pages)

    # Log View
    AccessLog.objects.create(user=request.user,
                             level=AccessLog.INFO,
                             notes="Viewed logs backend: {}".format(request.META.get('QUERY_STRING')))

    return render(request, 'backend_log.html', {'log': log,
                                            'customers': customers,
                                            'users': users,
                                            })

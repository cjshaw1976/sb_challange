from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from account.models import AccessLog, Customer

@login_required
def backend(request):
    # Get gata
    customers = Customer.objects.order_by('last_name', 'first_name')
    users = User.objects.order_by('last_name', 'first_name')
    log_list = AccessLog.objects.order_by('-timestamp')
    page = request.GET.get('page', 1)

    paginator = Paginator(log_list, 10)

    try:
        log = paginator.page(page)
    except PageNotAnInteger:
        log = paginator.page(1)
    except EmptyPage:
        log = paginator.page(paginator.num_pages)

    # Log View
    AccessLog.objects.create(user=request.user,
                             level=AccessLog.INFO,
                             notes="Viewed backend, page: {}".format(page))

    return render(request, 'backend.html', {'log': log,
                                            'customers': customers,
                                            'users': users,
                                            })

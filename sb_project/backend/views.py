from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from account.models import AccessLog

@login_required
def backend(request):
    log_list = AccessLog.objects.order_by('-timestamp')
    page = request.GET.get('page', 1)

    paginator = Paginator(log_list, 10)

    try:
        log = paginator.page(page)
    except PageNotAnInteger:
        log = paginator.page(1)
    except EmptyPage:
        log = paginator.page(paginator.num_pages)

    return render(request, 'backend.html', {'log': log})

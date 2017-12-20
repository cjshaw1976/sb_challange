from django.shortcuts import render

def backend(request):
    return render(request, 'backend.html', {})

from django.shortcuts import render

from .forms import AccountForm


def listAccounts(request):
    return render(request, 'start.html', {})

def newAccount(request):
    form = AccountForm()
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.created_by = request.user
            account.save()
            return redirect('view_account', userName=account.user_name)

    return render(request, 'account_edit.html', {'form': form})

def viewAccount(request, user_name):
    return render(request, 'start.html', {})

def editAccount(request, user_name):
    return render(request, 'start.html', {})

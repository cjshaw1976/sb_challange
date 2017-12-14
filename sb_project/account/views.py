from django.shortcuts import render, redirect

from .forms import AccountForm

# List all customers accounts
def listAccounts(request):
    return render(request, 'start.html', {})

# Create a new customer account
def newAccount(request):
    form = AccountForm()
    if request.method == "POST":
        form = AccountForm(request.POST, request.FILES)
        if form.is_valid():
            account = form.save(commit=False)
            account.created_by = request.user
            account.save()
            return redirect('view_account', user_name=account.user_name)

    return render(request, 'account_edit.html', {'form': form})

# View a customer account
def viewAccount(request, user_name):
    return render(request, 'start.html', {})

# Edit a customer account
def editAccount(request, user_name):
    return render(request, 'start.html', {})

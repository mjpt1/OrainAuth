from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages

from accounts.decorators import redirect_if_authenticated


@redirect_if_authenticated(path='dashboard')
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid Username or Password')
            return redirect('login')

        login(request, user)
        return redirect('dashboard')

    return render(request, 'registration/login.html')

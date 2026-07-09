from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib import messages

from accounts.decorators import redirect_if_authenticated

# Changing the model or the underlying database schema later in the development
# cycle will not cause any breaking changes or system failures
User = get_user_model()

# --------------
# Login Section
# --------------
@redirect_if_authenticated(path='dashboard')
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            # If the username does not exist in the accounts_orainauth table
            messages.error(request, 'Invalid Username or Password')
            return redirect('login')

        # Check user for db
        user = authenticate(request, username=username, password=password)

        if user is None:
            # If username is valid but password does not match
            messages.error(request, 'Invalid Username or Password')
            return redirect('login')
        
        else:
            # If username and password are correct
            login(request, user)
            # logging login
            return redirect('dashboard')

    # registration/login.html template
    return render(request, template_name='registration/login.html')

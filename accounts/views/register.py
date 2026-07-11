from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model

from accounts.decorators import redirect_if_authenticated

# Changing the model or the underlying database schema later in the development
# cycle will not cause any breaking changes or system failures
User = get_user_model()

# -----------------
# Register Section
# -----------------
@redirect_if_authenticated(path='dashboard')
def register_page(request):
    if request.user.is_authenticated:
        # If the user is logged in
        return redirect('dashboard')

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user:
            # If username exists in the database
            messages.error(request, 'Username already exists')
            return redirect('register')

        email_found = User.objects.filter(email=email)

        if email_found:
            # If email exists in the database
            messages.error(request, 'Email already exists')
            return redirect('register')

        # Creating a new user in the database
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
            cash = 5000
        )

        return redirect('dashboard')

    # registration/register.html template
    return render(request, template_name='registration/register.html')
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import (
    get_user_model, 
    authenticate, 
    login, 
    logout, 
    update_session_auth_hash
)
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from .forms import UserUpdateForm, PasswordUpdateForm

# Changing the model or the underlying database schema later in the development
# cycle will not cause any breaking changes or system failures
User = get_user_model()

# ----------------------------------------
# System Authentication Section Templates
# ----------------------------------------
class Template:
    TEMPLATE_LOGIN = 'login.html'
    TEMPLATE_REGISTER = 'register.html'
    TEMPLATE_LOGOUT = 'logout.html'
    TEMPLATE_PROFILE = 'users/profile.html'
    TEMPLATE_EDIT_PROFILE = 'users/edit_profile.html'
    TEMPLATE_CHANGE_PASSWORD = 'users/change_password.html'

# Since the Send Reset Password in Email system is for Django itself,
# that is, it is the default, we have to make it work in our Django custom classes so that if the user is logged into their account,
# they will go to the dashboard page
class RedirectDashboard:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # If the user is logged in
            return redirect('dashboard')
        
        return super().dispatch(request, *args, **kwargs)

# -------------------
# Redirect operation
# -------------------
class CustomPasswordResetView(RedirectDashboard, PasswordResetView):
    pass
class CustomPasswordResetDoneView(RedirectDashboard, PasswordResetDoneView):
    pass
class CustomPasswordResetConfirmView(RedirectDashboard, PasswordResetConfirmView):
    pass
class CustomPasswordResetCompleteView(RedirectDashboard, PasswordResetCompleteView):
    pass

# --------------
# Login Section
# --------------
def login_page(request):
    if request.user.is_authenticated:
        # If the user is logged in
        return redirect('dashboard')
        
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            # If the username does not exist in the accounts_orainauth table
            messages.error(request, 'Invalid Username or Password')
            return redirect('login')

        # Check user for db
        user = authenticate(username=username, password=password)

        if user is None:
            # If username is valid but password does not match
            messages.error(request, 'Invalid Username or Password')
            return redirect('login')
        
        else:
            # If username and password are correct
            login(request, user)
            # logging login
            return redirect('dashboard')

    # login.html template
    return render(request, template_name=Template.TEMPLATE_LOGIN)

# -----------------
# Register Section
# -----------------
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

        # New register logging
        return redirect('dashboard')

    # register.html template
    return render(request, template_name=Template.TEMPLATE_REGISTER)

# ---------------
# Logout Section
# ---------------
def logout_accounts(request):
    if not request.user.is_authenticated:
        # If the user not logged in
        return redirect('login')

    else:
        # The session is cleared from both the database and the user’s browser
        logout(request)
        return redirect('login')

# ----------------
# Profile Section
# ----------------
def profile_page(request):
    if not request.user.is_authenticated:
        # If the user not logged in
        return redirect('login')
    
    else:
        # User information
        user = request.user

    return render(request, template_name=Template.TEMPLATE_PROFILE, context={'user': user})

# ---------------------
# Edit Profile Section
# ---------------------
def edit_profile(request):
    if not request.user.is_authenticated:
        # If the user not logged in
        return redirect('login')

    else:
        if request.method == "POST":
            # Receive information entered by the user
            post_data = request.POST.copy()
            # Change in database
            form = UserUpdateForm(post_data, instance=request.user)
            
            if form.is_valid():
                # Save in database
                form.save()

                return redirect('profile')

            else:
                messages.error(request, 'Error: Please try again')
            
        else:
            # Initial template for GET method
            form = UserUpdateForm(instance=request.user)

    return render(request, template_name=Template.TEMPLATE_EDIT_PROFILE, context={'form': form})

# ----------------------
# Edit Password Section
# ----------------------
def change_password(request):
    if not request.user.is_authenticated:
        # If the user not logged in 
        return redirect('login')

    else:
        if request.method == "POST":
            # Comparison between new request and old information
            form = PasswordUpdateForm(request.POST)

            if form.is_valid():
                user = request.user
                
                old_pw = form.cleaned_data['old_password']
                new_pw = form.cleaned_data['new_password']

                if user.check_password(old_pw):
                    if old_pw == new_pw:
                        # If the new password matches the old password
                        messages.error(request, 'New password must not match the old password')
                        return redirect('change_password')

                    # Hashing new password
                    user.set_password(new_pw)
                    # Save in DB
                    user.save()

                    # Preventing user session changes in the database to avoid being logged out of the system
                    update_session_auth_hash(request, user)
                    return redirect('profile')
                
                else:
                    # If current password does not match
                    messages.error(request, 'Current password is incorrect')
                    return redirect('change_password')

            else:
                # If everything wasn't okay
                messages.error(request, 'Password and Confirm Password Field do not match')

        else:
            # Initial template for GET method
            form = PasswordUpdateForm()

    return render(request, template_name=Template.TEMPLATE_CHANGE_PASSWORD, context={'form': form})
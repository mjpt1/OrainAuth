from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from accounts.decorators import redirect_if_not_authenticated
from accounts.forms import PasswordUpdateForm


@redirect_if_not_authenticated(path='login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordUpdateForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = request.user
            user.set_password(form.cleaned_data['new_password'])
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password updated successfully')
            return redirect('profile')

        for errors in form.errors.values():
            for error in errors:
                messages.error(request, error)
    else:
        form = PasswordUpdateForm(user=request.user)

    return render(request, 'users/change_password.html', {'form': form})

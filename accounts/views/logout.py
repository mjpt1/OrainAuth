from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views.decorators.http import require_POST

from accounts.decorators import redirect_if_not_authenticated


@redirect_if_not_authenticated(path='login')
@require_POST
def logout_accounts(request):
    logout(request)
    return redirect('login')

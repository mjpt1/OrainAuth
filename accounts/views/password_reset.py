from django.shortcuts import redirect
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

# Since the Send Reset Password in Email system is for Django itself,
# that is, it is the default, we have to make it work in our Django custom classes so that if the user is logged into their account,
# they will go to the dashboard page
class RedirectDashboard:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
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

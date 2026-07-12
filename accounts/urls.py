from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_accounts, name='logout'),
    path('profile/', views.profile_page, name='profile'),
    path('profile/change-password/', views.change_password, name='change_password'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path(
        'password-reset/',
        views.CustomPasswordResetView.as_view(
            template_name='registration/password_reset_form.html',
            email_template_name='registration/password_reset_email.html',
        ),
        name='password_reset_form',
    ),
    path(
        'password-reset/done/',
        views.CustomPasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html',
        ),
        name='password_reset_done',
    ),
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        views.CustomPasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html',
        ),
        name='password_reset_confirm',
    ),
    path(
        'password-reset-complete/',
        views.CustomPasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html',
        ),
        name='password_reset_complete',
    ),
]

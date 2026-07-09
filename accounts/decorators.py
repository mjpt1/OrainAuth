from django.shortcuts import redirect
from collections.abc import Callable
from decorator import decorator

def redirect_if_authenticated(path: str = 'dashboard'):
    """
    A decorator that checks if the user is logged in, 
    redirects to the page the user specified in the route. 
    If the route is empty, it defaults to the `dashboard` page
    """
    @decorator
    def wrapper(func: Callable, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(path)
        return func(request, *args, **kwargs)
    return wrapper

def redirect_if_not_authenticated(path: str = 'login'):
    """
    A decorator that checks if the user is not logged in,
    redirects to the page specified in the route.
    If the route has no value, it defaults to the `login` page
    """
    @decorator
    def wrapper(func: Callable, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(path)
        return func(request, *args, **kwargs)
    return wrapper

from functools import wraps
from django.shortcuts import redirect


def redirect_if_authenticated(path: str = 'dashboard'):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                return redirect(path)
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator


def redirect_if_not_authenticated(path: str = 'login'):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect(path)
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator

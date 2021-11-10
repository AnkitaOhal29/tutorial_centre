def uppercase_decorator(function):
    def inner():
        import pdb;pdb.set_trace()
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return inner


def white_list_check():
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            import pdb;pdb.set_trace()
            ip = request.META.get('REMOTE_ADDR', '0.0.0.0')
            if ip in WHITE_LIST:
                return func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden()
        return wrapper
    return decorator


def decorator(view):
    # do something that requires view's class
    print('--------------aaaaaaaaaa-------------')
    return view


def require_ajax(func):
    def decorator(func):
        def inner(request, *args, **kwargs):
            print('--------------aaaaaaaaaa-------------')
            if not request.is_ajax():
                return HttpResponseBadRequest()
            return func(request, *args, **kwargs)
        return inner

    return decorator



from django.core.exceptions import PermissionDenied

def user_is_entry_author(function):
    def wrap(request, *args, **kwargs):
        if request.user:
            print('aaaaaaaaaaaaa')
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    # wrap.__doc__ = function.__doc__
    # wrap.__name__ = function.__name__
    return wrap
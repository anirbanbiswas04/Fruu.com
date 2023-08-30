from django.core.exceptions import PermissionDenied
from .models import Listing


def owner_verifier(function):

    def wrapper(request, *args, **kwargs):
        listing = Listing.objects.get(slug=kwargs['slug'])
        if listing.created_by == request.user:
            return function(request, *args, **kwargs)
        raise PermissionDenied
    
    return wrapper
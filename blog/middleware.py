# middleware.py

from django.shortcuts import redirect
from django.urls import reverse
from myblog.models import Profile

class ProfileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            # Check if the user has a profile
            has_profile = hasattr(request.user, 'profile') and request.user.profile is not None

            if not has_profile:
                if not request.path.startswith(reverse('create_profile_page')):
                    return redirect('create_profile_page')

        return response

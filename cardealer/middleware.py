# middleware.py
from django.shortcuts import render

class CustomLoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Check if the user is not logged in and the response status code is 403 (forbidden)
        if not request.user.is_authenticated and response.status_code == 403:
            # Render a custom 404 template
            return render(request, '404.html', status=404)

        return response

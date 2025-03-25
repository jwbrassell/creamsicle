"""
Custom middleware for the Django project.
"""

from django.middleware.csrf import get_token
from django.utils.safestring import mark_safe

class JinjaCSRFMiddleware:
    """
    Middleware that adds CSRF token support to Jinja2 templates.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        # Get the CSRF token for this request
        csrf_token = get_token(request)
        
        # Add CSRF token functions to the Jinja2 environment
        if hasattr(request, 'jinja2_env'):
            request.jinja2_env.globals['csrf_token'] = lambda: csrf_token
            request.jinja2_env.globals['csrf_input'] = lambda: mark_safe(
                f'<input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">'
            )
            
        response = self.get_response(request)
        return response

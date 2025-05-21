from django.utils.deprecation import MiddlewareMixin

class BaseHabiroleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            # Extract roles from OIDC claims or external service
            roles = request.session.get('oidc_roles', [])
            # Map roles to Django groups or permissions
            for role in roles:
                if role == 'admin':
                    request.user.is_staff = True
                elif role == 'viewer':
                    request.user.groups.add('viewers')
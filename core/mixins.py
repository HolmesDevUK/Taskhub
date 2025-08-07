from django.http import HttpResponseForbidden

class RoleRequiredMixin:
    required_role = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden("Authentication required.")
        if self.required_role and request.user.role != self.required_role:
            return HttpResponseForbidden("You are not allowed to access this page.")
        return super().dispatch(request, *args, **kwargs)

class ClientRequiredMixin(RoleRequiredMixin):
    required_role = "client"
    
class AdminRequiredMixin(RoleRequiredMixin):
    required_role = "client"
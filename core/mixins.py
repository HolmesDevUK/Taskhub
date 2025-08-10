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
    required_role = "admin"

class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            existing_classes = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = (existing_classes + "form-control").strip()
        
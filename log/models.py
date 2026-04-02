import uuid
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class ActivityLog(models.Model):

    class ActionType(models.TextChoices):
        LOGIN = "LOGIN", "Login"
        LOGOUT = "LOGOUT", "Logout"
        REGISTER = "REGISTER", "Register"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    action = models.CharField(max_length=20, choices=ActionType.choices)

    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def log(cls, *, user, action, request):
        from .utils import get_client_ip, get_user_agent

        cls.objects.create(
            user=user,
            action=action,
            ip_address=get_client_ip(request),
            user_agent=get_user_agent(request),
        )
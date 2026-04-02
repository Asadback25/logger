from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from .models import ActivityLog


@receiver(user_logged_in)
def log_login(sender, request, user, **kwargs):
    ActivityLog.log(
        user=user,
        action=ActivityLog.ActionType.LOGIN,
        request=request
    )


@receiver(user_logged_out)
def log_logout(sender, request, user, **kwargs):
    ActivityLog.log(
        user=user,
        action=ActivityLog.ActionType.LOGOUT,
        request=request
    )
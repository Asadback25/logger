from django.contrib import admin
from .models import ActivityLog


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "action",
        "ip_address",
        "short_user_agent",
        "created_at",
    )

    list_filter = (
        "action",
        "created_at",
    )

    search_fields = (
        "user__username",
        "ip_address",
        "user_agent",
    )

    ordering = ("-created_at",)

    readonly_fields = (
        "user",
        "action",
        "ip_address",
        "user_agent",
        "created_at",
    )

    list_per_page = 20
    date_hierarchy = "created_at"

    # 🔥 user_agent ni qisqartirib ko‘rsatish
    def short_user_agent(self, obj):
        if obj.user_agent:
            return obj.user_agent[:50]
        return "-"

    short_user_agent.short_description = "User Agent"
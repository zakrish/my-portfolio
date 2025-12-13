from django.contrib import admin
from .models import UserActivity, SystemMetric


@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ['user', 'activity_type', 'created_at']
    list_filter = ['activity_type']
    search_fields = ['user__username', 'description']
    readonly_fields = ['created_at']


@admin.register(SystemMetric)
class SystemMetricAdmin(admin.ModelAdmin):
    list_display = ['metric_name', 'metric_value', 'recorded_at']
    list_filter = ['metric_name']
    search_fields = ['metric_name']
    readonly_fields = ['recorded_at']

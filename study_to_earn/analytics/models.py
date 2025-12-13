from django.db import models
from django.conf import settings


class UserActivity(models.Model):
    """Model to track user activities."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'analytics_user_activity'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.activity_type}"


class SystemMetric(models.Model):
    """Model for system-wide metrics."""
    metric_name = models.CharField(max_length=100)
    metric_value = models.FloatField()
    metadata = models.JSONField(default=dict, blank=True)
    recorded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'analytics_system_metrics'
        ordering = ['-recorded_at']

    def __str__(self):
        return f"{self.metric_name}: {self.metric_value}"

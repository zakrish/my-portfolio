from django.db import models
from django.conf import settings


class LeaderboardEntry(models.Model):
    """Model for leaderboard entries."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    rank = models.IntegerField(null=True, blank=True)
    month = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'leaderboard_entries'
        ordering = ['-score']
        unique_together = ['user', 'month']

    def __str__(self):
        return f"{self.user.username} - {self.score} points"

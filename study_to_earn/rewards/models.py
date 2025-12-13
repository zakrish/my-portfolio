from django.db import models
from django.conf import settings


class Reward(models.Model):
    """Model for available rewards."""
    name = models.CharField(max_length=200)
    description = models.TextField()
    points_required = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'rewards'

    def __str__(self):
        return self.name


class UserReward(models.Model):
    """Model to track user rewards."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE)
    claimed_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('delivered', 'Delivered'),
    ], default='pending')

    class Meta:
        db_table = 'user_rewards'

    def __str__(self):
        return f"{self.user.username} - {self.reward.name}"

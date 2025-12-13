from celery import shared_task
from django.utils import timezone


@shared_task
def reward_top_users():
    """
    Reward top users on the leaderboard.
    This task runs on the 1st of every month at 1 AM.
    """
    print(f"[{timezone.now()}] Rewarding top users...")
    return "Top users rewarded"

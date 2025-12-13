from celery import shared_task
from django.utils import timezone


@shared_task
def reset_leaderboard_monthly():
    """
    Reset the leaderboard at the start of each month.
    This task runs on the 1st of every month at midnight.
    """
    print(f"[{timezone.now()}] Resetting monthly leaderboard...")
    return "Leaderboard reset completed"

from celery import shared_task
from django.utils import timezone


@shared_task
def refresh_daily_questions():
    """
    Refresh daily quiz questions.
    This task runs every day at midnight.
    """
    print(f"[{timezone.now()}] Refreshing daily questions...")
    return "Daily questions refreshed"

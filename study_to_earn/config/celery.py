import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('study_to_earn')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'reset-leaderboard-monthly': {
        'task': 'leaderboard.tasks.reset_leaderboard_monthly',
        'schedule': crontab(day_of_month='1', hour='0', minute='0'),
    },
    'reward-top-users': {
        'task': 'rewards.tasks.reward_top_users',
        'schedule': crontab(day_of_month='1', hour='1', minute='0'),
    },
    'refresh-daily-questions': {
        'task': 'quiz.tasks.refresh_daily_questions',
        'schedule': crontab(hour='0', minute='0'),
    },
}

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

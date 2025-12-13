from django.db import models
from django.conf import settings


class Question(models.Model):
    """Model for quiz questions."""
    title = models.CharField(max_length=500)
    content = models.TextField()
    difficulty = models.CharField(max_length=20, choices=[
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ])
    points = models.IntegerField(default=10)
    is_daily = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'quiz_questions'

    def __str__(self):
        return self.title


class Answer(models.Model):
    """Model for quiz answers."""
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    class Meta:
        db_table = 'quiz_answers'

    def __str__(self):
        return f"{self.question.title} - {self.text}"


class UserAnswer(models.Model):
    """Model to track user answers."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    is_correct = models.BooleanField()
    answered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'quiz_user_answers'

from django.contrib import admin
from .models import Question, Answer, UserAnswer


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'difficulty', 'points', 'is_daily', 'created_at']
    list_filter = ['difficulty', 'is_daily']
    search_fields = ['title', 'content']
    inlines = [AnswerInline]


@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ['user', 'question', 'is_correct', 'answered_at']
    list_filter = ['is_correct']
    search_fields = ['user__username']

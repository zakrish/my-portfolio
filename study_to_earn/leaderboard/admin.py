from django.contrib import admin
from .models import LeaderboardEntry


@admin.register(LeaderboardEntry)
class LeaderboardEntryAdmin(admin.ModelAdmin):
    list_display = ['user', 'score', 'rank', 'month', 'updated_at']
    list_filter = ['month']
    search_fields = ['user__username']

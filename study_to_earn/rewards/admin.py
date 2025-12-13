from django.contrib import admin
from .models import Reward, UserReward


@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    list_display = ['name', 'points_required', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['name']


@admin.register(UserReward)
class UserRewardAdmin(admin.ModelAdmin):
    list_display = ['user', 'reward', 'status', 'claimed_at']
    list_filter = ['status']
    search_fields = ['user__username', 'reward__name']

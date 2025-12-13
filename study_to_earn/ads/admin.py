from django.contrib import admin
from .models import Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'impressions', 'clicks', 'ctr', 'created_at']
    list_filter = ['is_active']
    search_fields = ['title', 'content']
    readonly_fields = ['impressions', 'clicks', 'ctr']

    def ctr(self, obj):
        return f"{obj.ctr:.2f}%"
    ctr.short_description = 'CTR'

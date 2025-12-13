from django.db import models


class Advertisement(models.Model):
    """Model for advertisements."""
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='ads/', blank=True, null=True)
    url = models.URLField()
    is_active = models.BooleanField(default=True)
    impressions = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return self.title

    @property
    def ctr(self):
        """Calculate click-through rate."""
        if self.impressions > 0:
            return (self.clicks / self.impressions) * 100
        return 0

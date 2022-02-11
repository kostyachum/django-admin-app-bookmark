from django.db import models


class AppBookmark(models.Model):
    user_id = models.UUIDField()
    app_label = models.CharField(max_length=256)
    order = models.IntegerField(default=0)

    class Meta:
        unique_together = ['user_id', 'app_label']

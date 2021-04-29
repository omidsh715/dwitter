from django.db import models
from django.conf import settings

# Create your models here.




class tweet(models.Model):
    content = models.TextField(max_length=140)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField()

    def __str__(self):
        c = self.content[:30]
        return c
    class Meta:
         ordering = ['-created_at']





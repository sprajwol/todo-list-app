from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    complete_status = models.BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['complete_status']
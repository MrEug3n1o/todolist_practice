from django.db import models
from django.urls import reverse
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag-list')

class Task(models.Model):
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    deadline_datetime = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ['is_done', '-created_datetime']

    def __str__(self):
        return self.content[:50]

    def get_absolute_url(self):
        return reverse('home')

    def toggle_status(self):
        self.is_done = not self.is_done
        self.save()

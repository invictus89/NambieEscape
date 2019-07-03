from django.db import models
from django.urls import reverse
from django.conf import settings

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    title_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pk',)

    @property
    def get_html_url(self):
        url = reverse('calendar:edit', args=(self.id,))
        bg_color = ''
        if self.title_type == '기념일':
            bg_color = 'bg-primary'
        elif self.title_type == '뉴스':
            bg_color = 'bg-secondary'
        elif self.title_type == '사건사고':
            bg_color = 'bg-danger'
        elif self.title_type == '역사':
            bg_color = 'bg-success'
        return f'<a href="#" class="my-day text-white font-weight-bolder {bg_color}" data-toggle="modal" data-target="#myModal" data-title={self.title} data-description={self.description} data-title_type={self.title_type} data-id={self.id}> {self.title} </a>'
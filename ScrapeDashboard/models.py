from django.db import models
from django.contrib.auth.models import User

class ScrapeConfig(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    website_url = models.URLField()
    notifications = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title + "\n" + self.website_url + "\n" + str(self.owner)

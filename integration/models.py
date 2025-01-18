from django.db import models

class HookRequest(models.Model):
    message = models.TextField()
    callback_url = models.URLField()
    response = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def update_response(self,new_response):
        self.response = new_response
        self.save()



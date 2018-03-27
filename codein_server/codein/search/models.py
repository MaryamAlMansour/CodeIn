from django.db import models

# Create your models here.

class Search(models.Model):
    #user = models.ForeignKey('server.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

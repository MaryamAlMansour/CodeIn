from django.db import models
from django.conf import settings


# Creating my-portfolio model.
DEFAULT = 'Pictures/man.png'


class Portfolio(models.Model):

    user = models.OneToOneField('server.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="", default=DEFAULT, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Project(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# the _str_ shows what is displayed when creating a portfolio,project, user, or contact.
    def __str__(self):
        return self.name


class Contact(models.Model):
    user_from = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='rel_from_set', on_delete=models.CASCADE)
    user_to = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='rel_to_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return '{} follows {}'.format(self.user_from, self.user_to)

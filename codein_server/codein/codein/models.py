from django.db import models

# Creating my-portfolio model.


class Project(models.Model):

    user = models.ForeignKey('server.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

    name.order_by('created_at').first()

    """
    def create_protfolio(self,name,description,user):

    def add_project(self, name, description):
        
    def edit_protfolio(self, name, description):

    def edit_project(self, name, description):
    """


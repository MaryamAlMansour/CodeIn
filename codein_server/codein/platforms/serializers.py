from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):

    # = serializers.CharField(required=True)
    class Meta:
        model = Project
        # you can either include all the fields from models, or excludes the ones you don't need.
        exclude = ['created_at', 'updated_at']


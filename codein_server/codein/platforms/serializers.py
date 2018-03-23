from rest_framework import serializers
from .models import Project, Portfolio


class PortfolioSerializer(serializers.ModelSerializer):

#    user = serializers.Field('user.username')

    class Meta:
        model = Portfolio
        # you can either include all the fields from models, or excludes the ones you don't need.
        exclude = ['created_at', 'updated_at']


class ProjectSerializer(serializers.ModelSerializer):

#    user = serializers.Field('user.username')

    class Meta:
        model = Project
        # you can either include all the fields from models, or excludes the ones you don't need.
        exclude = ['created_at', 'updated_at']


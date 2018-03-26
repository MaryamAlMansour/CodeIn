from rest_framework import serializers
from .models import Project, Portfolio
from rest_framework.parsers import JSONParser


class PortfolioSerializer(serializers.ModelSerializer):

    user = serializers.Field(source='user.username')

    class Meta:
        model = Portfolio
        # you can either include all the fields from models, or excludes the ones you don't need.
        exclude = ['created_at', 'updated_at']


class ProjectSerializer(serializers.ModelSerializer):

    user = serializers.Field(source='user.username')

    class Meta:
        model = Project
        # you can either include all the fields from models, or excludes the ones you don't need.
        exclude = ['created_at', 'updated_at']

        # deserializing the create and update
        def create(self, **validated_data):
            """ Create and return a new `Text` instance, given the validated data. """
            return Project.user.objects.create(**validated_data)

        def update(self, instance, validated_data):
            """ Update and return an existing `Text` instance, given the validated data. """
            instance.name = validated_data.get('name', instance.name)
            instance.description = validated_data.get('code', instance.code)
            instance.save()
            return instance

# serializing object instance & queryset

Project_instance = Project.objects.all().first()
serializer = ProjectSerializer(Project_instance, many=True)


from rest_framework import serializers
from .models import Project, Portfolio, Contact
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


class ContactSerializerRead(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('user_from', 'user_to',)
        ordering = ('-created',)


class ContactSerializerWrite(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ('created',)

    def create(self, validated_data):
        obj = Contact.objects.create(**validated_data)
        return obj


class PortfolioSerializerRead(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Portfolio
        # you can either include all the fields from models, or excludes the ones you don't need.
        fields = ('user', 'image',)


class PortfolioSerializerWrite(serializers.ModelSerializer):

    class Meta:
        model = Portfolio
        # you can either include all the fields from models, or excludes the ones you don't need.
        fields = ('user', 'image',)


class ProjectSerializerRead(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Project
        # you can either include all the fields from models, or excludes the ones you don't need.
        fields = ('user', 'name', 'description',)


class ProjectSerializerWrite(serializers.ModelSerializer):

    class Meta:
        model = Project
        # you can either include all the fields from models, or excludes the ones you don't need.
        exclude = ['created_at', 'updated_at', 'user']


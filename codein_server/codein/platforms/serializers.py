from rest_framework import serializers
from .models import Project, Portfolio, Contact
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


class ContactSerializerRead(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('user_from', 'user_to',)
        ordering = ('-created',)


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





'''
        def __init__(self, *args, **kwargs):

            super(ProjectSerializerRead, self).__init__(*args, **kwargs)
            request = self.context.get("request")
            if request and request.query_params.get('fields'):
                fields = request.query_params.get('fields')
                if fields:
                    fields = fields.split(',')
                    allowed = set(fields)
                    existing = set(self.fields.keys())
                    for field_name in existing - allowed:
                        self.fields.pop(field_name)
'''


class ProjectSerializerWrite(serializers.ModelSerializer):

    class Meta:
        model = Project
        # you can either include all the fields from models, or excludes the ones you don't need.
        exclude = ['created_at', 'updated_at', 'user']


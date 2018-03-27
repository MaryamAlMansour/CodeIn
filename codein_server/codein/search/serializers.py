from rest_framework import serializers
from .models import Search


class SearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Search
        # you can either include all the fields from models, or excludes the ones you don't need.
        exclude = ['created_at', 'updated_at']





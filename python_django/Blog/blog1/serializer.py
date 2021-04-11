from rest_framework import serializers
from blog1.models import Publisher


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

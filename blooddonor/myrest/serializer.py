from rest_framework import serializers
from .models import book


class BookSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = book
		fields = ('url', 'title', 'author')


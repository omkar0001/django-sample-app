from rest_framework import serializers
from news.models import NewsContent
class NewsContentModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = NewsContent
		fields = ('title','description','videoUrl', 'image')
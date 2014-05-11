from django.contrib.auth.models import User, Group
from rest_framework import serializers
from polls.models import Poll, Choice


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')

class PollSerializer(serializers.Serializer):
	pk = serializers.Field()
	question = serializers.CharField(max_length=200)
 	pub_date = serializers.DateTimeField('date published')

	def restore_object(self, attrs, instance=None):
		if instance:
			# Update existing instance
			instance.title = attrs.get('question', instance.question)
			instance.pub_date = attrs.get('code', instance.pub_date)
			return instance

        # Create new instance
		return Poll(**attrs)
class PollModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Poll
		fields = ('question','pub_date')
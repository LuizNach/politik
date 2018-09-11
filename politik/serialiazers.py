from django.contrib.auth.models import User, Group
from rest_framework import serializers
from politik.models import Politician, LawProject


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class PoliticianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Politician
        fields = ('id', 'user_id', 'bio', 'location', 'office')

class LawSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LawProject
        fields = ('id', 'description', 'passed')


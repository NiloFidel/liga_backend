from django.contrib.auth.models import User, Group
from rest_framework import serializers
from liga_app.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = ['url', 'username', 'email', 'groups']
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        #fields = ['url', 'name']
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        #fields = ['url', 'article_name', 'autor', 'document']
        fields = '__all__'
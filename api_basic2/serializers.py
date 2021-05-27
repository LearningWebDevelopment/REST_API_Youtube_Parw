from rest_framework import serializers
from .models import Article2


class ArticleSerializer2(serializers.ModelSerializer):

    class Meta:
        model = Article2
        #fields = ['id', 'title', 'author', 'email']
        fields = '__all__'
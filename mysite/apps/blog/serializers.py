from models import Post
from rest_framework import serializers

class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ('author', 'title', 'created_date', 'published_date')
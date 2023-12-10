from rest_framework import serializers
from .models import Video, Keyword, Categories
from users.serializers import UserSerializer
from users.models import User

class KeywordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    publishedBy = UserSerializer()
    keywords = KeywordsSerializer(many=True)
    class Meta:
        model = Video
        fields = ('id', 'title', 'text', 'video_link', 'photo_link', 'likes', 'dislikes', 'publishedBy', 'keywords', 'view')


    def create(self, validated_data):
        keywordsArray = []
        by = User.objects.get(username=validated_data['publishedBy']['username'])
        newVideo = Video.objects.create(title=validated_data['title'], text=validated_data['text'],video_link = validated_data['video_link'], photo_link=validated_data['photo_link'], publishedBy = by)
        for keyword in validated_data['keywords']:
            try:
                kw = Keyword.objects.get(name=keyword['name'])
                newVideo.keywords.add(kw)
            except:
                newKeyword = Keyword.objects.create(name=keyword['name'])
                newKeyword.save()
                kw = Keyword.objects.get(name=keyword['name'])
                newVideo.keywords.add(kw)
        newVideo.save()
        return newVideo
    
    def update(self, instance, validated_data):
        keywords = validated_data.pop('keywords')
        instance.video_link = validated_data.get('video_link')
        instance.photo_link = validated_data.get('photo_link')
        instance.title = validated_data.get('title')
        instance.text = validated_data.get('text')
        instance.view = validated_data.get('view')
        instance.keywords.set([])
        keepKeywords = []
        for keyword in keywords:
            try:
                kw = Keyword.objects.get(name=keyword['name'])
                keepKeywords.append(kw)
            except:
                Keyword.objects.create(name = keyword['name'])
                kw = Keyword.objects.get(name=keyword['name'])
                keepKeywords.append(kw)
        instance.keywords.set(keepKeywords)
        instance.save()
        return instance
            
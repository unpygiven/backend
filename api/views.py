from typing import Any
from rest_framework.response import Response
from rest_framework.decorators import api_view
from videos.models import Video, Categories
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from videos.serializers import VideoSerializer, CategoriesSerializer, VideoOTDSerializer
from users.serializers import UserSerializer
from users.models import User
from videos.extentions.videosextentions import VideoExtentions
from videos.models import VideoOTD

videoExtentions = VideoExtentions()

# Create your views here.
class VideoListCreateAPIView(APIView):

    def get(self, request):
        videos = Video.objects.all()
        videos = list(videos)
        videos.reverse()
        videosSerializer = VideoSerializer(videos, many=True)
        return Response(videosSerializer.data)

    def post(self, request):
        data = request.data
        user = User.objects.get(username=data['publishedBy']['username'])
        if user.status == "admin":
            serializer = VideoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
        else:
            return Response({'message' : 'only admins can publish video'})
        return Response(serializer.data)
    
class CategoryAPIView(APIView):
    def get(self, request):
        categories = Categories.objects.all()
        categorySerializer = CategoriesSerializer(categories, many=True)
        return Response(categorySerializer.data)
    
class VideoKeywordsPageAPIView(APIView):


    def get(self, request, keywords, page):
        keywordsSplit = keywords.split('-')
        videosByPage = videoExtentions.GetByPage(page, keywordsSplit)
        videosSerializer = VideoSerializer(videosByPage, many=True)
        return Response(videosSerializer.data)

class VideoDetailAPIView(APIView):
    def get(self, request, pk):
        video = VideoExtentions.GetVideoById(pk)
        videoSerializer = VideoSerializer(video)
        return Response(videoSerializer.data)
    
    def put(self, request, pk):
        info = request.data
        video = request.data
        instance = Video.objects.filter(pk=pk)[0]
        videoUpdate = VideoSerializer(instance, data=info)
        if videoUpdate.is_valid():
            videoUpdate.save()
            return Response({'message' : 'successfully updated'})
        return Response({'message' : 'error'})
    
class UserDetailAPIView(APIView):
    def get(self):
        return Response({'message' : 'bok'})
    def post(self, request):
        data = request.data
        print(data)
        try:
            user = User.objects.get(username = data['username'])
        except:
            return Response({'message' : 'yanlis kullanici adi veya sifre'})
        userSerializer = UserSerializer(user)
        if user.password == data['password']:
            return Response(userSerializer.data)
        else:
            return Response({'message' : 'yanlis kullanici adi veya sifre'})
        
class VideoOTDAPIView(APIView):
    def get(self):
        videos = VideoOTD.objects.all()
        videosSerializer = VideoOTDSerializer(videos, many=True)
        return Response(videosSerializer.data)
        
from django.urls import path

from . import views

urlpatterns = [
    path('allvideos/', views.VideoListCreateAPIView.as_view()),
    path('videos/<str:keywords>/<int:page>/', views.VideoKeywordsPageAPIView.as_view()),
    path('video/<int:pk>/', views.VideoDetailAPIView.as_view()),
    path('categories/', views.CategoryAPIView.as_view()),
    path('user/', views.UserDetailAPIView.as_view()),
]
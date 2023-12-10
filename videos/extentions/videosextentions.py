from ..models import Video

class VideoExtentions:

    @staticmethod
    def GetVideoById(id : int):
        video = Video.objects.get(pk=id)
        return video
    
    def __GetVideosByKeywords(self, keywords : list):
        videos = []
        if keywords[0] == "all":
            videos += Video.objects.all()
            return videos
        for keyword in keywords:
            videos += Video.objects.filter(keywords__name__contains = keyword)
        #videos.reverse()
        return videos
    
    def __VideosCount(self, keywords : list):
        videoDic = {}
        videosByKeywords = self.__GetVideosByKeywords(keywords)
        for video in videosByKeywords:
            try:
                videoDic[video] += 1
            except:
                videoDic[video] = 1
        return videoDic
    
    def __SortDicByValue(self, keywords : list):
        dic = self.__VideosCount(keywords)
        sortedDic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
        finalVideoList = []
        for i in sortedDic:
            finalVideoList.append(i[0])
        return finalVideoList
    
    def GetByPage(self, page : int, keywords : list):
        videos = self.__SortDicByValue(keywords)
        videos.reverse()
        VIDEO_PER_PAGE = 10
        first_index = (page - 1) * VIDEO_PER_PAGE
        last_index = (page) * VIDEO_PER_PAGE
        videoList = videos[first_index : last_index]
        return videoList


    

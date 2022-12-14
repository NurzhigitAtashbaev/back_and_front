from .serializer import NewsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import News


@api_view(['GET'])
def my_api_view(request):
    data = {
        'text': 'Hello world !'
    }
    return Response(data)


@api_view(['GET'])
def news_list_view(request):
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def detail_view(request, id):
    detail_list = News.objects.get(id=id)
    serializer = NewsSerializer(detail_list, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def news_create_view(request):
    serializer = NewsSerializer.get(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({"Created": "Object is created"})


@api_view(['POST'])
def news_update_view(request, id):
    news = News.objects.get(id=id)
    serializer = NewsSerializer(instance=news, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def news_delete_view(request, id):
    news = News.objects.get(id=id)

    news.delete()
    return Response({"obj": "Delete"})

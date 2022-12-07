from rest_framework.viewsets import ViewSet
from applications.posts.models import Post
from applications.posts.serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status


class PostAPIView(ViewSet):
    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
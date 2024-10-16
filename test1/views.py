from .serializers import SnippetSerializer
from .models import Snippet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


@api_view(["GET", "POST"])
def snippet_list(request, format=None): # format for suffixes
    if request.method == "GET":
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET", "PUT", "DELETE"])
def snippet_detail(request, pk, format=None):
    def get_object(pk):
        try:
            return Snippet.objects.get(id=pk)
        except Snippet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        snippet = get_object(pk=pk)
        serializer = SnippetSerializer(request.data, instance=snippet)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        snippet = get_object(pk=pk)
        serializer = SnippetSerializer(data=request.data, instance=snippet)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        snippet = get_object(pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



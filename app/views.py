from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.versioning import URLPathVersioning

from .models import *
from .serializers import *
from rest_framework.reverse import reverse


class ExampleVersioning(URLPathVersioning):
    default_version =  1.0
    allowed_versions = [1.0]
    version_param = '1.0'

class AuthorView(APIView):
    versioning_class = ExampleVersioning
    def get(self, request, pk=None):
        if pk:
            author = get_object_or_404(Author.objects.all(), pk=pk)
            serializer = AuthorSerializer(author)
            return Response({"author": serializer.data})
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True, context={'request': request})
        return Response({"authors": serializer.data})

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def put(self, request, pk):
        saved_author = get_object_or_404(Author.objects.all(), pk=pk)
        serializer = AuthorSerializer(instance=saved_author, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)


    def delete(self, request, pk):
        # Get object with this pk
        author = get_object_or_404(Author.objects.all(), pk=pk)
        author.delete()
        return Response({"message": "Author with id `{}` has been deleted.".format(pk)},status=204)


class ArticleView(APIView):
    versioning_class = ExampleVersioning
    def get(self, request, pk=None):
        if pk:
            article = get_object_or_404(Article.objects.all(), pk=pk)
            serializer = ArticleSerializer(article)
            return Response({"article": serializer.data})
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})

    def post(self, request):
        # data = request.data.get('article')
        # article = get_object_or_404(Article.objects.all())
        # Create an article from the above data
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def put(self, request, pk):
        saved_article = get_object_or_404(Article.objects.all(), pk=pk)
        serializer = ArticleSerializer(instance=saved_article, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)


    def delete(self, request, pk):
        # Get object with this pk
        article = get_object_or_404(Article.objects.all(), pk=pk)
        article.delete()
        return Response({"message": "Article with id `{}` has been deleted.".format(pk)},status=204)
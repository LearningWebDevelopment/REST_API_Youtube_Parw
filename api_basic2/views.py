from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


from .models import Article2
from .serializers import ArticleSerializer2


class ArticleModelViewSet2(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer2
    queryset = Article2.objects.all()
# Create your views here.

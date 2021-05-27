from django.urls import path, include
from .views import ArticleModelViewSet2
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#router.register('article', ArticleViewSet, basename='article')
router.register('article2', ArticleModelViewSet2, basename='article2')

urlpatterns = [
    path('', include(router.urls)),
]
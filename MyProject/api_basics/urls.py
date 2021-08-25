from django.urls import path
from django.urls.conf import include
from .views import ArticleAPIView, GenericAPIView,ArticleViewSet, article_detail, article_list, ArticleDetails
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename = 'article')

urlpatterns = [

    path('viewset/', include(router.urls)),
    #path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    #path('article/<int:pk>/',article_detail),
    #path('article/<int:id>/', APIView.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),
]

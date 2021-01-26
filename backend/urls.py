"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .api.views import index_view
from .api.views import MessageViewSet
from .api.views import QuestionViewSet
from .api.views import ScoreViewSet
from .api.views import UserResponsesViewSet

router = routers.DefaultRouter()
router.register('messages', MessageViewSet)
router.register('questions', QuestionViewSet)
router.register('scores', ScoreViewSet)
router.register('userresponses', UserResponsesViewSet)

urlpatterns = [

    # http://localhost:8000/
    path('', index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),
]

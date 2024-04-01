from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('studentapi', StudentApi.as_view(), basename='studentapi')


urlpatterns = [
     path('', include(router.urls)),
]
from django.contrib import admin
from django.db import router
from django.urls import path, include
from .views import UserViewSet, hello, UserList, UserDetails
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"users-3", UserViewSet)

urlpatterns = [
    path("users/", hello),
    path("users-2/", UserList.as_view()),
    path("users-2/<int:pk>/", UserDetails.as_view()),
    path("", include(router.urls)),
]

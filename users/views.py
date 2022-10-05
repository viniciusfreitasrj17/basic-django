from rest_framework import generics, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer

# 1
@api_view(["GET"])
def hello(response):
  users = User.objects.all()
  serializer = UserSerializer(users, many=True)

  return Response({
    "users": serializer.data
  }, status=202)

# 2
# class UserList(generics.ListAPIView):
class UserList(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

# read, update, delete
class UserDetails(generics.RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

# 3
class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  @action(["GET"], detail=True)
  def email(self, request, pk):
    user = User.objects.get(id=pk)
    return Response(user.email)
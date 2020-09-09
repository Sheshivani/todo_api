from django.http import *
from rest_framework import viewsets
from .serializer import UserSerializer,ToDoSerializer,CommentSerializer, ToDosSerializer
from django.contrib.auth import get_user_model
from .models import ToDoModel,Comment
from rest_framework.permissions import IsAdminUser, IsAuthenticated


User = get_user_model()

class UserRegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(self):
            serializer.save()
            return JsonResponse({'result': 'success', 'message': 'User created Successfully'})
        return JsonResponse({'result': 'error', 'message': 'Failed!!'})

class ToDosModelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ToDosSerializer
    queryset = ToDoModel.objects.all()

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return super().get_queryset().filter(user_id=self.request.user.id)
        return super().get_queryset()

class ToDoModelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = ToDoSerializer
    queryset = ToDoModel.objects.all()

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return super().get_queryset().filter(user_id=self.request.user.id)
        return super().get_queryset()

class Comments(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return super().get_queryset().filter(user_id=self.request.user.id)
        return super().get_queryset()





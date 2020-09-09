from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User,Comment,ToDoModel


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("by", "description")

class ToDosSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = ToDoModel
        fields = ("id", 'user','task_name', 'description', 'is_done','participants', "comments")

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoModel
        fields = ("id", 'user','task_name', 'description', 'is_done','participants', "comments")

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'phone')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, data):
        user = User.objects.create_user(**data)
        return user

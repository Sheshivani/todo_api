from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.UserRegisterView.as_view({'post': 'create'}), name="register_user"),
    path('todo/', views.ToDosModelViewSet.as_view({
        'post': 'create',
        'get': 'list'
    }), name='todos'),
    path('todo/<int:pk>/', views.ToDoModelViewSet.as_view({
        'get': 'retrieve',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='todo'),
    path('comment/', views.Comments.as_view({"get": "list",
                                             'post': 'create',})),
]

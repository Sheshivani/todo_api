from django.contrib import admin
from .models import User,ToDoModel


# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone', 'email')

class ToDoAdmin(admin.ModelAdmin):
    list_display = ('task_name','description','created','is_done')



admin.site.register(User, RegisterAdmin)
admin.site.register(ToDoModel, ToDoAdmin)


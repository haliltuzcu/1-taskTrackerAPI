from rest_framework import ModelViewSet
from .serializers import Todo, TodoSerializer
class TodoView(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
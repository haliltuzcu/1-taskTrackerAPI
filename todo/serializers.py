from rest_framework import serializers
from .models import Todo

class TodoSrializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        # fields = '__all__'
        exclude = []
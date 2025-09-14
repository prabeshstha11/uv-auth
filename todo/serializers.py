from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "user", "title", "description", "completed", "updated_at"]
        read_only_fields = ["id", "user", "created_at", "updated_at"]
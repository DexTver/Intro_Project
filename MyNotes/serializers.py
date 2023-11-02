from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Notes


class NotesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Notes
        fields = ['id', 'title', 'content', 'created', 'owner']


class UserSerializer(serializers.ModelSerializer):
    notes = serializers.PrimaryKeyRelatedField(many=True, queryset=Notes.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'notes']

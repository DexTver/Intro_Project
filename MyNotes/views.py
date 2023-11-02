from django.contrib.auth.models import User
from .models import Notes
from .serializers import NotesSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly

from rest_framework import generics
from rest_framework import permissions


class NotesList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NotesDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

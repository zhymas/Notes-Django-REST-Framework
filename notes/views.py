from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth import logout
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from .serializers import NotesSerializer
from .models import Note

class LinksAPI(APIView):

    def get(self, request):
        endpoints = {
            "home": "http://127.0.0.1:8000/",
            "auth-register-user": "http://127.0.0.1:8000/auth/",
            "get-token": 'http://127.0.0.1:8000/auth/token/',
            "logout-user": 'http://127.0.0.1:8000/auth/logout/',
            "create-note(only for auth user)": 'http://127.0.0.1:8000/api/v1/create_note/',
            "view existing notes(only for auth user)": 'http://127.0.0.1:8000/api/v1/notes/',
            "update note(only for auth user)": 'http://127.0.0.1:8000/api/v1/note/{id_note}',
            "retrieve note(only for auth user)": 'http://127.0.0.1:8000/api/v1/note_retrieve/{id_note}',
            "delete note(only for auth user)": 'http://127.0.0.1:8000/api/v1/note_delete/{id_note}'
        }
        return Response(endpoints)

class Logout(APIView):
    
    def get(self, request, format=None):
        token = Token.objects.get(user=request.user)
        token.delete()
        logout(request)
        return Response({'success': 'user has logout'})

class CreateNotesAPI(CreateAPIView):

    serializer_class = NotesSerializer
    queryset = Note.objects.all()

    def get(self, request):
        return Response({'wrong method': 'must be a method POST'})
    
    def post(self, request):
        data = request.data.copy()
        data['author'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)


class UpdateNotesAPI(UpdateAPIView):
    serializer_class = NotesSerializer
    queryset = Note.objects.all()


class DeleteNotesAPI(DestroyAPIView):
    serializer_class = NotesSerializer
    queryset = Note.objects.all()


class RetriveNotesAPI(RetrieveAPIView):
    serializer_class = NotesSerializer
    
    def get_queryset(self):
        return Note.objects.all()


class ListNotesAPI(ListAPIView):
    serializer_class = NotesSerializer
    queryset = Note.objects.all()

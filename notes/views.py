from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth import logout
from rest_framework.authtoken.models import Token

class LinksAPI(APIView):

    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        endpoints = {
            "home": "http://127.0.0.1:8000/",
            "auth-user": "http://127.0.0.1:8000/api/v1/auth/",
        }
        return Response(endpoints)

class Logout(APIView):
    
    def get(self, request, format=None):
        token = Token.objects.get(user=request.user)
        token.delete()
        logout(request)
        return Response({'success': 'user has logout'})
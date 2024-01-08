from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

class LinksAPI(APIView):
    
    def get(self, request):
        endpoints = {
            "home": "http://127.0.0.1:8000/",
            "test": "http://127.0.0.1:8000/",
        }
        return Response(endpoints)


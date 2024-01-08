from django.urls import path
from .views import LinksAPI


urlpatterns = [
    path('', LinksAPI.as_view())
]
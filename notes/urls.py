from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import LinksAPI, Logout


urlpatterns = [
    path('', LinksAPI.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/token/', obtain_auth_token, name='token'),
    path('auth/logout/', Logout.as_view())
]
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import LinksAPI, Logout, CreateNotesAPI, UpdateAPIView, ListNotesAPI, RetriveNotesAPI, DeleteNotesAPI


urlpatterns = [
    path('', LinksAPI.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/token/', obtain_auth_token, name='token'),
    path('auth/logout/', Logout.as_view()),
    path('api/v1/create_note/', CreateNotesAPI.as_view()),
    path('api/v1/notes/', ListNotesAPI.as_view()),
    path('api/v1/note/<int:pk>', UpdateAPIView.as_view()),
    path('api/v1/note_retrieve/<int:pk>/', RetriveNotesAPI.as_view()),
    path('api/v1/note_delete/<int:pk>', DeleteNotesAPI.as_view())
]
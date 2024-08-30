from django.shortcuts import render
from .models import Posts, Category
from .serializers import PostCreationSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated



class PostCreationView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request, *args, **kwargs):
        
        user_id= request.user.id
        if user_id:
            pass
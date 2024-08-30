from rest_framework.response import Response
from users.helper import token_validator
from .models import Posts, Category
from .serializers import PostCreationSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated



class PostCreationView(APIView):

    def get(self, request, *args, **kwargs):
        is_valid, response = token_validator(request)
        if not is_valid:
            return Response(response, status=400) 
        return super().get(request, *args, **kwargs)
    def get(self,request, *args, **kwargs):
        
        user_id= request.user.id
        if user_id:
            pass
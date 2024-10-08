from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.authentication import generate_tokens_for_user, validate_token
from users.helper import token_validator
from .models import UserInfo
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from .serializers import UserInfoSerializer, UserLoginSerializer
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated



class UserRegistrationView(APIView):
    def post(self,request,*args, **kwargs):
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'User registration Successful'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            tokens = generate_tokens_for_user(user=user)
            return Response({
                'refresh': str(tokens['refresh']),
                'access': str(tokens['access'])
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserListView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        is_valid, response = token_validator(request)
        if not is_valid:
            return Response(response, status=400) 
        return super().get(request, *args, **kwargs)
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

    
    
class UserDetailView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        is_valid, response = token_validator(request)
        if not is_valid:
            return Response(response, status=400) 
        return super().get(request, *args, **kwargs)
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    lookup_field = 'id'
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserInfo
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from .serializers import UserInfoSerializer, UserLoginSerializer
from django.contrib.auth.hashers import check_password



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
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserListView(generics.ListAPIView):

    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

class UserDetailView(generics.RetrieveAPIView):

    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    lookup_field = 'id'
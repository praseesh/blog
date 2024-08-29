from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserInfo
from .serializers import UserInfoSerializer


class UserRegistrationView(APIView):
    def post(self,request,*args, **kwargs):
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'User registration Successful'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserListView(generics.ListAPIView):

    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

class UserDetailView(generics.RetrieveAPIView):

    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    lookup_field = 'id'
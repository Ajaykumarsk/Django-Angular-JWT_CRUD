from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from .models import User
from .serializer import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated] 

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated] 
    queryset = User.objects.all()
    serializer_class = UserSerializer

def helloWorld(HttpRequest):
    return HttpResponse("Hello World")

class LoginView(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username = username,password = password)
        refresh = RefreshToken.for_user(user)
        return JsonResponse({
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        })
class RestricatedView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,format = None):
        return JsonResponse({"response":"YOU ARE ALLOWED"})
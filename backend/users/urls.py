from django.urls import path
from .views import LoginView, RestricatedView, UserList, UserDetail, helloWorld

urlpatterns = [
    path('users/', UserList.as_view(), name="user-list"),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('hello/', helloWorld, name='hello-world'),
    path('login/', LoginView.as_view(), name='login'),
    
    path('restricted/',RestricatedView.as_view(),name='restricted')

] 
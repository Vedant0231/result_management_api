from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


"""we create a api which is used for 
curd opration with jwt authentication.
"""
class Studentlist(viewsets.ModelViewSet):
    
    queryset = Student.objects.all()
    serializer_class= StudentSerializer
    authentication_classes= [JWTAuthentication]
    permission_classes= [IsAuthenticated]


    """this function will make sure that teacher 
    who make student result can see the student info 
    """
    def get_queryset(self):

        user = self.request.user

        return Student.objects.filter(checkby= user)


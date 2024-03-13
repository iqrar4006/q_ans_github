from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from .serializers import ValidateQuestionSerializer


# Create your views here.
class HomeView(APIView):
    def get(self,request,format=None):
        return HttpResponse('Home page')

class ValidateQuestionView(APIView):
    def get(self,request,format=None):
        serializer = ValidateQuestionSerializer(data=request.data)
        if serializer.is_valid():
            question_text = serializer.validated_data['question']
            options = serializer.validated_data['options']
            answer = serializer.validated_data['answer']
            if answer in options:
                return Response({'msg':f"You have selected the correct option {answer}"})
            else:
                return Response({'msg':f"You have selected the incorrect option {answer}"})
        return Response(serializer.errors, status=400)



from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from .serializers import ValidateQuestionSerializer
from rest_framework.permissions import IsAuthenticated



# Create your views here.
class HomeView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        return HttpResponse('Home page')

class ValidateQuestionView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serializer = ValidateQuestionSerializer(data=request.data)
        if serializer.is_valid():
            question_text = serializer.validated_data['question']
            options = serializer.validated_data['options']
            answer = serializer.validated_data['answer']
            if answer in options:
                return Response({"correct":True,"question":question_text,"options":options,"answer":answer})
            else:
                return Response({"correct":False,"question":question_text,"options":options,"answer":answer})
        return Response(serializer.errors, status=400)



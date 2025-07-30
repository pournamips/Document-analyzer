# analyzer/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TextInputSerializer
from .utils import analyze_with_ai
from django.shortcuts import render

def index(request):
    return render(request, 'analyzer/index.html')

class AnalyzeText(APIView):
    def post(self, request):
        serializer = TextInputSerializer(data=request.data)
        if serializer.is_valid():
            input_text = serializer.validated_data['text']
            ai_feedback = analyze_with_ai(input_text)
            return Response({"ai_feedback": ai_feedback})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

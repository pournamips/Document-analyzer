# analyzer/urls.py
from django.urls import path
from .views import AnalyzeText, index

urlpatterns = [
    path('', index, name='home'),

    path('analyze/', AnalyzeText.as_view(), name='analyze-text'),
]

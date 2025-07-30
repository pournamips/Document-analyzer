# legal_doc_analyzer/urls.py
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('', include('analyzer.urls')),  # 👈 mounts analyzer at root

]

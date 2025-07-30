from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Legal Document Analyzer API</h1><p>Use <code>/api/analyze/</code> to POST text for analysis.</p>")

from django.conf import settings

def project_language(request):
    return {"LANGUAGES": settings.LANGUAGES}
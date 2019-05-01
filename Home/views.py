from django.http import HttpResponse


def aboutUs(request):
    return HttpResponse("This will be the about us page")

from django.http import HttpResponse


def index(request):
    html = "<html><body><h1> API UP AND RUNNING - PFE </h1></body></html>"
    return HttpResponse(html)

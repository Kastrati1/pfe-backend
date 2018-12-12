from django.http import HttpResponse

import os

from boto.s3.connection import S3Connection
s3 = S3Connection(os.environ['S3_KEY'], os.environ['S3_SECRET'])


def index(request):
    html = "<html><body><h1> API UP AND RUNNING - PFE" + os.environ['ENV'] + " </h1></body></html>"
    return HttpResponse(html)

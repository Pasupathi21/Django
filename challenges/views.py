from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def testView(request):
    # print(request)
    return HttpResponse({
        "message": 'Working 👍',
        # "requestObj": request
    })

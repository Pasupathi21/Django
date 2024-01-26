from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError, HttpResponseRedirect

# 'reverse' this fn will help to redirect the url with 'name' and 'arg' 
from django.urls import reverse

list_item = [
    'apple',
    'orange'
]
# Create your views here.
def testView(request):
    # print(request)
    return HttpResponse({
        "message": 'Working 👍',
        # "requestObj": request
    })


def list(request):
    try:
        return HttpResponse(list_item)
    except e as error:
        return HttpResponseServerError(error)

def add(request, add_item):
    print('add_item >>>>>', add_item)
    try:
        list_item.append(add_item)
        return HttpResponse(list_item)
    except e :
        return HttpResponseNotFound(e)

def update(request, id, value):
    try:
        list_item[id] = value
        return HttpResponse(list_item)
    except e as error:
        return HttpResponseServerError(error)

def delete(request, id):
    try:
        list_item.remove(id)
        return HttpResponse(list_item)
    except (ValueError, TypeError, ZeroDivisionError) as Error:
        # Here we to redirect the request
        redirect_url = reverse('message_alert', args=[f'''{id} given value is not found'''])
        print('Redirect URL >>>>>>>>>>>>', redirect_url)
        return HttpResponseRedirect(redirect_url)
         
    
def message(request, message_str):
    try:
        alert_templete = f'''
    <div style="display: flex; align-item: center; justify-content: center"> 
        <h2>{message_str}</h2
    </div>
    '''
        return HttpResponse(alert_templete)
    except (TypeError, ValueError) as Error:
        return HttpResponseServerError(Error)
    
def showIndex(request):
    try:
        return render(request, 'challenges/test.html', {'test_text': 'Hi'})
    except (TypeError, ValueError) as Error:
        return HttpResponseServerError(Error)
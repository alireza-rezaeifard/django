
from django.http import HttpResponse,JsonResponse

def http_test(requests) :
    return HttpResponse('<h1>http test succecfully</h1>')

def json_test(requsts) : 
    return JsonResponse({'name' : 'ali'})
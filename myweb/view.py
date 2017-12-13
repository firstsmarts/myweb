from django.http import HttpResponse
import json
def index(request):
    resp = {'errorcode': 1, 'name': 'ck'}
    return HttpResponse(json.dumps(resp),content_type="application/json")
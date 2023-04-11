from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def getsymptoms(req):
    if(req.method=='POST'):
        print(req)
        # i = req.POST.get('queryResult')
        # par = i['parameters']
        # for k,v in par.items():
        #   if k=='person':
        #     person = par[k]['name']
        #   elif k=='Feeling':
        #     Feeling = par['Feeling']
        #   elif k=='Symptoms':
        #     Symptoms = par['Symptoms']
        # print(Feeling, person, Symptoms)
        return JsonResponse({
  "fulfillmentMessages": [
    {
      "text": {
        "text": [
          "Don't worry bro here are the steps you need to take"
        ]
      }
    }
  ]
})
    return HttpResponse('Hello')
        
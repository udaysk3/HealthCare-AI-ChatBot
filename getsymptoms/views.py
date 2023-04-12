from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

def getsymptoms(req):
    if req=='POST':
        return JsonResponse(
            {
                    "fulfillmentMessages": [
                        {
                        "text": {
                            "text": [
                            "Text response from webhook"
                            ]
                        }
                        }
                    ]
            }   
        )
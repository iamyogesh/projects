from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    
    latest = Question.objects.order_by('-pub_date')[:5]
    output = ','.join([p.question_text for p in latest])
    return HttpResponse(output)
    
def results(request, question_id):
    return HttpResponse("you are looking at the result of %s question" %question_id)
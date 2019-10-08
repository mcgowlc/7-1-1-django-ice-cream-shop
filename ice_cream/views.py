from django.shortcuts import render
rom django.http import HttpResponse

def index(request):
    # return HttpResponse('Hello, World')
    question_list = Question.objects.all()
    # output = '<br/>'.join([q.question_text for q in question_list])
    context = {
    'question_list': question_list
    }

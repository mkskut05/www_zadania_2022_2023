from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question

# Create your views here.
def question_list(request):
    questions = Question.objects.order_by('-question_text')
    filtered = questions.filter(pk=1)
    return render(request, 'jakis_polls/question_list.html', {'questions': filtered})

def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'jakis_polls/question_list.html', {'question': question})
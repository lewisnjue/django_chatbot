from django.shortcuts import render
import openai
from django.conf import settings
from openai import OpenAI
from django.http import JsonResponse
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai
# Create your views here.

OPENAI_API_KEY = settings.OPENAI_API_KEY
from openai import OpenAI


client = OpenAI()
def home(request):
    return render(request, 'home.html')



@csrf_exempt
def chatbot_response(request):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
    )

    print(completion.choices[0].message)
    return JsonResponse({'response': completion.choices[0].message['content']})
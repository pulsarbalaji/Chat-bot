from django.shortcuts import render
from django.http import JsonResponse
from core.reply_factory import generate_bot_responses
# Create your views here.


def chat(request):
    if not request.session.session_key:
        request.session.create()

    return render(request, 'chat.html')

def quiz_view(request):
    user_message = request.GET.get("msg", "")
    responses = generate_bot_responses(user_message, request.session)
    return JsonResponse({"bot_responses": responses})

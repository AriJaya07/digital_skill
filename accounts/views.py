from django.http import HttpResponse

def user_list(request):
    return HttpResponse("Hello, world. You're at the accounts index.")
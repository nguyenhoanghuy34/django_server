from django.http import HttpResponse

def home(request):
    return HttpResponse("Trang chủ nè.")

from django.http import HttpResponse

def index(request): 
	return HttpResponse("<h2>Hello world<h2>")
def test(request): 
	return HttpResponse("test")
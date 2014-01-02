from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango says hello world!<p><a href='/rango/about'>About Page</a></p>")
	
def about(request):
	return HttpResponse("Rango Says: Here is the about page.<p><a href='/rango'>Main Page</a></p>")
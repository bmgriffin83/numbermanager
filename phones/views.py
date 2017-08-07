from django.shortcuts import render
def detail (request, extension);
	return HttpResponse("You're looking at extension %s." % extension)

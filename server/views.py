from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from django.http import Http404
import urllib.request, urllib.error
from django.http import HttpResponse, HttpResponseNotFound, Http404

from server import common_utils



def index(request):
	pageExists = True
	# status_code_2 = urllib.request.urlopen("http://10.235.21.28:8282/CrestaL2/login/?next=/CrestaL2/").getcode()
	# status_code_3 = urllib.request.urlopen("http://10.235.21.28:8282/CrestaL2/login/?next=/CrestaL2/").getcode()
	# status_code_4 = urllib.request.urlopen("http://10.235.21.27:6611/CrestaL2/login/?next=/CrestaL2/").getcode()
	# status_code_5 = urllib.request.urlopen("http://10.235.21.27:8181/CrestaL2/").getcode()
	# status_code_6 = urllib.request.urlopen("http://10.235.21.27:2323/AITestEngine/login/?next=/AITestEngine/").getcode()
	# status_code_7 = urllib.request.urlopen("http://10.235.21.27:8181/CrestaL2/").getcode()
	# status_code_8 = urllib.request.urlopen("http://10.235.21.28:9292/AITestEngine/login/?next=/AITestEngine/").getcode()
	# status_code_9 = urllib.request.urlopen("https://10.235.21.28/AITestEngine//").getcode()
	# status_code_10 = urllib.request.urlopen("http://10.235.21.27:8181/CrestaL2/").getcode()

	status_code_1=urllib.request.urlopen("http://10.235.21.28:2828/AITestEngine/login/?next=/AITestEngine/").getcode()


	if(status_code_1 != 200):
		pageExists = False

	# if(status_code_2 != 200):
	# 	pageExists = False 

	# if(status_code_3 != 200):
	# 		pageExists = False

	# if(status_code_4 != 200):
	# 	pageExists = False

	# if(status_code_5 != 200):
	# 	pageExists = False

	# if(status_code_6 != 200):
	# 		pageExists = False

	# if(status_code_7 != 200):
	# 	pageExists = False 

	# if(status_code_8 != 200):
	# 		pageExists = False

	# if(status_code_9 != 200):
	# 	pageExists = False

	# if(status_code_10 != 200):
	# 	pageExists = False 

	context = {
		'pageExists': pageExists
	}



	return render(request, 'server/display.html', context)








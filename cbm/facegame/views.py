from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import scores, level1_happy, level1_else, level2_happy, level2_else, level3_else, level3_happy
from random import random
import json
from django.conf import settings
# from django.utils import json
from django.contrib.staticfiles.templatetags.staticfiles import static
# Create your views here.
def index(request):
	# template_name = "facegame/index.html"
	# context_object_name = "user_data"
	return HttpResponse("Hello, world. You're at the game index.")
	# def get_queryset(self):
	# 	return scores.objects.filter()\

def game(request, user_id):
	template_name = "facegame/index.html"
	context_object_name = "user_data"

		#call images from level1 happy and else
	context = {"user_data" : scores.objects.get(id=user_id)}
	response = "Hey you are user "+user_id
	# happy, sad, neutral, others contain urls of respective dirs
	# some_data = [ ( "Happy",  ), ("Sad", (1.2,1.3)) ]
	return render(request, 'facegame/game.html', context)
	# def get_queryset(self):
	# 	return scores.objects.filter()

# def view(request, …):
#     js_data = simplejson.dumps(my_dict)
#     …
#     render_template_to_response("my_template.html", {"my_data": js_data, …})

def getimages(request):
	if request.method == 'GET' :
		level = request.GET['user_level']
		# i = random() * 4

		image_data = []
		if(level=='1'):
			happy = level1_happy.objects.count()
			image1 = int(random()*happy) + 1
			helse = level1_else.objects.count()
			image2 = int(random()*helse) + 1
			helse = helse - 1
			rand1 = int(random()*helse) + 1
			image3 = rand1 if rand1 < image2 else rand1+1
			helse = helse - 1
			rand1 = int(random()*helse) + 1
			image4 = rand1 if rand1 < image2 else rand1+1
			image4 = image4 if image4 < image3 else image4+1
			# image_data[1] = level1_happy.objects.get(pk=image1).happyphoto.url
			# image_data[2] = level1_else.objects.get(pk=image2).elsephoto.url
			# image_data[3] = level1_else.objects.get(pk=image3).elsephoto.url
			# image_data[4] = level1_else.objects.get(pk=image4).elsephoto.url
			# image_data[5] = settings.MEDIA_ROOT 
			image_data.append(level1_happy.objects.get(pk=image1).happyphoto.url)
			image_data.append(level1_else.objects.get(pk=image2).elsephoto.url)
			image_data.append(level1_else.objects.get(pk=image3).elsephoto.url)
			image_data.append(level1_else.objects.get(pk=image4).elsephoto.url)
			image_data.append(settings.MEDIA_ROOT)
		elif(level=='2'):
			happy = level2_happy.objects.count()
			image1 = int(random()*happy) + 1
			helse = level2_else.objects.count()
			image2 = int(random()*helse) + 1
			helse = helse - 1
			rand1 = int(random()*helse) + 1
			image3 = rand1 if rand1 < image2 else rand1+1
			helse = helse - 1
			rand1 = int(random()*helse) + 1
			image4 = rand1 if rand1 < image2 else rand1+1
			image4 = image4 if image4 < image3 else image4+1
			image_data[1] = level2_happy.objects.get(pk=image1).happyphoto.url
			image_data[2] = level2_else.objects.get(pk=image2).elsephoto.url
			image_data[3] = level2_else.objects.get(pk=image3).elsephoto.url
			image_data[4] = level2_else.objects.get(pk=image4).elsephoto.url
			image_data[5] = settings.MEDIA_ROOT 
		else:
			happy = level3_happy.objects.count()
			image1 = int(random()*happy) + 1
			helse = level3_else.objects.count()
			image2 = int(random()*helse) + 1
			helse = helse - 1
			rand1 = int(random()*helse) + 1
			image3 = rand1 if rand1 < image2 else rand1+1
			helse = helse - 1
			rand1 = int(random()*helse) + 1
			image4 = rand1 if rand1 < image2 else rand1+1
			image4 = image4 if image4 < image3 else image4+1
			image_data[1] = level3_happy.objects.get(pk=image1).happyphoto.url
			image_data[2] = level3_else.objects.get(pk=image2).elsephoto.url
			image_data[3] = level3_else.objects.get(pk=image3).elsephoto.url
			image_data[4] = level3_else.objects.get(pk=image4).elsephoto.url
			image_data[5] = settings.MEDIA_ROOT 

		return HttpResponse(json.dumps(image_data), content_type='application/json')



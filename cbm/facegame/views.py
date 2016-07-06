from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import scores, level1_happy, level1_else, level2_happy, level2_else, level3_else, level3_happy
from random import random
import json
from django.conf import settings
from django.utils import timezone
import datetime
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

	return render(request, 'facegame/game.html', context)

def getimages(request):
	if request.method == 'GET' :
		level = request.GET['user_level']

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
			image_data.append(level1_happy.objects.get(pk=image1).happyphoto.url)
			image_data.append(level1_else.objects.get(pk=image2).elsephoto.url)
			image_data.append(level1_else.objects.get(pk=image3).elsephoto.url)
			image_data.append(level1_else.objects.get(pk=image4).elsephoto.url)

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
			image_data.append(level2_happy.objects.get(pk=image1).happyphoto.url)
			image_data.append(level2_else.objects.get(pk=image2).elsephoto.url)
			image_data.append(level2_else.objects.get(pk=image3).elsephoto.url)
			image_data.append(level2_else.objects.get(pk=image4).elsephoto.url)

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
			image_data.append(level3_happy.objects.get(pk=image1).happyphoto.url)
			image_data.append(level3_else.objects.get(pk=image2).elsephoto.url)
			image_data.append(level3_else.objects.get(pk=image3).elsephoto.url)
			image_data.append(level3_else.objects.get(pk=image4).elsephoto.url)

		return HttpResponse(json.dumps(image_data), content_type='application/json')

def sendinfo(request):
	if request.method == 'POST':
		level = request.POST.get('user_level', '')
		score = request.POST.get('user_score', '')
		user_id = request.POST.get('user_id', '') #user id will probably be assigned through session management but here for experimental purpose is sent through ajax
		try:
			user_scores = scores.objects.get(pk = user_id)
			user_scores.score = score
			user_scores.level = level
			user_scores.last_played = timezone.now()
			user_scores.save()
			data = 0;
			return HttpResponse(json.dumps(data), content_type='application/json')
		except:
			data = 1;
			return HttpResponse(json.dumps(data), content_type='application/json')

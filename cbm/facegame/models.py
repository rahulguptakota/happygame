from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
import datetime

# Create your models here.
class scores(models.Model):
	def __str__(self):
		return self.username
	# user = models.ForeignKey(settings.AUTH_USER_MODEL)
	username = models.CharField(max_length=25) #username should be a foreign key derived from some central db you have
	score = models.IntegerField(default=0)
	level = models.IntegerField(default=0)
	last_played = models.DateTimeField('date published')

class level1_happy(models.Model):
	happyphoto = models.ImageField(upload_to='cbmimages/level1_images/happy')

class level2_happy(models.Model):
	happyphoto = models.ImageField(upload_to='cbmimages/level2_images/happy')

class level3_happy(models.Model):
	happyphoto = models.ImageField(upload_to='cbmimages/level3_images/happy')

class level1_else(models.Model):
	elsephoto = models.ImageField(upload_to='cbmimages/level1_images/else', blank=True, null=True)

class level2_else(models.Model):
	elsephoto = models.ImageField(upload_to='cbmimages/level2_images/else', blank=True, null=True)

class level3_else(models.Model):
	elsephoto = models.ImageField(upload_to='cbmimages/level3_images/else', blank=True, null=True)

# class Choice(models.Model):
#     question = models.ForeignKey(Question)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
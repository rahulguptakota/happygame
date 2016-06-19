from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
import datetime

# Create your models here.
class scores(models.Model):
	def __str__(self):
		return self.username
	# user = models.ForeignKey(settings.AUTH_USER_MODEL)
	username = models.CharField(max_length=25)
	score = models.IntegerField(default=0)
	level = models.IntegerField(default=0)
	last_played = models.DateTimeField('date published')

# class Choice(models.Model):
#     question = models.ForeignKey(Question)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
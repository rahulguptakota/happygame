from django.shortcuts import render

# Create your views here.
def gamestart(request, userid):
	template_name = "facegame/index.html"
	context_object_name = "user_data"
	def get_queryset(self):
		return scores.objects.filter()
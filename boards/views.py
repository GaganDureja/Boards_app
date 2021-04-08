from django.shortcuts import render

from .models import Board

# Create your views here.
from django.http import HttpResponse, Http404

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})




def board_topics(request, pk):

	try:
		board = Board.objects.get(pk=pk)
	except Board.DoesNotExist:
		raise Http404

	return render(request, 'topics.html', {'board': board})
from django.http import HttpResponse
from polls.models import Choice,Poll
from django.template import RequestContext, loader
from django.shortcuts import render
from django.shortcuts import *
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from polls.models import Choice, Poll
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from polls.serializers import UserSerializer, GroupSerializer
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from polls.models import Choice, Poll
from polls.forms import UploadFileForm

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from polls.models import Poll
from polls.models import ImageModel
from polls.serializers import PollSerializer, PollModelSerializer
from taggit.models import TagBase
from taggit.models import Tag

#Searching the images based on the tag
@csrf_exempt
def search_images(request):
	tag_selected_id = request.POST['tag_list']
	tags = Tag.objects.all()
	images = []
	if tag_selected_id == "-1":
		images = ImageModel.objects.all()
	else:
		images = ImageModel.objects.filter(tags__id=tag_selected_id)
	return render_to_response('polls/list_images.html',{'list_images':images, 'list_tags':tags, 'tag_selected_id':int(tag_selected_id)})	



#Listing the images
@csrf_exempt
def list_images(request):
	tags = ImageModel.tags.all()
	images = ImageModel.objects.all()
	return render_to_response('polls/list_images.html',{'list_images':images, 'list_tags':tags})



#Upload file
@csrf_exempt
def upload_file(request):
    if request.method == 'POST':

        image = ImageModel(imageField = request.FILES['file'])
        str_tags = request.POST['tags']
        list_tags = str_tags.split(",")
        tags = Tag.objects.all()
        
        image.save()
        for each_tag in list_tags:
        	image.tags.add(each_tag)
        #image.tags.add(tag)
        image.save()
        #handle_uploaded_file(request.FILES['file'])
        return HttpResponseRedirect('/polls/upload_form/')
    
    else:
        form = UploadFileForm()
    return render_to_response('polls/upload.html', {'form': form})








######################################IGNORE THE BELOW CODE. Its not related to the tags#####################


@csrf_exempt
def poll_rest_list(request):
	if request.method == 'GET':
		polls = Poll.objects.all()
		serializer = PollModelSerializer(polls, many=True)
		return JSONResponse(serializer.data)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		poll = PollModelSerializer(data=data)
		if poll.is_valid():
			poll.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, status=400)




class JSONResponse(HttpResponse):
    
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)



class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    
	queryset = Group.objects.all()
	serializer_class = GroupSerializer




class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_poll_list'

	def get_queryset(self):
	#"""Return the last five published polls."""
		return Poll.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
	model = Poll
	template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
	model = Poll
	template_name = 'polls/results.html'



def results(request, poll_id):
	poll = get_object_or_404(Poll, pk=poll_id)
	return render(request, 'polls/results.html', {'poll': poll})
# ...
def vote(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the poll voting form.
		return render(request, 'polls/detail.html', {
			'poll': p,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('results', args=(p.id,)))

def index(request):
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = RequestContext(request, {
		'latest_poll_list': latest_poll_list,
	})
	return HttpResponse(template.render(context))
    #return HttpResponse("Hello, world. You're at the poll index.")
# Create your views here.
def detail(request, poll_id):
	try:
		poll = Poll.objects.get(pk=poll_id)
	except Poll.DoesNotExist:
		raise Http404
	return render(request, 'polls/detail.html', {'poll': poll})
    #return HttpResponse("You're looking at poll %s." % poll_id)

#def results(request, poll_id):
 #   return HttpResponse("You're looking at the results of poll %s." % poll_id)

#def vote(request, poll_id):
    #return HttpResponse("You're voting on poll %s." % poll_id)
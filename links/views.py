from django.shortcuts import render,render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .forms import LinkForm
# Create your views here.
def add_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(".")
    else:
        form = LinkForm()
    return render_to_response('add_link.html', {'form': form}, context_instance=RequestContext(request))
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Contact, Members, Reviews
from django.urls import reverse
# Create your views here.
def index(request):
  mymembers = Members.objects.all().values()
  rev=Reviews.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
    'rev':rev,
  }
  return HttpResponse(template.render(context, request))
def addrecord(request):
  name = request.POST['name']
  email = request.POST['email']
  country = request.POST['country']
  subject = request.POST['subject']
  member = Contact(name=name,email=email,country=country,subject=subject)
  member.save()
  return HttpResponseRedirect(reverse('index'))
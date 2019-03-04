from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .models import BlogModel
# Create your views here.



# index views

def index(requrest):
    return render(requrest, 'd_a_app/index.html')


# view for all entries page

@login_required
def allBlogEntries(request):
    allEntries = BlogModel.objects.all()
    context = {'allEntries': allEntries}
    return render(request, 'd_a_app/allBlogEntries.html', context)

# views for user logged in entries

@login_required
def yourEntries(request):
    urEntries = BlogModel.objects.filter(blogAuthor=request.user)
    context = {'yourEntries': urEntries}
    return render(request, 'd_a_app/yourentries.html',context)


















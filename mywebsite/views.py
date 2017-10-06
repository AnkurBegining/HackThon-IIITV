from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def firstPage(request):
    return render(request, 'mywebsite/firstPage.html', {})
@login_required
def view_profile(request):
    args = {'user': request.user}
    return render(request, 'mywebsite/firstPage.html', args)
from django.shortcuts import render, redirect, get_object_or_404
from .models import Bug
from .forms import BugRegistrationForm

def index(request):
    return render(request, "Hello, world! You are in  Paula Ukerun's Homepage 🤗")  


def register_bug(request):
    if request.method == 'POST':
        form = BugRegistrationForm(request.POST)
        if form.is_valid():
            bug = form.save()
            return redirect('view_bug', bug_id=bug.pk)  # Redirect to the view_bug page for the newly registered bug
    else:
        form = BugRegistrationForm()
    
    return render(request, 'register_bug.html', {'form': form})

def view_bug(request, bug_id):
    bug = get_object_or_404(Bug, pk=bug_id)
    return render(request, 'view_bug.html', {'bug': bug})

def list_bug(request):
    bugs = Bug.objects.all()
    return render(request, 'list_bug.html', {'bugs': bugs})

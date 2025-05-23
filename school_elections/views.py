from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Candidate, Vote
from .forms import VoteForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError
from django.contrib import messages
from collections import defaultdict
from django.utils.text import slugify



def user_login(request):
    
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return render (request, 'school_elections/dashboard.html',{'success':'Login successfully!'})
        else:
            return render (request, 'school_elections/login.html',{'error':'Invalid Credentials !'})


    return render (request, 'school_elections/login.html')
        
  
def user_logout(request):
    logout(request)
    
    return redirect('login')
  
        
@login_required
def dashboard(request):
        
    return render(request, 'school_elections/dashboard.html')

# @login_required
# def vote_view(request):
#     if Vote.objects.filter(voter=request.user).exists():
#         return render(request, 'school_elections/vote.html', {'voted': True})

#     if request.method == 'POST':
#         form = VoteForm(request.POST)
#         if form.is_valid():
#             for position, candidate in form.cleaned_data.items():
#                 Vote.objects.create(voter=request.user, candidate=candidate)
#             return redirect('results')
#     else:
#         form = VoteForm()

#     candidates = Candidate.objects.all()
#     return render(request, 'school_elections/vote.html', {'form': form, 'voted': False, 'candidates': candidates})





@login_required
def vote_view(request):
    if Vote.objects.filter(voter=request.user).exists():
        return render(request, 'school_elections/vote.html', {'voted': True})

    grouped = defaultdict(list)
    for candidate in Candidate.objects.all():
        grouped[candidate.get_position_display()].append(candidate)

    return render(request, 'school_elections/vote.html', {
        'voted': False,
        'grouped_candidates': dict(grouped)
    })

@login_required
def results_view(request):
    positions = dict(Candidate.POSITION_CHOICES)
    results = {}
    for key in positions:
        candidates = Candidate.objects.filter(position=key)
        results[positions[key]] = [(c.name, 
                                    Vote.objects.filter(candidate=c).count()) for c in candidates]
        
    print("RESULTS:", results)
    return render(request, 'school_elections/results.html', {'results':results})


        
    
    
    

from django.shortcuts import render, redirect
from market.models import Listing
from .forms import SignUpForm
from .models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    listings = Listing.objects.filter(is_sold=False)[0:8]
    context = {
        'listings': listings
    }
    return render(request, 'home.html', context)

def sign_up(request):
    form = SignUpForm

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            return redirect('home')
        
    return render(request, 'signup.html', {'form':form})

@login_required
def profile(request):
    listings = Listing.objects.filter(created_by=request.user)
    no_listings = User.objects.filter(pk=request.user.pk).annotate(num_listings=Count("listings"))
    no_listings = no_listings[0].num_listings
    page = request.GET.get('page', 1)
    paginator = Paginator(listings, 8)
    try:
        listings = paginator.page(page)
    except PageNotAnInteger:
        listings = paginator.page(1)
    except EmptyPage:
        listings = paginator.page(paginator.num_pages)

        print(listings.has_other_pages)

    context = {
        'listings': listings,
        'no_listings': no_listings
        }

    return render(request, 'profile.html', context)

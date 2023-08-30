from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Listing
from django.contrib.auth.decorators import login_required
from .forms import SellForm, UpdateSellForm
from .decorators import owner_verifier
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def search(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        listings = Listing.objects.filter(is_sold=False, name__contains=query)
        num_listings = listings.count()
        if query:
            page = request.GET.get('page', 1)
            paginator = Paginator(listings, 8)
            try:
                listings = paginator.page(page)
            except PageNotAnInteger:
                listings = paginator.page(1)
            except EmptyPage:
                listings = paginator.page(paginator.num_pages)

    context = {
        'query': query,
        'listings': listings,
        'num_listings': num_listings
    }

    return render(request, 'search.html', context)

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    listings = Listing.objects.filter(category=category, is_sold=False)
    page = request.GET.get('page', 1)
    paginator = Paginator(listings, 8)
    try:
        listings = paginator.page(page)
    except PageNotAnInteger:
        listings = paginator.page(1)
    except EmptyPage:
        listings = paginator.page(paginator.num_pages)

    context = {
        'listings': listings,
        'category': category
    }

    return render(request, 'category.html', context)


def list_detail(request, slug):
    list = get_object_or_404(Listing, slug=slug)
    similar = Listing.objects.exclude(slug=slug).filter(category=list.category, is_sold=False)[:8]

    context = {
        'list': list,
        'similar': similar
    }

    return render(request, 'detail.html', context)


@login_required
def sell(request):
    form = SellForm

    if request.method == 'POST':
        form = SellForm(request.POST, request.FILES)

        if form.is_valid():
            listing = form.save(commit=False)
            listing.created_by = request.user
            listing.save()

            return redirect('list_detail', listing.slug)
        
    context ={
        'form': form,
        'action': 'Sell'
    }
        
    return render(request, 'sell.html', context)

@login_required
@owner_verifier
def update_sell(request, slug):
    listing = get_object_or_404(Listing, slug=slug)
    form = UpdateSellForm(instance=listing)

    if request.method == 'POST':
        form = UpdateSellForm(request.POST, request.FILES, instance=listing)

        if form.is_valid():
            listing.save()

            return redirect('list_detail', listing.slug)
        
    context ={
        'form': form,
        'action': 'Update'
    }
        
    return render(request, 'sell.html', context)


@login_required
@owner_verifier
def delete_sell(request, slug):
    listing = get_object_or_404(Listing, slug=slug)
    listing.delete()
    
    return redirect('home')
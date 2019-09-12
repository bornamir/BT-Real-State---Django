from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .choices import *

from .models import Listing

# Create your views here.
def index(req):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings,3)
    page = req.GET.get('page')
    paged_listing = paginator.get_page(page)
    context = {
        'listings' : paged_listing
    }
    return render(req, 'listings/listings.html', context)

def listing(req, listing_id ):
    listing = get_object_or_404(Listing, pk=listing_id)
    
    optional_photos = Listing.objects.filter(pk = listing_id).values('photo_1','photo_2','photo_3','photo_4')
    #optional_photos = Listing.objects.raw( 'SELECT photo_1, photo_2 FROM listings_listing')

    context = {
        'listing': listing,
        'optional_photos' : optional_photos
     }
    return render(req, 'listings/listing.html', context)

def search(req):
    # Creating a query set list from search items:
    queryset = Listing.objects.order_by('-list_date')
    # Searching for keywords:
    if 'keywords' in req.GET:
        keywords = req.GET['keywords']
        if keywords :
            # icontatins searchs for keywords within a description.
            queryset = queryset.filter(description__icontains=keywords)
    # Searching for City:
    if 'city' in req.GET:
        city = req.GET['city']
        if city:
            queryset = queryset.filter(city__iexact=city)
    # Searching for State:
    if 'state' in req.GET:
        state = req.GET['state']
        if state:
            queryset = queryset.filter(state__iexact=state)

    # Searching for bedrooms:
    if 'bedrooms' in req.GET:
        bedrooms = req.GET['bedrooms']
        if bedrooms:
            queryset = queryset.filter(bedrooms__lte=bedrooms)
    # Searching for price:
    if 'price' in req.GET:
        price = req.GET['price']
        if price:
            queryset = queryset.filter(price__lte = price)

    context = {
        'state_choices' : state_choices,
        'bedroom_choices' : bedroom_choices,
        'price_choices' : price_choices,
        'listings' : queryset,
        'values' : req.GET
        }
    return render(req, 'listings/search.html',context) 
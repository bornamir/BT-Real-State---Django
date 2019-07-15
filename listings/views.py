from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
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
    return render(req, 'listings/search.html') 
from django.shortcuts import render
from secrets import ACCESS_KEY, SECRET_KEY, ASSOC_ID
from amazon.api import AmazonAPI
# Create your views here.
def search(request):
    if request.method == 'POST':
        searchvalue = request.POST.get('searchbox', '')
        amazon = AmazonAPI(ACCESS_KEY, SECRET_KEY, ASSOC_ID)
        products = amazon.search(Keywords=searchvalue, SearchIndex='All')
        context = {
            'search': searchvalue,
            'products': products
        }
    else:
        context = {}
    return render(request, 'azsearch/search.html', context)


# Default home page given that this was the first app built
def home(request):
    context = {
        'titlecontext': 'Giftpier Home',
        'bodycontext': 'Splash page goes here'
    }
    return render(request, 'azsearch/generic.html', context)
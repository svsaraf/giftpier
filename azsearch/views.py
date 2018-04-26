from django.shortcuts import render
from secrets import ACCESS_KEY, SECRET_KEY, ASSOC_ID
from amazon.api import AmazonAPI
from azsearch.models import Gift
# Create your views here.
def search(request):
    if request.method == 'POST':
        searchvalue = request.POST.get('searchbox', '')
        saved_or_not = request.POST.get('saved_or_not', '')
        amazon = AmazonAPI(ACCESS_KEY, SECRET_KEY, ASSOC_ID)
        products = amazon.search_n(20, Keywords=searchvalue, SearchIndex='All')
        context = {
            'search': searchvalue,
            'products': products
        }
        if saved_or_not == 'saved':
            for product in products:
                if product.title and product.offer_url and product.large_image_url and product.formatted_price and product.price_and_currency:
                    gift = Gift(name=product.title, link=product.offer_url, image_link=product.large_image_url, price_desc=product.formatted_price, price=product.price_and_currency[0])
                    gift.save()

    else:
        context = {}
    return render(request, 'azsearch/search.html', context)


# Default home page given that this was the first app built
def home(request):
    gifts = Gift.objects.raw('SELECT * from azsearch_gift limit 20')
    context = {
        'titlecontext': 'Giftpier Home',
        'bodycontext': '',
        'gifts': gifts
    }
    return render(request, 'azsearch/generic.html', context)
from django.shortcuts import render
from secrets import ACCESS_KEY, SECRET_KEY, ASSOC_ID
from amazon.api import AmazonAPI
from azsearch.models import Gift
from django.http import HttpResponse
import json
# Create your views here.

def createCart(products):
    pdict = {}
    for item in products:
        if item in pdict:
            pdict[item] = pdict[item] + 1
        else:
            pdict[item] = 1
    amazon = AmazonAPI(ACCESS_KEY, SECRET_KEY, ASSOC_ID)
    for index, key in enumerate(pdict.items()):
        product = amazon.lookup(ItemId=key[0])
        item = {'offer_id': product.offer_id, 'quantity': key[1]}
        if index == 0:
            cart = amazon.cart_create(item)
        else:
            cart = amazon.cart_add(item, cart.cart_id, cart.hmac)
    return cart



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

def checkout(request):
    success = False
    to_return = {'msg': 'No POST data sent.' }

    if request.method == 'POST':
        products = json.loads(request.POST['shoppingcart'])
        cart = createCart(products)
        to_return['msg'] = cart.purchase_url

    serialized = json.dumps(to_return)
    
    return HttpResponse(serialized, content_type="application/json")

def modifycart(request):
    success = False
    to_return = {'msg': 'No POST data sent.' }

    if request.method == 'POST':
        to_return['msg'] = 'Message successfully posted!'

    serialized = json.dumps(to_return)
    
    if success == True:
        return HttpResponse(serialized, content_type="application/json")
    else:
        return HttpResponse(serialized, content_type="application/json")


# Default home page given that this was the first app built
def home(request):
    gifts = Gift.objects.all().order_by('?')[:20]
    context = {
        'titlecontext': 'Giftpier Home',
        'bodycontext': '',
        'gifts': gifts
    }
    return render(request, 'azsearch/generic.html', context)
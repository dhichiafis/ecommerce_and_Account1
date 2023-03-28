from django.conf import settings
from .models import Product
class Cart(object):
    def __init__(self,request):
        self.session=request.session
        cart=self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart=self.session[settings.CART_SESSION_ID]={}
        self.cart=cart


    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product']=Product.objects.get(pk=p)

        for item in self.cart.values():
            item['total_price']=item['product'].price*item['quantity']
            yield item

    def add(self,product_id,quantity=1,override_quantity=False):
        product_id=str(product_id)
        if product_id not in self.cart:
            self.cart[product_id]={'quantity':quantity,'id':product_id}
        if override_quantity:
            self.cart[product_id]['quantity']+=quantity
        self.save()

    def remove(self,product_id):
        product_id=str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product']=Product.objects.get(pk=p)

        return sum(item['product'].price*item['quantity'] for item in self.cart.values())

    def save(self):
        self.session.modified=True

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Product,Category,OrderItem
from store.cart import Cart
from .forms import OrderForm

def checkout(request):
    cart=Cart(request)
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            total_price=0
            for item in cart:
                product=item['product']
                total_price+=int(product.price*item['quantity'])
            order=form.save(commit=False)
            order.total_cost=total_price
            order.save()
            for item in cart:
                product=item['product']
                quantity=item['quantity']
                price=product.price*quantity
                item=OrderItem.objects.create(order=order,product=product,price=price,quantity=quantity)
                return render(request,'store/order_created.html')
    else:
        form=OrderForm()
    return render(request,'store/checkout.html',{'cart':cart,'form':form})

def cart_detail(request):
    cart=Cart(request)
    return render(request,'store/cart_detail.html',{'cart':cart})

def add_to_cart(request,product_id):
    cart=Cart(request)
    cart.add(product_id)
    return redirect('store:product_list')

def remove_from_cart(request,product_id):
    cart=Cart(request)
    cart.remove(product_id)
    return redirect('store:cart_detail')

def category_detail(request,slug):
    category=get_object_or_404(Category,slug=slug)
    products=Product.objects.filter(category=category)
    context={'category':category,'products':products}
    return render(request,'store/category_detail.html',context)

def product_list(request):
    products=Product.objects.all()
    return render(request,'store/product_list.html',{'products':products})

def product_detail(request,slug):
    product=get_object_or_404(Product,slug=slug)
    return render(request,'store/product_detail.html',{'product':product})
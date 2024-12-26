from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Coffee, Cart, CartItem
from .forms import CheckoutForm
import uuid
from django.views.decorators.http import require_POST


def home(request):
    coffee = Coffee.objects.all()
    return render(request, 'home.html', {'coffee': coffee})


def checkout(request):
    cart = get_cart(request)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.total_price() for item in cart_items)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.total_price = total_price
            order.save()
            return render(request, 'checkout_success.html')  # Create this template
    else:
        form = CheckoutForm()

    return render(request, 'checkout.html', {'form': form, 'total_price': total_price})



def get_cart(request):
    session_id = request.session.session_key
    if not session_id:
        request.session.create()
        session_id = request.session.session_key

    cart, created = Cart.objects.get_or_create(session_id=session_id)
    return cart


def cart(request):
    cart = get_cart(request)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'cart.html', {'cart': cart, 'cart_items': cart_items})


@require_POST
def add_to_cart(request, coffee_id):
    cart = get_cart(request)
    coffee = get_object_or_404(Coffee, id=coffee_id)
    
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart, 
        coffee=coffee
    )
    if not created:
        cart_item.quantity += 1
    cart_item.save()  # Ensure the cart item is saved
    
    return redirect('cart')


def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart')
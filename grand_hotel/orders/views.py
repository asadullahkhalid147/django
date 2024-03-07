from django.shortcuts import render,redirect
from cart.models import Cart, CartItem
from . forms import OrderForm
from . ssl import sslcommerz_payment_gateway
from .models import Payment, OrderProduct, Order
from store.models import Product
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .ssl import sslcommerz_payment_gateway

@method_decorator(csrf_exempt, name='dispatch')
def success_view(request):
    data = request.POST
    print('data -------', data)
    payment = Payment(
        user = request.user,
        payment_id =data['tran_id'],
        payment_method = data['card_issuer'],
        amount_paid = int(data['store_amount'][0]),
        status =data['status'],
    )
    payment.save()
    
    order = Order.objects.get(user=request.user, is_ordered=False, order_number=data['value_a'])
    order.payment = payment
    order.is_ordered = True
    order.save()
    cart_items = CartItem.objects.filter(user = request.user)
    
    for item in cart_items:
        orderproduct = OrderProduct()
        # product = Product.objects.get(id=item.product.id)
        orderproduct.order = order
        orderproduct.payment = payment
        orderproduct.user= request.user
        orderproduct.product = item
        orderproduct.quantity = item.quantity
        orderproduct.ordered = True
        orderproduct.save()
        
        product = Product.objects.get(id=item.product_id)
        product.stock -= item.quantity
        product.save()

    # Clear cart
    CartItem.objects.filter(user=user).delete()
    return redirect('cart')
    
    
    
def order_complete(request):
    return render(request,'orders/order_complete.html')


def place_order(request):
    print(request.POST)
    cart_items = None
    tax = 0
    total = 0
    grand_total = 0
    # 1 --- 100
    # 5 --- 100*5
    cart_items = CartItem.objects.filter(user = request.user)
    if cart_items.count()<1:
        return redirect('store')
    for item in cart_items:
        total += item.product.price * item.quantity
    print(cart_items)  
    tax = (2*total)/100 # 2 % vat
    grand_total = total + tax
    print('no')
    if request.method == 'POST':
        
        form= OrderForm(request.POST)
        
        if form.is_valid():
            form.instance.user=request.user
            form.instance.order_total = grand_total
            form.instance.tax=tax
            form.instance.ip = request.META.get('REMOTE_ADDR')
            form.instance.payment = 2
            saved_instance = form.save()
            form.instance.order_number=saved_instance.id
            form.save()
            print('form print',form)
            return redirect(sslcommerz_payment_gateway(request,saved_instance.id,str(request.user.id),grand_total))
        
    return render(request, 'orders/place-order.html' ,{'cart_items' : cart_items, 'tax' : tax,'total' : total, 'grand_total' : grand_total})

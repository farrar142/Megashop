from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import response
from django.shortcuts import redirect, render
from accounts.models import User
from cart.models import CartItem

from products.models import ProductReal

# Create your views here.


def detail(request):
    user = request.user
    
    if str(request.user) != "AnonymousUser":
        carts = user.cartitem_set.all()
        q_sum = 0
        for i in carts:
            q_sum += i.quantity
        c_sum = 0
        for i in carts:
            c_sum += i.product_real.product.sale_price * i.quantity
    else:
        request.COOKIES.get('CartItems')
        messages.success(request,request.user)
    context = {'carts':carts,'q_sum':q_sum,'c_sum':c_sum}
    return render(request,'cart/detail.html',context)
    
@login_required(login_url='accounts:signin')
def add_product(request):
    productreal = ProductReal.objects.get(id = request.POST.get('option_id'))
    ##유저의 카트아이템 목록에 해당 목록이 존재한다면. 수량 증가
    if str(request.user) != "AnonymousUser":
        try:
            _pr = request.user.cartitem_set.all().get(product_real=productreal)
            _pr.quantity += 1
            messages.success(request,f"{productreal} {_pr.quantity}개")
            _pr.save()
        ##없다면 새로 생성
        except:
            newitem = CartItem(user=request.user,product_real=productreal,quantity=1)
            newitem.save()
            messages.success(request,productreal)
    else:
        messages.success(request,request.user)
    return redirect('products:detail',product_id = productreal.product.id)

@login_required(login_url='accounts:signin')
def modify_quantity(request,cartitem_id):
    cartitem = CartItem.objects.get(id=cartitem_id)
    cartitem.quantity = request.POST.get('quantity')
    messages.success(request,f"수량변경됨 {request.POST.get('quantity')}개")
    cartitem.save()
    return redirect("cart:detail")

@login_required(login_url='accounts:signin')
def delete_cartitem(request,cartitem_id):    
    cartitem = CartItem.objects.get(id=cartitem_id)
    cartitem.delete()
    messages.success(request,f"{cartitem} 삭제됨")
    return redirect("cart:detail")

def delete_all(request):
    if request.method == 'POST':
        selected = request.POST.getlist('cartitems')
        messages.success(request,selected)
    
    return redirect("cart:detail")
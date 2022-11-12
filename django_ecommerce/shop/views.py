from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Orders, OrderUpdate
from django.core.mail import send_mail 
from math import ceil
import json

# Create your views here.
def index(request):

    #products= Product.objects.all()
    # # print(product)
    # n=len(products)
    # # print(n)
    # nslide= n//4 + ceil((n/4)-n//4)

    allprods=[]
    catprods=Product.objects.values('cateogry', 'id')
    cats={item['cateogry'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(cateogry=cat)
        n=len(prod)
        nslide= n//4 + ceil((n/4)-n//4)

        allprods.append([prod, range(1, nslide)] )

    # # params1 = {'no_of_slides':nslide,'range':range(1, nslide) ,'product':product}
    # allprods=[[products, range(1, nslide)  ],
    #          [products, range(1, nslide)  ]]

    params={'allprods':allprods}

    return render(request, 'shop/index.html', params)   

# Create your views here.
def about(request):
    return render(request, 'shop/about.html')   


# Create your views here.
def contact(request):

    if request.method=='POST':
        name=request.POST.get('name', ' ')
        email=request.POST.get('email', ' ')
        phone=request.POST.get('phone', ' ')
        message=request.POST.get('message', ' ')

        contact=Contact(name=name, email=email, phone=phone, message=message)
        contact.save()

        ### Email message setting
        # subject = "Greetings"  
        # msg     = request.POST.get('message', ' ')  
        # to      = request.POST.get('email', ' ')  
        # res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
        # if(res == 1):  
        #     msg = "Mail Sent Successfuly"  
        # else:  
        #     msg = "Mail could not sent"  
        # return HttpResponse(msg)  



        ##### end email code...

    return render(request, 'shop/contact.html')  



# Create your views here.
def tracker(request):
    if request.method=='POST':

        orderid=request.POST.get('orderid', ' ')
        email=request.POST.get('email', ' ')

        try:
            order = Orders.objects.filter(order_id= orderid, email=email)
            
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderid)
                updates = []
                for item in update:
                    updates.append({'text':item.update_desc, 'time':item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')

        except Exception as e:
                return HttpResponse('{}')


    return render(request, 'shop/tracker.html')  




# Create your views here.
def checkout(request):

    if request.method=='POST':

        item_json=request.POST.get('itemJson', ' ')
        name=request.POST.get('name', ' ')
        email=request.POST.get('email', ' ')
        address=request.POST.get('address1', ' ')+ " , " + request.POST.get('address2', ' ')
        city=request.POST.get('city', ' ')
        state=request.POST.get('state', ' ')
        zip_code=request.POST.get('zip', ' ')
        phone=request.POST.get('phone', ' ')

        order=Orders(item_json=item_json ,name=name, email=email, phone=phone, 
                    city=city, state=state, 
                    address=address, zip_code=zip_code)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="Order has been placed")
        update.save()
        #thank=True
        #id=order.order_id
    return render(request, 'shop/checkout.html') 


# Create your views here.
def cartitem(request):
    return render(request, 'shop/cartitem.html')

# Create your views here.
def search(request):
    return render(request, 'shop/search.html')   


# Create your views here.
def productview(request, myid):

    product = Product.objects.filter(id=myid)
    return render(request, 'shop/productview.html', {'product':product[0]})  



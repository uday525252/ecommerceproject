from django.shortcuts import render
from ecommerceapp.models import Product,Customer

# Create your views here.


def fetch_data(request):
    all_products=Product.objects.all()

    item_name=request.POST.get('data')#item_name="shirt"
    if item_name!='' and item_name is not None:
        all_products=all_products.filter(title__contains=item_name)

    context={
        'all_products':all_products
    }
    return render(request,"home.html",context)


def display_one_data(request,slug):
    one_product_data=Product.objects.get(slug=slug)
    context={
        'one_product_data':one_product_data
    }
    return render(request,"data.html",context)



def checkout_view(request):
    return render(request,"checkout.html")


def contact_view(request):
    if request.method == "POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        mobileno=request.POST.get('mobileno')
        address=request.POST.get('address')
        emailid=request.POST.get('emailid')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')
        tprice=request.POST.get('tprice')

        c=Customer(name=name,age=age,phoneno=mobileno,address=address,emailid=emailid,
        city=city,state=state,pincode=pincode,totalprice=tprice)
        c.save()

    return render(request,"contact.html")

















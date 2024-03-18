from django.shortcuts import render,redirect
from .models import Product,Category,Customer

# home page views.
def home(request):
    
    return render(request,"index.html",)

#contact page views
def contact(request):
    return render(request,"contact.html",)


#about page views
def about(request):
    return render(request,"about.html",)

#prodect page views
def glass_product(request):
    products = Product.objects.all()
    return render(request,"prodect.html",{'products':products})



def category(request,foo):
    foo = foo.replace('-',' ')
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, "category.html", {'products': products, 'category': category})
    except Category.DoesNotExist:
        return redirect('home')

def all_product(request,pk):
    prodect =Product.objects.get(id=pk)
    return render(request,"all_prodect.html",{'prodect':prodect})
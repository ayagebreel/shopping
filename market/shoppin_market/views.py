from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.

def getProducts(request):
    products = Product.objects.order_by('price')
    product_names = ', '.join([pro.name for pro in products])
    return HttpResponse(product_names)

def searchProducts(request,name):
	products=Product.objects.filter(name__contains=name)
	product_names = ', '.join([pro.name for pro in products])
	return HttpResponse(product_names)

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def add_to_cart(request,product_id):
	#get the produc object that will be added to cart
    product = get_object_or_404(Product, pk=product_id)
    #make order with attribute active is false as it is still in the cart when the user go to payment gateway,we will make active true to be ordered
    cart = Orders.objects.get_or_create(user=request.user, active=false)
    #add products of the order with amount
    order_product= OrderProduct.objects.get_or_create(OrderID_id=cart,ProductID_id=product)
    order_product.amount += 1
    order_product.save()
    return HttpResponse(order_product)

 def get_user_cart(request,user_id):
 	user = get_object_or_404(User, pk=product_id)
 	cart=Orders.objects.get(user=request.user,active=false)
 	return HttpResponse(cart)

 def execute_order(request,order_id):
 	order = get_object_or_404(Order, pk=order_id)
 	cart=Orders.objects.get(user=request.user,OrderID=order_id)
 	cart.active=true
 	cart.save()
 	return HttpResponse(cart)

 def get_user_orders(request,user_id):
 	orders = Product.objects.get(UserID_id=user_id)
    return HttpResponse(orders)


from typing import ValuesView
from django.contrib.messages.api import error
from django.shortcuts import render,HttpResponse,redirect
from .models.product import product
from .models.category import category
from .models.customer import customer
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views import View

# create your class views here.
class index(View):
    # get request product id 
    def post(self,request):
        product = request.POST.get('product')
        change = request.POST.get('change')
        # print(product)
        # cart access from session
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if change:
                    # add to button(add cart) then quantity less then 1(dictonary)
                    if quantity<=1:
                        cart.pop(product)
                    else:    
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1   
            else:
                cart[product] = 1    
        else:
            cart  = {}
            cart[product]  = 1
        request.session['cart'] = cart  
        print('cart-:',request.session['cart'])  
        return redirect('index')
    #firslty request by user hit this point 
    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart']={}
        products = None
        categories = category.get_all_categories()
        categoryid = request.GET.get('category')
        if categoryid:
            products = product.get_all_categories(categoryid)

        else:
            products = product.get_all_products()

        data = {}
        # session identy who is user
        data ['products'] = products
        data ['categories'] = categories
        print('your data-:',request.session.get('user_username'))
        return render(request,'index.html',data)




# Create your functions views here.
# def index(request):
    # products = product.get_all_products()
    # products = None
    # categories = category.get_all_categories()
    # categoryid = request.GET.get('category')
    # if categoryid:
    #    products = product.get_all_categories(categoryid)
    # else:
    #      products = product.get_all_products()
    # data = {}
    # # session identy who is user
    # data ['products'] = products
    # data ['categories'] = categories
    # print('your data-:',request.session.get('user_username'))
    # return render(request,'index.html',data)

def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'You are successfully logged in')
            # session part
            request.session['user_id']=user.id
            request.session['user_username']=user.username
            return redirect('login')

        else:
            messages.error(request,'Invalid credentials please try again')    
            return redirect('login')
    else:
         return render(request,'login.html')       
      

def signup(request):
    if request.method == 'POST':
        # getthe all parameter as username,pss,name etc
        # request.post ek dictionary hai or query ker ke value ko store kiya hai
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # text field auto feild after reload page
        my_value={
            'username':username,
            'first_name':first_name,
            'last_name':last_name,
            'email':email
        }
        data={'values':my_value}
        # checks for errorneous input(koi user input field blank na chode
        # user should be under 10 character
        if len(username) > 10:
            messages.error(request, "Your username must be under 10 characters")
            return render(request,'signup.html',data)
            
        if User.objects.filter(username = username).first():
            messages.error(request, "This username is already taken")
            return render(request,'signup.html',data)

        if len(first_name) < 4:
            messages.error(request,'Your first-name must be greater then 3 characters')
            return render(request,'signup.html',data)
        # check email if already registor or not
        if User.objects.filter(email=email).first():
            messages.error(request,'This email already exist')
            return render(request,'signup.html',data)
        # user pass1 and pass2 should be match
        if pass1 != pass2:
            messages.error(request, 'Your password do not match')
            return redirect('signup')

        # create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()
        messages.success(request, 'Your account has been successfully created')
        return redirect('index')

    else:
        return render(request,'signup.html')
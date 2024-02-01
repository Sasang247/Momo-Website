from django.shortcuts import render
from .models import Product,MomoCategory,MenuCategory,allmenu,IngredientCategory,ingredient
from .models import Contact
from django.shortcuts import redirect
from django.contrib import messages




# Create your views here.

def about(request):
    return render(request,'momos/aboutus.html')


def services(request):
    return render(request,'momos/services.html')



def menu(request):
    # Retrieve all categories
    categories = MomoCategory.objects.all()

    # Create a dictionary to store data for each category
    data = {}

    # Loop through each category and get associated products
    for category in categories:
        momos = Product.objects.filter(category=category)
        data[category.name] = momos

    # Pass the data to the template
    return render(request,'momos/menu.html',{'data': data})



def foodmenu(request):
    every= MenuCategory.objects.all()
    data = {}
    for category in every:
        all= allmenu.objects.filter(category=category)
        data[category.name] = all
    return render(request,'momos/foodmenu.html',{'data': data})


def allergy(request):
    categories = IngredientCategory.objects.all()
    data = {}
    
    for category in categories:
        ingredients = ingredient.objects.filter(category=category)
        data[category.name] = ingredients
    
    return render(request, 'momos/allergy.html', {'data': data})


def contact(request):
    if request.method == "POST":
        fname = request.POST['fname']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        data = Contact.objects.create(
            fname=fname,
            email=email,
            phone=phone,
            message=message
        )
        messages.success(request, 'Received Your Message.')  

        return redirect('contact')
        
    return render(request, 'momos/contact.html')

    
    

def home(request):
    return render(request,'momos/index.html')
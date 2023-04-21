from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Pizza
from .forms import PizzaModelForm
from .forms import ToppingModelForm
from .models import Toppings

def index(request):
    print('INSIDE of INDEX !!!!!!!!!!')
    return render(request, 'orlando_pizzas/index.html')
@login_required
def new_topping(request,pizza_id):
    if request.method != 'POST':
        form = ToppingModelForm()
    else:
        pizza = Pizza.objects.get(id=pizza_id)
        print(f'HAHAHAHHAHAHAHHAHAHHAHAHAHHAHAHAHAHHAHAHAH >>>>>>>>>>>>>>>>>>>>>>{pizza}')
        form = ToppingModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return getPizzaById(request,pizza_id)
    context = {'form': form,'pizza_id': pizza_id}
    return render(request, 'orlando_pizzas/new_topping.html', context)
@login_required
def new_pizza(request):
    if request.method != 'POST':
        form = PizzaModelForm()
    else:
        form = PizzaModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('orlando_pizzas:pizza')
    context = {'form': form}
    return render(request, 'orlando_pizzas/new_pizza.html', context)

def getPizza(request):
    try:
        pizzas = Pizza.objects.order_by('date_added')
        context = {'pizzas': pizzas}
        print(f'Pizza .... {pizzas}')
        shortcut =render(request, 'orlando_pizzas/pizza.html', context)
    except Exception:
        shortcut = render(request, 'orlando_pizzas/errors.html')
    return shortcut

def getPizzaById(request, pizza_id):

    try:
        pizza = Pizza.objects.get(id=pizza_id)
        print(f'INSIDE of PIZZA and TOPPINGS  !!!!!!!!!!{pizza}')
        toppings = Toppings.objects.filter(pizza_id=pizza_id).all()
        context = {'toppings': toppings , 'pizza':pizza}
        shortcut = render(request, 'orlando_pizzas/pizza_toppings.html', context)
    except Exception:
        shortcut = render(request, 'orlando_pizzas/errors.html')
    return shortcut
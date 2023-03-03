from django.shortcuts import render, redirect
from .forms import PizzaForm, MultiplerPizzaForm
from django.contrib import messages
from .models import Pizza
from django.forms import formset_factory

# Create your views here.

def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    multiple_form = MultiplerPizzaForm()
    form = PizzaForm()  

    if request.method == 'POST':
        filled_forms = PizzaForm(request.POST)
        if filled_forms.is_valid():
            created_pizza = filled_forms.save()
            messages.success(request, f'Tahanks for ordering! Your {created_pizza.size} is on way ...')
            context = {
                'pizzaform' : form,
                'multiple_form': multiple_form,
                'created_pizza_pk': created_pizza.id
            }
            return render(request, 'pizza/order.html', context)  



    context = {
        'pizzaform' : form,
        'multiple_form': multiple_form
    }  

    return render(request, 'pizza/order.html', context)    


def edit_order(request, pk):
    pizza = Pizza.objects.get(pk = pk)
    form = PizzaForm(instance=pizza)
    
    if request.method == "POST":
        filled_forms = PizzaForm(request.POST, instance=pizza)
        if filled_forms.is_valid():
            pizza = filled_forms.save()
            messages.success(request, 'Order has been updated.')
            return redirect('order')
            
            # context={
            #     "pizzaform" : filled_forms,
            #     "pizza" : pizza
            # }
            # return render(request, "pizza/edit_order.html", context)

    
    context = {
        "pizzaform" : form,
        "pizza" : pizza
    }
    
    return render(request, "pizza/edit_order.html", context)


def pizzas(request):
    # number = int(request.GET["number"])
    # PizzaFormSet = formset_factory(PizzaForm, extra=number)
    # formset = PizzaFormSet()

    # if request.method=="POST":
    #     filled_formset = PizzaFormSet(request.POST)
    #     if filled_formset.is_valid():
    #         for form in filled_formset:
    #             form.save()
    #         messages.success(request, 'Pizzas have been ordered!')
    #         return redirect("order")

    number_of_pizzas = 2
    filled_multiple_pizza_form = MultiplerPizzaForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data.get('number')
        print(number_of_pizzas)
    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()
    
    
    if request.method == "POST":
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                form.save()
            messages.success(request, 'Pizzas have been ordered!')
    
    context = {
        "formset" : formset
    }
    
    return render(request, "pizza/pizzas.html", context)
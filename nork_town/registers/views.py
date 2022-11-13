from django.shortcuts import render, redirect
from .models import Person, Car
# Create your views here.
def home(request):
    peoples = Person.objects.all()
    return render(request, 'index.html', {"peoples": peoples})

def create(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        age = request.POST.get("age")
        cpf = str(request.POST.get("cpf")).replace('.', '').replace('-', '')
        sale_oportunity = True
        Person.objects.create(name=name, surname=surname, age=age, cpf=cpf, sale_oportunity=sale_oportunity)
        return redirect(home)
    return render(request, 'create.html')

def delete(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return redirect(home)

def update(request, id):
    person = Person.objects.get(id=id)
    person.name = request.POST.get("name")
    person.surname = request.POST.get("surname")
    person.age = request.POST.get("age")
    person.cpf = str(request.POST.get("cpf")).replace('.', '').replace('-', '')
    person.save()
    return redirect(home)

def edit(request, id):
    person = Person.objects.get(id=id)
    return render(request, 'update.html', {"person": person})
    
def create_car(request, id):
    return render(request, 'create_car.html', {"person_id": id})

def delete_car(request, id):
    car = Car.objects.get(id=id)
    car.delete()
    user = Person.objects.get(id=car.user.id)
    user.sale_oportunity = True
    user.save()
    print(user.sale_oportunity)
    return redirect(home)

def build_car(request, id):
    user = Person.objects.get(id=id)
    if user.get_cars().count() <= 3:
        Car.objects.create(
                vehicle_name= request.POST.get("vehicle_name"),
                category = request.POST.get("category"),
                brand = request.POST.get("brand"),
                color = request.POST.get("color"),
                user = Person.objects.get(id=id)
            )
        if user.get_cars().count() == 3:
            user.sale_oportunity = False
            user.save()
        return redirect(home)
    else:
        return redirect(home)

def update_car(request, id):
    car = Car.objects.get(id=id)
    if request.method == 'POST':
        car.vehicle_name = request.POST.get("vehicle_name")
        car.category = request.POST.get("category")
        car.brand = request.POST.get("brand")
        car.color = request.POST.get("color")
        car.save()
        return redirect(home)
    return render(request, 'update_car.html', {"car": car})
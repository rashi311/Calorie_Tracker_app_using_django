from django.shortcuts import render,get_object_or_404,redirect
from .models import Food,Consume
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def index(request):
    if request.method=="POST":
        food_consumed=request.POST['food_consumed']
        consume=get_object_or_404(Food,name=food_consumed)
        user=request.user
        consume=Consume(user=user,food_consumed=consume)
        consume.save()
        return redirect("index")
    foods=Food.objects.all()
    consumed_food=Consume.objects.filter(user=request.user)
        
        
    context={'foods':foods,'consumed_food':consumed_food}
    return render(request,'myapp/index.html',context)


def delete_consume(request,id):
    consumed_food=Consume.objects.get(id=id)
    if request.method=="POST":
        consumed_food.delete()
        return redirect('index/')
    else:
        return render (request,'myapp/delete.html')
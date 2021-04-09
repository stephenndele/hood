from django.shortcuts import render
from .models import Hood

# Create your views here.

def home(request):
    query = request.GET.get('title')    
    
    allHoods = None
    if query:
        allHoods = Hood.objects.filter(title__icontains=query)
    else:

        allHoods = Hoods.objects.all()
    context = {
        "hoods": allHoods,
    }

    return render(request,'main/index.html', context)
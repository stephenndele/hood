from django.shortcuts import render, redirect
from .models import Hood
from .forms import *



# Create your views here.

def home(request):
    query = request.GET.get('title')    
    
    allHoods = None
    if query:
        allHoods = Hood.objects.filter(title__icontains=query)
    else:

        allHoods = Hood.objects.all()
    context = {
        "hoods": allHoods,
    }

    return render(request,'main/index.html', context)


def add_hood(request):
    if request.method == 'POST':
        form = HoodForm(request.POST or None, request.FILES,)

        if form.is_valid():
            data = form.save(commit=False)
            # data.user = request.user.profile
            data.save()
            return redirect("main:home")
    else:
        form = HoodForm()
    return render(request, 'main/addhoods.html', {'form': form, "controller":"Add Hood"}) 

# def details(request, id):
#     hood = Hood.objects.get(id=id)
#     reviews = Review.objects.filter(project=id).order_by('-comment')
    
#     average1 = reviews.aggregate(Avg("design_rating"))["design_rating__avg"]
#     average2 = reviews.aggregate(Avg("usability_rating"))["usability_rating__avg"]
#     average3 = reviews.aggregate(Avg("content_rating"))["content_rating__avg"]

#     average = (average1 + average2 + average3) / 3

#     if average == None:
#         average = 0
#     average = round(average, 2)

#     context = {
#         "project": project,
#         "reviews": reviews,
#         "average": average,

#     }

#     return render( request,'main/details.html', context)
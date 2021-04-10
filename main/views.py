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

def details(request, id):
    hood = Hood.objects.get(id=id)
    posts = Post.objects.filter(hood=id).order_by('-comment')
    bussines = Bussines.objects.filter()
    
    # average1 = reviews.aggregate(Avg("design_rating"))["design_rating__avg"]
    

    # if average == None:
    #     average = 0
    # average = round(average, 2)

    context = {
        "project": project,
        "reviews": reviews,
        "posts":posts,
        "bussines":bussines
        # "average": average,

    }

    return render( request,'main/details.html', context)


def userpage(request,):
	if request.method == "POST":
		user_form = UserForm(request.POST, instance=request.user)
		profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
		if user_form.is_valid():
		    user_form.save()
		    messages.success(request,('Your profile was successfully updated!'))
		elif profile_form.is_valid():
		    profile_form.save()
		    messages.success(request,('Your Projects were successfully updated!'))
		else:
		    messages.error(request,('Unable to complete request'))
		# return redirect ("main:userpage")
	user_form = UserForm(instance=request.user)
	profile_form = ProfileForm(instance=request.user.profile)
	return render(request = request, template_name ="main/user.html", context = {"user":request.user, 
		"user_form": user_form, "profile_form": profile_form })
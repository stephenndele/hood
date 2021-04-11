from django.shortcuts import render, redirect, get_object_or_404
from .models import Hood, Business, Post
from .forms import *
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import HoodSerializer


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

@login_required()
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

@login_required()
def edit_hoods(request, id):
    hood = Hood.objects.get(id=id)

    if request.method == 'POST':
        form = HoodForm(request.POST or None, instance=hood)

        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("main:details", id)
    else:
        form = HoodForm(instance=hood)
    return render(request,'main/addhoods.html', {"form": form, "controller":"Update Hood"})
@login_required()
def delete_hoods(request, id):

    hood = Hood.objects.get(id=id)
    hood.delete()
    return redirect("main:home")

@login_required()
def details(request, id):
    hood = Hood.objects.get(id=id)
    posts = Post.objects.filter(hood=id).order_by('-post')
    business = Business.objects.filter(hood=id)
    
    # Occupants = occupants.aggregate(Avg("design_rating"))["design_rating__avg"]
    

   
    context = {
        "hood": hood,
        "posts":posts,
        "business":business

    }

    return render( request,'main/details.html', context)

@login_required()
def userpage(request):
    '''
    A function for creating the user profile and updating
    
    '''
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('main:userpage')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)


    # profile = request.user.profile.hood.objects.all()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        # 'profile': profile
    }

    return render(request, 'main/user.html', context)





@login_required()
def create_post(request, hood_id):
    hood = Hood.objects.get(id=hood_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user = request.user.profile
            post.save()
            return redirect('main:details', hood.id)
    else:
        form = PostForm()
    return render(request, 'main/post.html', {'form': form})

@login_required()
def create_business(request, hood_id):
    query = request.GET.get('name') 
    hood = Hood.objects.get(id=hood_id)
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user = request.user.profile
            post.save()
            return redirect('main:details', hood.id)
    else:
        form = BusinessForm()
    return render(request, 'main/business.html', {'form': form})

@login_required()
def join_hood(request, id):
    hood = get_object_or_404(Hood, id=id)
    request.user.profile.hood = hood
    request.user.profile.save()
    messages.success(request, "Welcome to Your Hood!")
    return redirect('main:details', hood.id)


def leave_hood(request, id):
    hood = get_object_or_404(Hood, id=id)
    request.user.profile.hood = None
    request.user.profile.save()
    messages.success(request, "Bye see you again")
    return redirect("main:home")



# def search_business(request):
#     if request.method == 'GET':
#         name = request.GET.get("title")
#         results = Business.objects.filter(name__icontains=name).all()
#         print(results)
#         message = f'name'
#         params = {
#             'results': results,
#             'message': message
#         }
#         return render(request, 'results.html', params)
#     else:
#         message = "You haven't searched for any image category"
#     return render(request, "results.html")


class HoodList(APIView):
    def get(self, request, format=None):
        all_hood = Hood.objects.all()
        serializers = HoodSerializer(all_hood, many=True)
        return Response(serializers.data)
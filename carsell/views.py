from django.shortcuts import render
from . models import Car, CarEvaluate, Profile, CarEvaluate
from django.contrib.auth.decorators import login_required
from .forms import *
import datetime as dt

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    date = dt.date.today()
    cars = Car.objects.all()
    return render(request, 'index.html', {'cars':cars, "date":date})


def profile(request):
    date = dt.date.today()
    current_user = request.user
    # profile = Profile.objects.get(user=current_user.id)
    cars = Car.objects.all()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    return render(request, 'profile/profile.html', locals() )#{"date": date, "profile":profile,"cars":cars})

def edit_profile(request):
    date = dt.date.today()
    current_user = request.user
    #profile = Profile.objects.get(user=current_user.id)
    if request.method == 'POST':
        signup_form = EditForm(request.POST, request.FILES,instance=request.user.profile) 
        if signup_form.is_valid():
            signup_form.save()
            return redirect('profile')
    else:
        signup_form =EditForm() 
        
    return render(request, 'profile/edit_profile.html', {"date": date, "form":signup_form,"profile":profile})

@login_required(login_url='/login/')
def rate(request, project_id):
    try:
        project=Car.objects.get(id=car_id)
    except Exception as e:
        raise  Http404()

    if request.method=='POST':
        current_user=request.user
        check = Rating.objects.filter(poster = current_user, project = project_id).all()
        form=RateForm(request.POST)
        if form.is_valid:
            if len(check) < 1:
                ratings=form.save(commit=False)
                if ratings.usability < 11 or ratings.design < 11:
                    ratings.poster=current_user
                    ratings.car= car_id
                    ratings.average = (ratings.usability + ratings.design)/3
                    ratings.save()
                else:
                    message = 'Rating failed! One value is not within the defined range'
                    return redirect('rate', {"message":message})
            else:
                Rating.objects.filter(poster = current_user, project = project_id).delete()
                ratings=form.save(commit=False)
                if ratings.usability < 11 or ratings.content < 11 or ratings.design < 11:
                    ratings.poster=current_user
                    ratings.project= project_id
                    ratings.average = (ratings.usability + ratings.design)/3
                    ratings.save()
                else:
                    message = 'Rating failed! One value is not within the defined range'
                    return redirect('rate', {"message":message})

            return redirect('review', project_id)

    else:
        form=RateForm()

    return render(request,"rate.html",{"project":project,'form':form})

@login_required(login_url='/login/')
def rating(request, pk):
    car = get_object_or_404(Car, pk=pk)
    rating = CarEvaluate.objects.all()
    if request.method == 'POST':
        form = RatingForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            rating=form.save(commit=False)
            rating.voter = request.user.id
            rating.voted = project.id
            rating.save()
            usability = form.cleaned_data.get('usability')
            content = form.cleaned_data.get('content')
            design = form.cleaned_data.get('design')
            
            messages.success(request, f'You have rated this project usability: {usability}, design: {design}, content: {content}')
            return redirect('index')
    else:
        form = RatingForm()
    return render(request, 'rating.html', {'form': form, "project":project})

from django.shortcuts import render,redirect
from .models import Crop

def home(request):

    return render(request,'home.html')


def add_crop(request):

    if request.method=="POST":

        Crop.objects.create(

            crop_name=request.POST['crop_name'],

            farmer_name=request.POST['farmer_name'],

            season=request.POST['season'],

            price=request.POST['price']

        )

        return redirect('/view/')

    return render(request,'add_crop.html')


def view_crop(request):

    crops=Crop.objects.all()

    return render(request,'view_crop.html',{'crops':crops})

def edit_crop(request,id):

    crop=Crop.objects.get(id=id)

    if request.method=="POST":

        crop.crop_name=request.POST['crop_name']
        crop.farmer_name=request.POST['farmer_name']
        crop.season=request.POST['season']
        crop.price=request.POST['price']

        crop.save()

        return redirect('/view/')

    return render(request,'edit_crop.html',{'crop':crop})

def delete_crop(request,id):

    crop=Crop.objects.get(id=id)

    crop.delete()

    return redirect('/view/')

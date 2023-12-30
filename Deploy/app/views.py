from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from . import models
from . import forms

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np


# Create your views here.
def home_view(request):
    if request.method == "POST":
        username = request.POST['username']
        #print(username)
        password = request.POST['password']
        #print(password)
        name = request.POST['user']
        if name == "user":
            user = authenticate(request, username=username, password=password)
            #print(user)
            if user is not None:
                form = forms.UserImageForm()
                login(request, user)
                return render(request, 'app/index.html',{'form':form})
            else:
                msg = 'Invalid Credentials'
                form = AuthenticationForm(request.POST)
                return render(request, 'app/user_login.html', {'form': form, 'msg': msg})
        else:
            user = authenticate(request, username=username, password=password)
            #print(user)
            if user is not None:
                login(request, user)
                model = models.UserImageModel.objects.latest('id')
                form = forms.DoctorFeedForm(request.POST)
                #print(model)
                return render(request, 'app/last.html', {'model':model,'form':form})
            else:
                msg = 'Invalid Credentials'
                form = AuthenticationForm(request.POST)
                return render(request, 'app/user_login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
    return render(request, 'app/user_login.html', {'form': form})

def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #print('saving')
            form.save()
            return render(request, 'app/user_signup.html', {'msg':"Successfully registered",'form':form})
    else:
        form = UserCreationForm()
    return render(request, 'app/user_signup.html',{'form':form})

def doctor_login(request):
    form = AuthenticationForm()
    return render(request, 'app/login.html', {'form': form})

def doctor_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #print('saving')
            form.save()
            return render(request, 'app/signup.html', {'msg':"Successfully registered",'form':form})
    else:
        form = UserCreationForm()
    return render(request, 'app/signup.html',{'form':form})

def doctor_patient_details_view_all(request):
    model = models.UserImageModel.objects.all().order_by('-id')
    #print(model)
    return render(request, 'app/all.html', {'model':model})


def doctor_patient_details_view_last(request):
    if request.method == "POST":
        form = forms.DoctorFeedForm(request.POST)
        #print('form',form)
        if form.is_valid():
            form.save()
            model = models.UserImageModel.objects.latest('id')
            #print(model)
            return render(request, 'app/last.html', {'model':model,'msg':'Feedback sent'})
        else:
            model = models.UserImageModel.objects.latest('id')
            return render(request, 'app/last.html', {'model':model,'msg':'Feedback Error'})
    else:
        model = models.UserImageModel.objects.latest('id')
        form = forms.DoctorFeedForm(request.POST)
    return render(request, 'app/last.html', {'model':model,'form':form})

def index(request):
    print("HI")
    if request.method == "POST":
        print('HIPOST')
        form = forms.UserImageForm(files=request.FILES)
        print('form',form)
        if form.is_valid():
            print('HIFORM')
            form.save()
            obj = form.instance
            #('obj',obj)
            result = models.UserImageModel.objects.latest('id')
            result = result.image            
            model = load_model('C:/Users/SPIRO-PYTHON/Desktop/dl22 new/E1563/CODE/Deploy/app/resnet.h5')
            test_image1 = image.load_img('C:/Users/SPIRO-PYTHON/Desktop/dl22 new/E1563/CODE/Deploy/media/' + str(result),
                                target_size=(225, 225))
            test_image = image.img_to_array(test_image1)
            test_image = np.expand_dims(test_image, axis=0)
            result = model.predict(test_image)
            prediction = result[0]
            prediction = list(prediction)
            classes=['INTERMITTENT_ASTHMA','NORMAL','SEVERE_PERSISTENT_ASTHMA']
            output = zip(classes, prediction)
            output = dict(output)
            if output['INTERMITTENT_ASTHMA'] == 1.0:
                a='INTERMITTENT_ASTHMA'
            elif output['NORMAL'] == 1.0:
                a='NORMAL'
            elif output['SEVERE_PERSISTENT_ASTHMA'] == 1.0:
                a="SEVERE_PERSISTENT_ASTHMA"
            
            ob = models.UserImageModel.objects.latest('id')
            ob.type1 = a
            ob.save()
            
            return render(request, 'app/index.html',{'form':form,'obj':obj,'predict':a})
    else:
        form = forms.UserImageForm(files=request.FILES)
    return render(request, 'app/index.html',{'form':form})

def apredict(request):
    return render(request, 'app/index.html')

def feedback(request):
    model = models.DoctorFeedModel.objects.latest('id')
    return render(request, 'app/feedback.html', {'model':model})

def doctor(request):
    data = models.UserImageModel.objects.filter(type1="Happy").get()
    return render(request, 'app/admin.html',{'data':data})

def logout_view(request):
    logout(request)
    return redirect('home')
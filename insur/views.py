from django.shortcuts import render,HttpResponse
import joblib
model=joblib.load('/home/kimath/Desktop/INSURENCE/insurence/insur/static/random_forest_regressor')
# Create your views here.

def index(request):
    #return HttpResponse("THis is home page")
    return render(request,'index.html')


def about(request):
    #return HttpResponse("THis is about page")
    return render(request,'about.html')


def contact(request):
    #return HttpResponse("THis is contact page")
    return render(request,'contact.html')


def login(request):
    #return HttpResponse("THis is about page")
    return render(request,'login.html')


def registration(request):
    #return HttpResponse("THis is contact page")
    return render(request,'registration.html')

def prediction(request):
    if request.method=="POST":
        print("am here")
        age=int(request.POST.get('age'))
        sex=int(request.POST.get('sex'))
        bmi=int(request.POST.get('bmi'))
        children=int(request.POST.get('children'))
        smoker=int(request.POST.get('smoker'))
        print("hhhhhhhhh")
        region=int(request.POST.get('region'))
        print(age,sex,bmi,children,smoker,region)

        pred=round(model.predict([[age,sex,bmi,children,smoker,region]])[0])
        print(pred)

        output={
"output":pred
        }
        return render(request,'prediction.html',output)
    
    else:    
    #return HttpResponse("THis is prediction page")
        return render(request,'prediction.html')


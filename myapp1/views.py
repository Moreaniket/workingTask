from django.shortcuts import render,HttpResponse,redirect

from django.contrib import messages
# Create your views here.

from.models import student,shubham,customer

def home(request):
    #return render(request,"send_otp.html")
    return render(request,"registration.html")


def register(request):
    if request.method=="POST":
        nm=request.POST["name"]
        em=request.POST["email"]
        nmb=request.POST["number"]
        ps=request.POST["password"]


        obj=student(name=nm,email=em,number=nmb,password=ps)
        obj.save()

        messages.success(request,"Registration Successfully Complete")
        #return HttpResponse("Registration Successfully")
        return redirect("/login")
    else:
        return HttpResponse("Fails to Register")


 #  READ

def showdata(request):
    data=student.objects.all()
    return render(request,"showdata.html",{'data':data})

# DELETE

def delete(request):
    x=request.GET["id"]
    student.objects.all().filter(id=x).delete()
    return redirect("/showdata")


# UPDATE

def update(request):
    x = request.GET["id"]
    data=student.objects.all().filter(id=x)
    return render(request,"update.html",{'data':data})

# SAVE UPDATE

def saveupdate(request):
    if request.method=="POST":
        id=request.POST["id"]
        nm=request.POST["name"]
        em=request.POST["email"]
        nmb=request.POST["number"]
        ps=request.POST["password"]


        student.objects.all().filter(id=id).update(name=nm,email=em,number=nmb,password=ps)
        return redirect("/showdata")


def login(request):
    return render(request,"login.html")


def checklogin(request):
    if request.method=="POST":
        em=request.POST["email"]
        ps=request.POST["password"]

        data=student.objects.all().filter(email=em,password=ps)

        if data:
            #request.session["username"]=em # session start
            messages.success(request,"Login Successfully")
            return redirect("/dashboard")
        else:
            messages.warning(request, "Login Fails try again")
            return HttpResponse("LOGIN FAILS..")






def logout(request):
    del request.session['otp_verified']
    messages.warning(request,"Logout Successfully")
    return redirect("/verify-otp")

# FILE UPLOAD

def file(request):
    return render(request,"file.html")



def savefile(request):
    if request.method=="POST":
        nm=request.POST["name"]
        ph=request.FILES["photo"]

        obj=shubham(name=nm,photo=ph)
        obj.save()
        return HttpResponse("FILE UPLOAD SUCCESSFULLY")
    else:
        return HttpResponse("FILE UPLOAD FAILS")



def cookies(request):
    res= HttpResponse("Cookies Set")
    res.set_cookie("Name","Aniket")
    res.set_cookie("address","pune")
    return res



def getcookies(request):
    res=request.COOKIES["Name"]
    x=request.COOKIES["address"]
    myvar=res+x
    return HttpResponse(myvar)


from .forms import customer_form

def form(request):
    data=customer_form()
    return render(request,"form.html",{'data':data})



def multipledelete(request):
    if request.method=="POST":
        x=request.POST.getlist("id")
        for id in x:
            student.objects.filter(id=id).delete()
        return redirect("/showdata")

    else:
        return HttpResponse("Fails...")


from.serializers import customerserializer
from rest_framework.renderers import JSONRenderer
def customerdetails(request,id):

    data=customer.objects.get(id=id)
    serializer=customerserializer(data)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type="application/json_data")



def list(request):

    data=customer.objects.all()
    serializer=customerserializer(data,many=True)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type="application/json_data")


def dashboard(request):
    if request.session.get("otp_verified",False): # GET SESSION
       return render(request,"dashboard.html")
    else:
        return redirect("/verify-otp")







import pyotp
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse

def send_otp(request):
    if request.method == 'POST':
        email = request.POST['email']

        # Generate a unique secret for this user session
        secret = pyotp.random_base32()  # Generate a random base32 secret
        totp = pyotp.TOTP(secret)
        otp = totp.now()  # Generate OTP

        # Store the secret and the generated OTP in the session
        request.session['otp_secret'] = secret  # Store secret in session
        request.session['generated_otp'] = otp  # Store the generated OTP in session
        request.session['email'] = email  # Store email in session

        # Send the OTP via email
        send_mail(
            'Your OTP Code',
            f'Your OTP is {otp}. Please use this otp to verify your email.',
            'aniketmore7964@gmail.com',  # From email address
            [email],  # To email address
            fail_silently=False,
        )
        return redirect('/verify-otp')  # Redirect to the verification page

    return render(request, 'send_otp.html')  # Adjust the path as needed


def verify_otp(request):
    if request.method == 'POST':
        otp_input = request.POST['otp'].strip()  # Trim whitespace

        # Retrieve the generated OTP stored in the session
        generated_otp = request.session.get('generated_otp', None)

        if generated_otp:

            if otp_input == generated_otp:
                request.session['otp_verified'] = True  # SESSION START FOR DASHBOARD AND GET IN DASHBOARD.HTML
                #return HttpResponse('OTP verified successfully!')
                return redirect("/dashboard")
            else:
                return HttpResponse('Invalid OTP, please try again.')
        else:
            return HttpResponse('Session expired. Please request a new OTP.')

    return render(request, 'verify_otp.html')  # Adjust the path as needed


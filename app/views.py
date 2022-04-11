from django.shortcuts import render
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
import datetime
# Create your views here.

def homepage(request):
    if request.method=='POST':
        # print(type(request.POST.items()))
        # for key in request.POST.items():
        #     print(key)
            # print("key: "+key+"  "+"value"+value)
        if "password2" in request.POST:
            # print("post")
            form = NewUserForm(request.POST)
            # print("form")
            if form.is_valid():
                # print("valid")
                user = form.save()
                login(request, user)
                messages.success(request, "Registration successful.")
                # print("sucess")
                return redirect("home")
            else:
                messages.error(request, "Unsuccessful registration. Invalid information.")
        else:
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    # messages.success(request, f"You are now logged in as {username}.")
                    return redirect("dash")
            else:
                form = AuthenticationForm()

    return render(request,'home.html',{'registerform':NewUserForm,'loginform':AuthenticationForm,'time':datetime.datetime.now()})

# def register_request(request):
#     if request.method == "POST":
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             print("store")
#             messages.success(request, "Registration successful." )
#             return redirect("dash")
#         messages.error(request, "Unsuccessful registration. Invalid information.")
#     form = NewUserForm()


def dash(request):
    # messages=messages.success(request, 'are logout thanks for use')
    return render(request,'dash.html',{'time':datetime.datetime.now()})


#bdvkfbk1233bkvjb@


# def logout(request):
#     return render(request,)
from django.shortcuts import render
from django.http import HttpResponse
def home_view(request,*args,**Kwargs):
    print(args,Kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request,"home.html", {})
def contact_view(request,*args,**Kwargs):
    #return HttpResponse("<h1>Welcome </h1>")    
    my_context={
    "title": " abc This is about me" ,
    "this_is_true": True,
    "my_number": 123 ,
    "my_list": [1313,4231,312,"Abc"] ,
    "my_html": "<h1>Hello World</h1>"

    }
    return render(request,"contact.html", my_context)


from django.http import HttpResponse
from django.shortcuts import render
#it was for index.html
# def home(request):
#     data={
#         'title':'Home Page',
#         'bdata':'welcome to SaniaZ codes',
#         'clist':['php','java','SQL'],
#         'numbers':[10,20,30,40,55,66,77,88,100],
#         'std_detail':[
#             {'name':'Ahmad','phn':2344566788},
#             {'name':'Amna','phn':2343544657},
#         ]
        
#     }
#     return render(request,"index.html",data)
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def categories(request):
    return render(request, "categories.html")

def products(request):

    products = [
        {
            "name": "Rainbow T-Shirt",
            "category": "Boys",
            "price": 15,
            "description": "Soft cotton colorful t-shirt.",
            "image": "https://images.unsplash.com/photo-1519238263530-99bdd11df2ea"
        },
        {
            "name": "Cute Summer Dress",
            "category": "Girls",
            "price": 25,
            "description": "Beautiful and comfortable summer dress.",
            "image": "https://images.unsplash.com/photo-1596870230751-ebdfce98ec42"
        },
        {
            "name": "Baby Cotton Set",
            "category": "Baby",
            "price": 20,
            "description": "Soft cotton clothing set for babies.",
            "image": "https://images.unsplash.com/photo-1519689680058-324335c77eba"
        }
    ]

    return render(request, "products.html", {
        "products": products
    })
    
def userform(request):
    # try:
    #     n1=int(request.GET['val1'])
    #     n2=int(request.GET['val2'])
    #     print(n1+n2)
    # except:
    #     pass
    
    result=0
    """using GET method"""
    # if request.GET:
       
    #     n1 = int(request.GET.get('val1'))
    #     n2 = int(request.GET.get('val2'))

    #     result=n1 + n2
    # return render(request, "userform.html",{'output':result})
    
    """using post method"""
    if request.method== "POST":
       
        n1 = int(request.POST.get('val1'))
        n2 = int(request.POST.get('val2'))

        result=n1 + n2
    return render(request, "userform.html",{'output':result})


# def about_us(request):
#     return HttpResponse("<b>heloooo rahila sana</b>")
# def courses(request):
#     return HttpResponse(" rahila sana is provinding a web dev corurse")
# """concept of dynamic URLS/routing"""
# """it means page will remain same but data will be changed """

# def courseDetail(request,courseid):
#     return HttpResponse(f"this is my {courseid} course ")
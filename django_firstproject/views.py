from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import RegisterForm
from news.models import News ,Product

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
    #orm command
    # read operation , objects.all() is used to get all objects
    news_data=News.objects.all()
    
    return render(request,"home.html",{'news_data':news_data})

def news_detail(request,newsid):
    # here get is used for retreiving a single row
    newsDetail=News.objects.get(id=newsid)
    
    data={
        'newsdetail':newsDetail
        
    }
    return render(request,'detailed_page.html',data)


def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def categories(request):
    if request.method=="GET":
        result=request.GET.get('output')#q k url ma output name se a rhi hai value
    return render(request, "categories.html",{'result':result})

"""  __icontains use hota hai name mein search karne ke liye.
 Ye capital aur small letters ka farq nahi karta
 aur name ke kisi bhi part ko match kar leta hai.
 Example: "baby" search karne par "Baby Frock" bhi mil jayega."""
def products(request):
    search = request.GET.get('search', '')

    products = Product.objects.all()

    if search:
        products = products.filter(name__icontains=search) 
    return render(request, "products.html", {
        "products": products
    })

    
def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

    else:

        form = RegisterForm()

    return render(
        request,
        'register.html',
        {'form': form}
    )
    
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
    
        "how we can redirect + show any value in url using .format() the value of result will be in output"
        
        url=('/categories/?output={}'.format(result))
        return HttpResponseRedirect(url)
    
    return render(request, "userform.html",{'output':result})


# def about_us(request):
#     return HttpResponse("<b>heloooo rahila sana</b>")
# def courses(request):
#     return HttpResponse(" rahila sana is provinding a web dev corurse")
# """concept of dynamic URLS/routing"""
# """it means page will remain same but data will be changed """

# def courseDetail(request,courseid):
#     return HttpResponse(f"this is my {courseid} course ")

def transfer(request):
    return HttpResponse(request)
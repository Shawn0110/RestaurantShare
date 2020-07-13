from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("index")
    return render(request, 'shareRes/index.html')

def restaurantDetail(request):
    #return HttpResponse("restaurantDetail")
    return render(request, 'shareRes/restaurantDetail.html')

def restaurantCreate(request):
    #return HttpResponse("restaurantCreate")
    return render(request, 'shareRes/restaurantCreate.html')

def categoryCreate(request):
    #return HttpResponse("categoryCreate")
    return render(request, 'shareRes/categoryCreate.html')

def Create_category(request):
    category_name = request.POST['categoryName']
    new_category = Category(cagetory_name = category_name)
    new_category.save()
    return HttpResponse
    #return HttpResponse("여기서 category Create 기능을 구현")
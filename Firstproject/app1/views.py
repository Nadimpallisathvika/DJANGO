from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
def view1(request):
    # print(request.method)
    return HttpResponse("hello world i am from view1")
def view2(request):
    return HttpResponse("hello world i am from view2")
def view3(request):
    return HttpResponse("hello hi everyone")
def view4(request):
    return JsonResponse({"name":"sathwi","message":"hello"})
def view5(request):
    return JsonResponse({"status":"success","response":"welcome"})
def dynamicview(request):
    qp1=request.GET.get("name")
    return HttpResponse(f"hello {qp1}")
def personinfo(request):
    name=request.GET.get("name","saki"),
    city=request.GET.get("city","hyd"),
    role=request.GET.get("role","it")
    info={"name":name,"city":city,"role":role}
    return JsonResponse({"status":"success","data":info})
def ticket(request):
    movie=request.GET.get("movie","darling"),
    theratere=request.GET.get("theratere","AMB"),
    show=request.GET.get("show","firstshow"),
    timings=request.GET.get("timings","6pm")
    info={"movie":movie,"theratere":theratere,"show":show,"timings":timings}
    return JsonResponse({"status":"success","data":info})
def temp1(request):
    return render(request,"./simple.html")
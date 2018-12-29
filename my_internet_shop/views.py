from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    header = "Personal date"
    langs = ["rus", "by", "en"]
    user = {"name": "Petr", "age": 23}
    addr = ("Lenina", 34, 12)
    data = {"header": header, "user": user, "address": addr, "languages": langs}
    return render(request, "home.html", context=data)


def about(request):
    return render(request, "about.html")


def contacts(request):
    return render(request, "contacts.html")


# def products(request, productid=13):
#     output = "<h2>Product № {0}</h2>".format(productid)
#     return HttpResponse(output)


# def my_internet_shop(request, id=7, name="Ivan"):
#     output = "<h2>User</h2>" \
#              "<h3>id: {0}  name: {1}</h3>".format(id, name)
#     return HttpResponse(output)


def products(request, productid=3):
    category = request.GET.get("cat", "")
    output = "<h2>Product № {0}  Category: {1}</h2>".format(productid, category)
    return HttpResponse(output)


def users(request):
    id = request.GET.get("id", 7)
    name = request.GET.get("name", "Ivan")
    output = "<h2>User</h2>" \
             "<h3>id: {0}  name: {1}</h3>".format(id, name)
    return HttpResponse(output)


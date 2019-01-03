from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ProductForm


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


def products(request):
    if request.method == "POST":
        productForm = ProductForm(request.POST)
        if productForm.is_valid():
            # 
            id_product = productForm.cleaned_data["id"]
            name_product = productForm.cleaned_data["name_product"]
            count = productForm.cleaned_data["count"]
            product = {"id": id_product, "name": name_product, "count": count}
            return render(request, "product.html", context=product)
        else:
            return HttpResponse("Invalid data")

        # return render(request, "product.html", context=product)

    else:
        productForm = ProductForm()
        return render(request, "product_order.html", context={"form": productForm})


def users(request):
    id = request.GET.get("id", 7)
    name = request.GET.get("name", "Ivan")
    output = "<h2>User</h2>" \
             "<h3>id: {0}  name: {1}</h3>".format(id, name)
    return HttpResponse(output)


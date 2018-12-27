from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return HttpResponse("<h2>Главная</h2>")


def about(request):
    return HttpResponse("<h2>О нас</h2>")


def contacts(request):
    return HttpResponseRedirect("/about")


# def products(request, productid=13):
#     output = "<h2>Product № {0}</h2>".format(productid)
#     return HttpResponse(output)


# def users(request, id=7, name="Ivan"):
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


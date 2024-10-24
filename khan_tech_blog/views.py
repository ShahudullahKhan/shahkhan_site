from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item, ToDOList
from .forms import CreateNewList

# Create your views here.
def index(response, id):
    ls = ToDOList.objects.get(id=id)

    if ls in response.user.todolist.all():

        if response.method == "POST":
            print("response.POST", response.POST)
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("new")

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("Invalid!")

        return render(response, "khan_tech_blog/list.html", {"ls":ls})
    return render(response, "khan_tech_blog/view.html", {})


def home(response):
    return render(response, "khan_tech_blog/home.html", {})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDOList(name=n)
            t.save()
            response.user.todolist.add(t)

        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response, "khan_tech_blog/create.html", {"form":form})


def view(response):
    return render(response, "khan_tech_blog/view.html")
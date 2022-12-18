from django.shortcuts import render, redirect, reverse
from pygooglenews import GoogleNews

gn = GoogleNews()
s = gn.search('ukraine')

for entry in s["entries"]:
    print(entry["title"])


def home(request):

    return render(request, "home.html")

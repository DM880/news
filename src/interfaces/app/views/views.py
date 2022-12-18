from django.shortcuts import render, redirect, reverse
from pygooglenews import GoogleNews

# gn = GoogleNews()
# s = gn.search('ukraine')

# for entry in s["entries"]:
#     print(entry["title"])


def home(request):

    gn = GoogleNews(country="NZ")

    s = gn.search('new')
    latest = [()]

    for entry in s["entries"]:
        latest.append(entry['title'])
        print(entry["title"])



    return render(request, "home.html", {'latest':latest})

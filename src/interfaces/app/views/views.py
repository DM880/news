from django.shortcuts import render, redirect, reverse
from pygooglenews import GoogleNews

# gn = GoogleNews()
# s = gn.search('ukraine')

# for entry in s["entries"]:
#     print(entry["title"])


def home(request):

    gn = GoogleNews(country="NZ")
    # s = gn.top_news(proxies=None, scraping_bee = None)
    s = gn.search('', when="1d")
    latest = []
    # count = 0

    for entry in s["entries"]:
        # if count < 10:
        latest.append((entry['title'], entry['link']))
            # count += 1

    return render(request, "home.html", {'latest':latest})


def search_topic(request):

    if request.method == 'POST':

        topic = request.POST.get('topic')
        geo = request.POST.get('location')

        pass
    pass
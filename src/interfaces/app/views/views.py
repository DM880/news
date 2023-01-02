from django.shortcuts import render, redirect, reverse
from pygooglenews import GoogleNews


def home(request):

    gn = GoogleNews()
    s = gn.top_news()

    latest = []

    for entry in s["entries"]:
        latest.append((entry["title"], entry["link"], entry["published"]))

    latest.sort(key=lambda tup: tup[2]) #sort latest by newest

    return render(request, "home.html", {"latest": latest})


def search_topic(request):

    if request.method == "POST":

        keyword = request.POST.get("keyword")
        geo = request.POST.get("location")
        time = request.POST.get("time")
        language = request.POST.get("language")
        # topic = request.POST.get('topic') # unsure

        if not keyword or None and geo:
            gn = GoogleNews(lang=language, country=geo)
            s = gn.top_news()

        elif not geo or None and keyword:
            gn = GoogleNews(lang=language)
            s = gn.search(keyword)

        elif keyword and geo and not time or None:
            gn = GoogleNews(lang=language, country=geo)
            s = gn.search(keyword)

        else:
            gn = GoogleNews(lang=language, country=geo)
            s = gn.search(keyword, when=time)

        results = []

        for entry in s["entries"]:
            results.append((entry["title"], entry["link"]))

        return render(request, "search_results.html", {"results": results})





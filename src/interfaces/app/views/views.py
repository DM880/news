from django.shortcuts import render, redirect, reverse
from pygooglenews import GoogleNews


def home(request):

    google_news = GoogleNews()
    stories = google_news.top_news()

    stories_list = []

    for entry in stories["entries"]:
        stories_list.append(
            (entry["title"], entry["link"], entry["published"], entry["id"])
        )

    if request.method == "POST":
        sorting_element = request.POST.get("sorting_element")

        if sorting_element == "oldest":

            stories_list.sort(
                key=lambda tup: tup[2], reverse=True
            )  # sort stories_list by oldest

        else:

            stories_list.sort(key=lambda tup: tup[2])  # sort stories_list by latest

    return render(request, "home.html", {"stories_list": stories_list})


def search_topic(request):

    if request.method == "POST":

        keyword = request.POST.get("keyword")
        geo = request.POST.get("location")
        time = request.POST.get("time")
        language = request.POST.get("language")

        if not keyword or None and geo:
            google_news = GoogleNews(lang=language, country=geo)
            stories = google_news.top_news()

        elif not geo or None and keyword:
            google_news = GoogleNews(lang=language)
            stories = google_news.search(keyword)

        elif keyword and geo and not time or None:
            google_news = GoogleNews(lang=language, country=geo)
            stories = google_news.search(keyword)

        else:
            google_news = GoogleNews(lang=language, country=geo)
            stories = google_news.search(keyword, when=time)

        results = []

        for entry in stories["entries"]:
            results.append((entry["title"], entry["link"]))

        return render(request, "search_results.html", {"results": results})

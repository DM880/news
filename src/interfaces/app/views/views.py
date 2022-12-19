from django.shortcuts import render, redirect, reverse
from pygooglenews import GoogleNews


def home(request):

    gn = GoogleNews()
    s = gn.top_news()
    latest = []
    count = 0

    for entry in s["entries"]:
        if count < 12:
            latest.append((entry['title'], entry['link']))
            count += 1

    return render(request, "home.html", {'latest':latest})


def search_topic(request):

    if request.method == 'POST':

        topic = request.POST.get('topic')
        geo = request.POST.get('location')
        time = request.POST.get('time')

        if not topic or None and geo:
            gn = GoogleNews(country=geo)
            s = gn.top_news()

        elif not geo or None and topic:
            gn = GoogleNews()
            s = gn.search(topic)

        elif topic and geo and not time or None:
            gn = GoogleNews(country=geo)
            s = gn.search(topic)

        elif time and topic and geo:
            gn = GoogleNews()
            s = gn.search(topic, when=time)

        else:
            gn = GoogleNews(country=geo)
            s = gn.search(topic, when=time)

        results = []
        count = 0

        for entry in s["entries"]:
            if count < 12:
                results.append((entry['title'], entry['link']))
                count += 1

        return render(request, "search_results.html", {'results':results})



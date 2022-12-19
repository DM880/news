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

            results = []
            count = 0

            for entry in s["entries"]:
                if count < 12:
                    results.append((entry['title'], entry['link']))
                    count += 1
            return render(request, "search_results.html", {'results':results})

        elif not geo or None and topic:
            gn = GoogleNews()
            s = gn.search(topic)

            results = []
            count = 0

            for entry in s["entries"]:
                if count < 12:
                    results.append((entry['title'], entry['link']))
                    count += 1
            return render(request, "search_results.html", {'results':results})

        elif topic and geo and not time or None:

            gn = GoogleNews(country=geo)
            s = gn.search(topic)

            results = []
            count = 0

            for entry in s["entries"]:
                if count < 12:
                    results.append((entry['title'], entry['link']))
                    count += 1
            return render(request, "search_results.html", {'results':results})


        elif time and topic and geo:
            gn = GoogleNews()
            s = gn.search(topic, when=time)
            count = 0

            for entry in s["entries"]:
                if count < 12:
                    results.append((entry['title'], entry['link']))
                    count += 1

            return render(request, "search_results.html", {'results':results})

        return redirect(reverse('search_results', args=(topic,geo,time)))


def search_results(request, topic, geo, time):

    gn = GoogleNews(country=geo)
    s = gn.search(topic, when=time)
    results = []
    count = 0

    for entry in s["entries"]:
        if count < 12:
            results.append((entry['title'], entry['link']))
            count += 1

    return render(request, "search_results.html", {'results':results})


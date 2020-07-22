import operator


from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.POST['fulltext'].lower()
    wordlist = fulltext.split()
    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] = 1

    sorted_words = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {"fulltext":fulltext, "count": len(wordlist), "sorted_words": sorted_words})


def whatthis(request):
    return render(request,"whatthis.html")
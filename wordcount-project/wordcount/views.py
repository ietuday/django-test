from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'hithere': 'This is me'})


def count(request):
    fullText = request.GET['fullText']
    wordList = fullText.split()
    worddictionary = {}
    for word in wordList:
        if word in worddictionary:
            # Increase Count
            worddictionary[word] += 1
        else:
            # Add to the dictionary
            worddictionary[word] = 1
    return render(request, 'count.html', {'fullText': fullText, 'count': len(wordList), 'worddictionary': worddictionary.items()})

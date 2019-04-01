from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request,'home.html')

def count(request):
    result = request.GET['fulltext']
    wordlist = result.split()

    wordscount ={}

    for word in wordlist:
        if word in wordscount:
            wordscount[word] += 1
        else :
            wordscount[word] = 1

    sortedWords = sorted(wordscount.items(), key = operator.itemgetter(1), reverse= True)

    return render(request,'count.html',{'words':result, 'count':len(wordlist), 'sortedWords' : sortedWords })

def about(request):
    return render(request,'about.html')

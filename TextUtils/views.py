# I have created this file - Suryakant Vishal
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the Text
    djtext = request.POST.get('text', 'default')

    # Check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # Check which check =box is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose':'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()

        params = {'purpose': 'Change to UpperCase', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed += char

        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed += char

        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}

    if removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on":
        return HttpResponse('Error')

    return render(request, 'analyze.html', params)


# def capfirst(request):
#     return HttpResponse('Capitalize First')
#
# def newlineremove(request):
#     return HttpResponse("Remove New Lines")
#
# def spaceremove(request):
#     return HttpResponse("Remove Spaces")
#
# def charcounter(request):
#     return HttpResponse("Count Character")
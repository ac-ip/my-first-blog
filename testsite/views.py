from django.shortcuts import render

def testsitepost_list(request):
    return render(request, 'testsite/testsitepost_list.html',{})

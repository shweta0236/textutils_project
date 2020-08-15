# this file is created by - Shweta

#render function :- render(request, template_name, context=None, content_type=None, status=None, using=None)¶
    #Combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.
    #Django does not provide a shortcut function which returns a TemplateResponse because the constructor of TemplateResponse offers the same level of convenience as render().

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html',{'name':'shweta'})

def about(request):
    return render(request,'about.html')

def contact_us(request):
    return render(request,'contact_us.html')

def analyzer(request):
    #get data from textarea in text_analyzer.html
    djtext = request.POST.get('text','default')

    #get data from index.html
    remove_punctuation = request.POST.get('rp','off')
    remove_newline = request.POST.get('remove_newline', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    remove_space = request.POST.get('remove_space', 'off')
    count_char = request.POST.get('count_char', 'off')

    #check value of checkbox
    if(remove_punctuation == "on"):
        new_text = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations or char == '\n':
                new_text = new_text + char

        para = {'purpose':'Remove Punctuation', 'analyzed_text':new_text}
        djtext = new_text

    if (uppercase == "on"):
        new_text = ""
        for char in djtext:
            new_text = new_text + char.upper()
        para = {'purpose': 'Uppercase', 'analyzed_text': new_text}
        djtext = new_text


    if (remove_space == "on"):
        new_text = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                new_text = new_text + char
        para = {'purpose': 'Remove Space', 'analyzed_text': new_text}
        djtext = new_text


    if (remove_newline == "on"):
        new_text = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                new_text = new_text + char

        para = {'purpose': 'Remove Newline', 'analyzed_text': new_text}
        djtext = new_text

    if (count_char == "on"):
        new_text = 0
        for char in djtext:
            if char != " " and char != '\n' and char != '\r':
                new_text += 1
        count = str(new_text)
        para =   {'purpose': 'char Counter', 'analyzed_text':count }

    if (remove_space != "on" and remove_newline != "on" and count_char != "on" and remove_punctuation != "on" and uppercase != "on"):
        return HttpResponse("Please select operation")

    return render(request, 'analyzer.html',para)



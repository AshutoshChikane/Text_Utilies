from string import punctuation
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def analysis(request):
    djtext = request.GET.get('text', 'default')
    djpunc = request.GET.get('punc', 'off')
    djcap = request.GET.get("cap", "off")
    djdspace = request.GET.get("dspace", "off")
    djline = request.GET.get("line", "off")
    conditionList = []
    print(djtext, djpunc)
    if (djpunc == "on" or djcap == "on" or djdspace == "on" or djline == "on") and djtext != "":
        if djpunc == "on":
            punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
            analysed_text = ""
            for i in djtext:
                if i not in punctuations:
                    analysed_text += i
                    # print(analysed_text)
            djtext = analysed_text
            con = "Text after removing Punctuations"
            conditionList.append(con)

        if djcap == "on":
            analysed_text = djtext.upper()
            djtext = analysed_text
            con = "Text after Capitalization"
            conditionList.append(con)

        if djline == "on":
            a = ""
            for i in djtext:
                if i == "\n":
                    a += ""
                elif i == "\r":
                    a += ""
                else:
                    a += i
            print(a)
            djtext = a
            con = "remove new line"
            conditionList.append(con)
        if djdspace == "on":
            analysed_text = ""
            for i in range(len(djtext)):
                if djtext[i] == " " and djtext[i+1] == " ":
                    continue
                else:
                    analysed_text += djtext[i]
            djtext = analysed_text
            con = "Text after removing double space"
            conditionList.append(con)

        a = {"result": djtext, "condition": conditionList}
        return render(request, 'analyzed.html', a)

    elif djtext == "":
        a = "no text found"
        b = {"a": a}
        return render(request, 'error.html', b)
    else:
        a = "no action selected"
        b = {"a": a}
        return render(request, 'error.html', b)


# punctuation
# CAptialize
# double spacing

# from string import punctuation
# from django.shortcuts import render
# from django.http import HttpResponse


# def home(request):
#     return render(request, 'home.html'


# def analysis(request):
#     djtext = request.GET.get('text', 'default')
#     djpunc = request.GET.get('punc', 'off')
#     djcap = request.GET.get("cap", "off")
#     djdspace = request.GET.get("dspace", "off")
#     djlength = request.GET.get("length", "off")

#     print(djtext, djpunc)
#     if djpunc == "on":
#         punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
#         analysed_text = ""
#         for i in djtext:
#             if i not in punctuations:
#                 analysed_text += i
#                 print(analysed_text)
#         aa = {'condition': "Text after removing Punctuations",
#               "result": analysed_text}
#         return render(request, "analyzed.html", aa)

#     elif djcap == "on":
#         analysed_text = djtext.upper()
#         aa = {'condition': "Text after Capitalization",
#               "result": analysed_text}
#         return render(request, "analyzed.html", aa)
#     elif djdspace == "on":
#         analysed_text = ""
#         for i in range(len(djtext)):
#             if djtext[i] == " " and djtext[i+1] == " ":
#                 continue
#             else:
#                 analysed_text += djtext[i]

#         aa = {'condition': "Text after removing double space",
#               "result": analysed_text}
#         return render(request, "analyzed.html", aa)

#     elif djlength == "on":
#         analysed_text = len(djtext)
#         aa = {'condition': "Total length of text",
#               "result": analysed_text}
#         return render(request, "analyzed.html", aa)

#     else:
#         return HttpResponse('<h1>Error</h1>')

# punctuation
# CAptialize
# double spacing

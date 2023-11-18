from fileinput import filename
from http.client import HTTPResponse
from urllib import request
from django.shortcuts import render, redirect
import markdown
import random

from . import util
import encyclopedia


def convert_md_to_html(title):
    content = util.get_entry(title)
    # converted = markdown.markdown(content)

    if content == None:
        return None
    else:
        return markdown.markdown(content)
           # return markdowner.convert(content)
        # return converted


def index(request):
    entries = util.list_entries()
    # css_file = util.get_entry("CSS")

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()

    })


def entry(request, title):
    html_content = convert_md_to_html(title)
    if html_content == None:
        return render(request, "encyclopedia/404.html")
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })


def search(request):
    entry_search = request.GET.get('q', '').strip()

    if util.get_entry(entry_search) is not None:
        content = convert_md_to_html(entry_search)
        return render(request, "encyclopedia/entry.html", {
            "title": entry_search,
            "content": content,
        })
    else:
        recommendation = [entry for entry in util.list_entries() if entry_search.lower() in entry.lower()]
        return render(request, "encyclopedia/search.html", {"recommendation": recommendation})


#
# def new_page(request):
#     if request.method == "GET":
#         return render(request, "encyclopedia/new.html")
#     else:
#         title = request.POST['title']
#         content = request.POST['content']
#         titleExist = util.get_entry(title)
#         if titleExist is not None:
#             return render(request, "encyclopedia/error.html", {"message": "Entry already exist"})
#         else:
#             util.save_entry(title, content)
#             html_content = convert_md_to_html(title)
#             return render(request, "encyclopedia/entry.html", {
#                 "title": title,
#                 "content": html_content
#             })
#
#         # return render(request, "encyclopedia)
#
#
# def edit(request):
#     if request.method == "POST":
#         title = request.POST['title']
#         content = util.get_entry(title)
#         return render(request, "encyclopedia/edit.html", {"title": title, "content": content})
#
#
# def saveEdit(request):
#     if request.method == "POST":
#         title = request.POST['entry_title']
#         content = request.POST['content']
#         util.save_entry(title, content)
#         html_content = convert_md_to_html(title)
#         return render(request, "encyclopedia/entry.html",
#                       {
#                           "title": title,
#                           "content": content,
#                       })
#
#
# def rando(request):
#     allEntries = util.list_entries()
#
#     randomentry = random.choice(allEntries)
#     html_content = convert_md_to_html(randomentry)
#     return render(request, "encyclopedia/entry.html", {
#         "title": randomentry,
#         "content": html_content,
#     })
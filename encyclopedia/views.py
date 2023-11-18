from django.shortcuts import render

from markdown2 import Markdown

from . import util

def convert_md_html(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request,  title):
    content = convert_md_html(title)
    if content == None:
        return render(request, "encyclopedia/404.html", {
            "message": "Entry Not Found",
            "callToAction": "Create one"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": content
        })

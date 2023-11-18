from django.shortcuts import render
from markdown2 import Markdown
from . import util

def covnvert_md_html(title):
    content = util.get_entry(title)
    markdower = Markdown()
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request,  title):
    return

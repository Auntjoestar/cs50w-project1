from django.shortcuts import render
from markdown2 import Markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entries(request, title):
    utilAnswer = util.get_entry(title)
    if utilAnswer is not None:
        return render(request, "encyclopedia/entries.html",{
            "content": Markdown().convert(util.get_entry(title)),
            "title" : title
            })
    else:
        return render(request, "encyclopedia/error.html",{
            "content": "Error 404: Page Not Found",
            "title" : "Error 404"
            })
        
    


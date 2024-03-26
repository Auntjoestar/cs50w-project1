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
    
def search(request):
    query = request.GET.get("q")
    entries = util.list_entries()
    filteredEntries = []
    matchCount = []

    for entry in entries:
        if query.lower() == entry.lower():
            matchCount.append(entry)
    
    if len(matchCount) == 0:
        for entry in entries:
            if query.lower() in entry.lower():
                filteredEntries.append(entry)
        if len(filteredEntries) == 0: 
            return render(request, "encyclopedia/not_found.html",{
                    "content": "A matching entry was not found, maybe you misspelled something?",
                    "title" : "Page Not Found"
                    })
        return render(request, "encyclopedia/search.html",{
                    "entries" : filteredEntries
                    })

    if len(matchCount) >= 2:
        return render(request, "encyclopedia/matches.html",{
            "entries" : matchCount,
            "query" : query
            })
    return render(request, "encyclopedia/entries.html",{
            "content": Markdown().convert(util.get_entry(matchCount[0])),
            "title" : query
            })
    
    
            

        
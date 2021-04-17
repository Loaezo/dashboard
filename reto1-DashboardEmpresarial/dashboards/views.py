#django
from django.shortcuts import render

# Create your views here.
"""Views"""

#from django.http import HttpResponse
from datetime import datetime


#def list_dashboards(request):
posts =[
    {
        'name' : 'Gatin',
        'user' : 'tuchi',
        'timestamp' : datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    }
]

def list_dashboards(request):
    """List existing posts"""
    return render(request,'feed.html',{'posts' : posts})
#    """List existing dashboards"""
#    content = []
#    for post in posts:
#        content.append("""<p><strong>{name}<s/trong></p>""")
#    return HttpResponse(str(posts))

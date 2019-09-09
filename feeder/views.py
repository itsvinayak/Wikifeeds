from django.shortcuts import render
import wikipedia
from .models import Data

def index(request):

    #getting wikipedia page at random
    try:
        source = wikipedia.page(wikipedia.random(pages=1))

        #getting data
        title = source.title
        img = source.images[0]
        url = source.url
        text = source.content

        data=Data.objects.create(title=title,img=img,url=url,text=text)
        data.save()
    except:
        pass

    feed_data = Data.objects.all()[:20:-1]
    data={
              'data':feed_data,
         }


    return render(request,'feeder/index.html',data)

def about(request):
    return render(request,'feeder/about.html')

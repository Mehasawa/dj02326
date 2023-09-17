from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,'index.html')

def shok(req,name):
    if name == 'mars':
        k1='Mars'
        k2 = 'img/mars.png'
        k3 = 'шоколадка марс'
    elif name == 'snickers':
        k1='Snickers'
        k2 = 'img/snickers.jpg'
        k3 = 'не тормози сникерсни'
    elif name == 'bounty':
        k1 = 'Bounty'
        k2 = 'img/bounty.jpg'
        k3 = 'баунти райское наслаждение'
    data={'title':k1,'pic':k2,'desc':k3}
    return render(req,'shoko.html',data)
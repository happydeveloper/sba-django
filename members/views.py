from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Members

# Create your views here.
def index(req):
    #print(dir(req))
    print(req.GET.get('id',''))
    num = req.GET.get('id','') 
    return HttpResponse(f"<h2> input data : {squred(num)}</h2>")

def squred(i):
    return int(i) * int(i)

def test(req):
    return HttpResponse("<h2>Test</h2>")

def signup(req):
    if req.method == 'POST' :
        username = req.POST['username']
        email = req.POST['email']

        member = Members(
            username = username,
            useremail = email
        )
       
        member.save()
        res_data = {}
        res_data['res'] = '등록성공'
        return render(req, 'index.html', res_data)

    return render(req, 'index.html') 

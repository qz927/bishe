from django.shortcuts import render,HttpResponse,redirect
from book.models import Book,bookinfo,stuinfo
from django.forms import ModelForm
#create your views here .
from django import  forms
class BookForm(forms.ModelForm):
    class Meta:
        model =bookinfo
        fields=["name","author","price"]
def index(request):
    books =bookinfo.objects.all()
    return render(request,"index.html",{"books":books})
def add(request):
    if request.method == "GET":
        b_obj= BookForm()
        return render(request,"add.html",{"b_obj":b_obj})
    else:
        b_obj=BookForm(request.POST)
        if b_obj.is_valid():
            b_obj.save()
        return redirect("/index/")
def edit(request):
    id = request.GET.get('id')
    book = bookinfo.objects.get(id=id) #取山id 值对应的书籍对象
    if request.method == 'GET':
        b_obj = BookForm(instance=book) #这一步实例化的时候，需要传入书籍对象，生成表单的时候就会默认填充这些数据
        return render(request, 'edit.html', {'b_obj': b_obj})
    else:
        b_obj = BookForm(instance=book, data=request.POST) # 此处需要传入编辑的书籍对象，和提交的数据
        if b_obj.is_valid():
            b_obj.save()
        return redirect('/index/')
#删除书籍（常规操作）
def delete(request):
    id = request.GET.get('id') # 获取要删除的书籍的 id
    book = bookinfo.objects.get(id=id) # 取出 id 值对应的书籍对象
    book.delete() #从数据库中刑除这个书籍对象
    return redirect('/index/')
def login(request):
    return render(request,"login.html")
def login_ok(request):
    return render(request,'login_ok.html')
def login1(request):
    return render(request,"login1.html")
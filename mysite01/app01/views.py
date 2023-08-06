from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("欢迎使用")


def user_list(request):
    # 如果settings没加os.templates这句话，就先去根目录的templates里找
    # 根据app的注册顺序，逐一去它们的templates寻找）
    # 默认都是去 app 目录下的templates目录寻找user_list.html
    return render(request, "user_list.html")


def user_add(request):
    return HttpResponse("添加用户")


def tpl(request):
    name = "Elena"
    roles = ['1', '2', 3]
    user_info = {
        "name": "Elena",
        "salary": 10000,
        "role": "CTO"
    }
    data_list = [
        {"name": "Elena", "salary": 10000, "role": "CTO"},
        {"name": "Elena", "salary": 10000, "role": "CTO"},
        {"name": "Elena", "salary": 10000, "role": "CTO"},
    ]
    return render(request,
                  'tpl.html',
                  {"n1": name, 'n2': roles, 'n3': user_info, 'n4': data_list})


def something(request):
    # request是一个对象，封装了用户通过浏览器发来的所以请求相关数据
    # 获取请求方式
    print(request.method)

    # 关于重定向：浏览器被redirect后，把网站发回请求者，请求者再访问新的网站
    return HttpResponse('返回内容')


def login(request):
    if request.method == 'GET':
        return render(request, "login.html")
    else:
        print(request.POST)
        username = request.POST.get("user")
        password = request.POST.get("password")
        if username == 'root' and password == "123":
            return HttpResponse("登录成功")
        else:
            # return HttpResponse("登录失败")
            return render(request, "login.html", {"error_msg": "Incorrect password"})

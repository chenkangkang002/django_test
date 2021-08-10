from django.shortcuts import render, redirect

# Create your views here.
from login import models, forms
from login.utils.utils import hash_code


def index(request):
    if not request.session.get('is_login', None):
        return redirect('/u/login/')
    return redirect('/b/')

def login(request):
    if request.session.get('is_login',None):
        return redirect('/b/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        message = False
        # if username.strip() and password.strip():
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            try:
                user = models.User.objects.get(u_name=username)
            except:
                message = '用户还未注册'
                return render(request, 'login/login.html', locals())
            if hash_code(password) == user.password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.u_name
                return redirect('/b/')
            else:
                message = '密码错误'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())
    login_form = forms.UserForm()
    return render(request,'login/login.html',locals())

def register(request):
    if request.session.get('is_login',None):
        return render(request,'booktest/index.html')
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = False
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')
            if password1 != password2:
                message = '两次密码不一致'
                render(request, 'login/register.html', locals())
            else:
                same_name = models.User.objects.filter(u_name=username)
                if same_name:
                    message = '用户已注册'
                    render(request, 'login/register.html', locals())
                same_email = models.User.objects.filter(email=email)
                if same_email:
                    message = '邮箱已注册'
                    render(request, 'login/register.html', locals())

                new_user = models.User()
                new_user.u_name = username
                new_user.password = hash_code(password2)
                new_user.email = email
                new_user.sex = sex
                new_user.save()

                user = models.User.objects.get(u_name=username)
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.u_name

                return redirect('/b/')
        else:
            message = '请检查输入的内容'
            render(request, 'login/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html',locals())

def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/u/login/')
    request.session.flush()
    return redirect('/u/login/')

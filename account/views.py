from django.contrib.auth import authenticate
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm   # 로그인 폼, 회원가입 폼
from django.contrib.auth import login, logout
from account.forms import RegisterForm
from account.models import CustomUser
from django.contrib import messages


def login_view(request):
    if request.method =='POST':
        auth_form = AuthenticationForm(request=request, data = request.POST)
        if auth_form.is_valid(): #계정이 존재하지 않을때 혹은 비밀번호가 틀렸을때
            v_username = auth_form.cleaned_data.get('username')
            v_password = auth_form.cleaned_data.get('password')
            auth_user = authenticate(request=request, username = v_username, password = v_password)
            login(request, auth_user)
            return redirect('urlnamehome')
        else:
            if CustomUser.objects.filter(username =  request.POST['username']).exists():
                messages.info(request, '비밀번호가 일치하지않습니다.')
                return redirect('urlnamelogin')
            else:
                messages.info(request, '존재하지 않는 계정입니다.')
                return redirect('urlnamelogin')
    else:
        login_form = AuthenticationForm()
        return render (request, 'login.html', {'views_login_form':login_form})

def signup_view(request):
    if request.method == 'POST':
        new_signup_form = RegisterForm(request.POST)
        if new_signup_form.is_valid():
            user = new_signup_form.save()
            login(request, user)
            return redirect('urlnamehome')
        else:
            if CustomUser.objects.filter(phone_number = request.POST['phone_number']).exists(): #저장소의 객체들 중에서 필터를 거친다.
                messages.info(request, '하나의 핸드폰 번호는 하나의 계정만 생성할 수 있습니다.') #다른 곳에서 핸드폰 번호를 가져왔기 때문에 일단 일빠로 유효성 검사를 해주자! 그러면 되긴 해
                return redirect ('urlnamesignup')

            elif request.POST['password1'] != request.POST['password2']:
                messages.info(request, '비밀번호와 비밀번호 확인이 일치하지않습니다.')
                return redirect ('urlnamesignup')   

            elif len(request.POST['password1']) < 8 :
                messages.info(request, '비밀번호는 8자리 이상으로 작성해주세요.')
                return redirect ('urlnamesignup') 
            
            elif request.POST['password1'].isdigit() :
                messages.info(request, '비밀번호는 숫자로만 이루어질 수 없습니다.')
                return redirect ('urlnamesignup') 

            elif request.POST['username'] in request.POST['password1'] :
                messages.info(request, '비밀번호에 아이디가 포함될 수 없습니다.')
                return redirect ('urlnamesignup') 

            elif CustomUser.objects.filter(student_id =  request.POST['student_id']).exists(): 
                messages.info(request, '하나의 학번은 하나의 계정만 생성할 수 있습니다.')
                return redirect ('urlnamesignup') 
            
            elif CustomUser.objects.filter(username =  request.POST['username']).exists(): 
                messages.info(request, '중복되는 아이디가 존재합니다.')
                return redirect ('urlnamesignup') 
            
            else: 
                messages.info(request, '알 수 없는 에러입니다. 관리자에게 문의해주세요.')
                return redirect ('urlnamesignup') 
    else:
        signup_form = RegisterForm()
        return render(request, 'signup.html',{'views_signup_form':signup_form})

def logout_view(request):
    logout(request)
    return redirect('urlnamehome')
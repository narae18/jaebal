import re
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from django.db.models import Q

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('main:mainpage')
        else:
            return render(request,'accounts/login.html')
        
    elif request.method == "GET":
        return render(request, 'accounts/login.html')

# def login(request):
#         if request.method == "POST" :
#             username = 'guest';
#             password = 'simbaton'

def logout(request):
    auth.logout(request)
    return redirect("main:mainpage")   

def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        nickname = request.POST['nickname']
        gender = request.POST['gender']
        birth = request.POST['birth']
        year = birth[:4]
        month = birth[4:6]
        day = birth[6:]
        birth = f'{year}-{month}-{day}'
        college = request.POST['college']
        department = request.POST['department']
        email = request.POST['email']


        if not re.match(r'^[a-zA-Z0-9_-]{4,16}$', request.POST['username']):
            messages.error(request, '유효한 아이디 형식이 아닙니다.')
            return redirect('accounts:signup')

        if not re.match(r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', request.POST['password']):
            messages.error(request, '비밀번호는 영문자, 숫자, 특수문자(@$!%*?&)를 모두 포함하여 8자 이상 입력해야 합니다.')
            return redirect('accounts:signup')

        if request.POST['password'] != request.POST['confirm']:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
            return redirect('accounts:signup')

        if User.objects.filter(Q(username=request.POST['username']) | Q(email=request.POST['email'])).exists():
            messages.error(request, '이미 사용 중인 ID 또는 이메일입니다.')
            return redirect('accounts:signup')

        try:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            user.save()

            # 추가 필드 정보 저장
            profile = Profile(
                user=user,
                name=name,
                nickname=nickname,
                gender=gender,
                birthday=birth,
                college=college,
                department=department,
                email = email,
            )
            profile.save()

            auth.login(request, user)
            messages.success(request, '회원 가입이 완료되었습니다.')
            return redirect('main:mainpage')
        except Exception as e:
            messages.error(request, '회원 가입 중 오류가 발생했습니다. 다시 시도해주세요.')

    return render(request, 'accounts/signup.html')

def deleteUser(request):
    user = request.user
    user.delete()
    return redirect('main:mainpage')
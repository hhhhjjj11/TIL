# 학습한내용
- 인증관련 기능 : 로그인, 로그아웃, 회원가입, 회원탈퇴, 회원정보수정, 비밀번호변경

# 새로 배운 것들 및 느낀점
- 비밀번호 변경 기능 구현 연습을 충분히 해보지 않았던 것 같다. (폼 사용 및 미들웨어 코드 작성) 
- 확실히 관통프로젝트를 하면서 배운것들을 다시 다져보고, 되돌아보며 연습할 수 있어서 좋은 것 같다. 그리고 처음부터 지금까지 점점 기능을 추가해가면서 할줄 아는게 늘었다는 점이 기분 좋다.


# 비밀번호 변경 기능 
1. 다른 인증 폼들 처럼, 비밀번호 변경 폼 또한 빌트인 모델폼을 쓴다는 점.
```python
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
```
2. 수정과 비슷한 느낌이기 때문에 폼의 인자로 기존정보와 새로받은 데이터를 모두 넣어 주어야 한다는 점. 

3. 비밀번호를 건들면 세션이 삭제되기때문에, 빌트인 메서드를 불러와서 세션을 유지시켜준다는 점.

4. 미들웨어 코드
```python
def password(req):
    if req.method == "POST":
        # 수정과 비슷한 느낌이기 때문에 폼의 인자로 기존정보와 새로받은 데이터를 모두 넣어 주어야 한다는 점. 
        form = PasswordChangeForm(req.user, req.POST)
        if form.is_valid():
            form.save()
            # 비밀번호를 건들면 세션이 삭제되기때문에, 빌트인 메서드를 불러와서 세션을 유지시켜준다는 점.
            update_session_auth_hash(req, form.user)
            return redirect('movies:index')
    else:
        # get요청시에도, 정보수정 때와 마찬가지로, 기존 정보를 담아서 프론트로 보내주어야 한다.
        form = PasswordChangeForm(req.user) 
    context = {
        'form':form
    }
    return render(req, 'accounts/change_password.html',context)
```
   
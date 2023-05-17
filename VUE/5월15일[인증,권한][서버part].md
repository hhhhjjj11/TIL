# DRF Auth System
## Authentication , Authorization
1. Authentication : 인증 (로그인ㄱㄱ)
2. Authorization : 권한 (로그인되어있는가?)
## Authentication 
- 프레임워크마다 다양한 인증방법이 있다.
- 우리가 사용할 방법 : TokenAuthentication
(DRF가 기본으로 제공)
- 참고. 모든 상황에 대한 인증 방식을 정의 하는 것이므로, 각 요청에 따라 다른 인증 방식을 거치고자 한다면 다른 방식이 필요 -> 데코레이터 활용

## TokenAuthentication 사용해보기
1. INSTALLED_APPS에 'rest_frame.authtoken' 등록
2. settings.py에 다음 코드 추가
    ```python
    REST_FRAMEWORK = {
        # Authentication
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.TokenAuthentication',
        ],
    }
    ```
3. $ pip install dj-rest-auth
   ```
   $ pip install dj-rest-auth
   ```
4. INSTALLED_APPS에 'dj_rest_auth'추가
5. urls.py에
    ```python
    path('accounts/', include('dj_rest_auth.urls')),
    ```
6. db날리고 마이그레이션 초기화 한 후 다시 마이그레이션 하고 서버 키기 
[여기까지하면, 회원가입 추가가 안되어있어서 회원가입까지 추가하려면 다음 진행]
1. $ pip install 'dj-rest-auth[with_social]'
2. INSTALLED_APPS에 추가
    ```
        'django.contrib.sites',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'dj_rest_auth.registration',
    ```
3. settings.py에 다음 코드 추가
    ```python
    REST_AUTH={ # 회원가입시 토큰 발급
        'SESSION_LOGIN': False,
    }

    SITE_ID = 1
    # 하나의 컨텐츠로 여러 개의 도메인에 등록하고 싶을 때 사용
    ```
4. ulr.py에 추가
    ```python
    path('accounts/signup/', include('dj_rest_auth.registration.urls'))
    ```
5.  설정이 바꼈으므로 python manage.py migrate 다시 해주기 (뭔설정이바꼇단거지)
6.  서버켜보면 이제 /accounts/signup이 생겨있음
7.  가서 회원가입진행하면 key(통행증)를 줌 , 이것을 메모해두자
8.  이제 비밀번호를 변경해보자 
9.  포스트맨이용 ㄱㄱ
10. `http://127.0.0.1:8000/accounts/password/change/` 로 POST요청
11. [주의] new_password1, new_password2 는 body에, Authorization는 Headers에 넣는다.
12. Body,
{
 new_password1 : 새비번
  new_password2:  새비번
}
1.  Headers
{
 Authorization : Token 회원가입하고받은토큰
}
- 이때 주의, Token쓰고 한칸띈 다음에 넣어줘야함!!!!

<br><br>

# 권한해보자
1. settings.py에 코드추가
    ```python
    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': [
            # 'rest_framework.permissions.IsAuthenticated',
            'rest_framework.permissions.AllowAny',
        ],
    }
    ```
2. view에서 데코레이터 import
    ```python
    from rest_framework.decorators import permission_classes
    from rest_framework.permissions import IsAuthenticated
    ```
3. 로그인이 필요한 함수에 데코레이터추가
    ```python
    @api_view(['GET', 'POST'])
    @permission_classes([IsAuthenticated])
    def article_list(request):
        if request.method == 'GET':
            # articles = Article.objects.all()
            articles = get_list_or_404(Article)
            serializer = ArticleListSerializer(articles, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = ArticleSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                # serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

    ```
4. 포스트맨으로 테스트해보자
5. POST, http://127.0.0.1:8000/api/v1/articles/
6. 로그인이 필요하도록 설정해놨으므로,
Body 에 title, content를 넣어도
 Headers에 Authorization을 넣지 않으면 에러가남. Authorization을 써주면 제대로 등록됨.

<br><br>

## 정리 
1. 인증 방법 설정
   - DEFAULT_AUTHENTICATION_CLASSES
2. 권한 설정하기
   - DEFAULT_PERMISSION_CLASSES
3. 인증방법, 권한 세부 설정도 가능
   - @authentication_classes
   - @permission_classes
4. 인증방법은 다양한 방법이 있으므로 내 서비스에 적합한 방식을 선택한다.

<br><br>


# 유저필드 커스터마이징하기
## 1. 유저모델 작성
```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # 여기다가 닉네임필드 만들구
    nickname = models.CharField(max_length=50)

# 상속 받아서 구현해보기
from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    # 기본 코드는 다 그대로 쓰고, save_user 만 오버라이딩 하겠다!
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_email, user_field, user_username

        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        # nickname 필드
        nickname = data.get("nickname")

        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        # 닉네임 필드 추가
        if nickname:
            user_field(user, "nickname", nickname)

        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        return user
```
## 2. settings.py에서 설정 추가
```python
# dj-rest-auth는 email을 필수적으로 사용하도록 구현되어 있으므로, 해당 사항을 수정
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = None

# django 인증 시스템에서 사용할 백엔드 클래스 지정
# 기본 인증 백엔드와 allauth 패키지에서 제공하는 인증 백엔드를 모두 사용하겠다는 설정.
AUTHENTICATION_BACKENDS=(
    # django 기본 인증 백엔드
    "django.contrib.auth.backends.ModelBackend",
    # django-allauth 패키지에서 제공하는 인증 백엔드 클래스
    "allauth.account.auth_backends.AuthenticationBackend",
)

# dj_rest_auth 의 설정
REST_AUTH = {
    'REGISTER_SERIALIZER': 'accounts.serializers.RegisterSerializer',
}

# allauth 의 default adapter 설정
ACCOUNT_ADAPTER = 'accounts.models.CustomAccountAdapter'

```
- 마이그레이션 다시하기~

## [참고] dj-rest-auth 기능
1. accounts/ password/reset/ [name='rest_password_reset']
- 패스워드 초기화 (이메일로 전송)
3. accounts/ password/reset/confirm/[name='rest_password_reset_confirm']
- 패스워드 초기화(이메일 확인 후 초기화 페이지)
5. accounts/ login/ [name='rest_login']
6. accounts/ logout/ [name='rest_logout']
7. accounts/ user/ [name='rest_user_details']
8. accounts/ password/change/[name='rest_password_change']
- 패스워드변경
10. accounts/signup/
- 회원가입

## 3. serializers.py 작성
```python
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers
from allauth.utils import email_address_exists, get_username_max_length
from allauth.account import app_settings as allauth_account_settings
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from django.utils.translation import gettext_lazy as _

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=get_username_max_length(),
        min_length=allauth_account_settings.USERNAME_MIN_LENGTH,
        required=allauth_account_settings.USERNAME_REQUIRED,
    )
    email = serializers.EmailField(required=allauth_account_settings.EMAIL_REQUIRED)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    # 추가~
    nickname = serializers.CharField(max_length=50)

    def validate_username(self, username):
        username = get_adapter().clean_username(username)
        return username

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_account_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _('A user is already registered with this e-mail address.'),
                )
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(_("The two password fields didn't match."))
        return data

    def custom_signup(self, request, user):
        pass

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            # 추가~
            'nickname': self.validated_data.get('nickname', ''),
        }

    def save(self, request):
        # allauth 의 기본 adaper 를 가져옴
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        # 기본 adaper 의 save_user 는 nickname 필드를
        # 저장하지 않는다!
        user = adapter.save_user(request, user, self, commit=False)
        if "password1" in self.cleaned_data:
            try:
                adapter.clean_password(self.cleaned_data['password1'], user=user)
            except DjangoValidationError as exc:
                raise serializers.ValidationError(
                    detail=serializers.as_serializer_error(exc)
            )
        user.save()
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user
```
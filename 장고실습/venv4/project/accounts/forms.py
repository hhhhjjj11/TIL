from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# 유저모델 불러오는 전용 메서드 임포트.
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # 메타클래스 인자로 UerCreationForm.Meta를 넣어줘야 나머지는 그대로이고 model만 오버라이딩 됨. 저거 넣지 않으면 아예 전체를 새로 정의하는 것임.
        model = get_user_model()

# 수정전용 폼이 따로 있음 주의
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        # 메타클래스 인자로 UerCreationForm.Meta를 넣어줘야 나머지는 그대로이고 model만 오버라이딩 됨. 저거 넣지 않으면 아예 전체를 새로 정의하는 것임.
        model = get_user_model()
        fields= ('username', 'email','first_name','last_name')
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'name', 'student_id', 'major', 'phone_number']

        labels = {
            'username' : '아이디',
            'name' : '이름',
            'student_id' : '학번',
            'major' : '학과',
            'phone_number' : '전화번호'
        }
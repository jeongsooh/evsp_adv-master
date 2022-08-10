from django import forms
from django.contrib.auth.hashers import check_password
from .models import Evuser

class RegisterForm(forms.Form):
  userid = forms.CharField(
    error_messages={
      'required': '사용자 아이디를 입력하세요.'
    },
    max_length=64, label='사용자 아이디'
  )
  password = forms.CharField(
    error_messages={
      'required': '비밀번호를 입력하세요.'
    },
    widget=forms.PasswordInput, label='비밀번호'
  )
  re_password = forms.CharField(
    error_messages={
      'required': '비밀번호를 다시 입력하세요.'
    },
    widget=forms.PasswordInput, label='비밀번호 확인'
  )

  def clean(self):
    cleaned_data = super().clean()
    userid = cleaned_data.get('userid')
    password = cleaned_data.get('password')
    re_password = cleaned_data.get('re_password')

    if password and re_password:
      if password != re_password:
        self.add_error('password', '비밀번호가 서로 다릅니다.')
        self.add_error('re_password', '비밀번호가 서로 다릅니다.')

class LoginForm(forms.Form):
  userid = forms.CharField(
    error_messages={
      'required': '사용자 아이디를 입력하세요.'
    },
    max_length=64, label='사용자 아이디'
  )
  password = forms.CharField(
    error_messages={
      'required': '비밀번호를 입력하세요.'
    },
    widget=forms.PasswordInput, label='비밀번호'
  )

  def clean(self):
    cleaned_data = super().clean()
    userid = cleaned_data.get('userid')
    password = cleaned_data.get('password')

    if userid and password:
      try:
        evuser = Evuser.objects.get(userid=userid)
      except Evuser.DoesNotExist:
        self.add_error('userid', '아이디가 없습니다.')
        return

      if password != evuser.password:
        self.add_error('password', '비밀번호가 틀렸습니다.')
      else:
        self.user_id = evuser.id

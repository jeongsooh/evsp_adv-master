from django import forms
from django.contrib.auth.hashers import check_password
from .models import Ocpp16

class MessageForm(forms.Form):
  cpnumber = forms.CharField(
    error_messages={
      'required': '충전기번호를 입력하세요.'
    },
    max_length=64, label='충전기번호'
  )
  msg_name = forms.CharField(
    error_messages={
      'required': '메세지이름을 입력하세요.'
    },
    max_length=64, label='메세지이름'
  )
  msg_content = forms.CharField(
    error_messages={
      'required': '메세지내용을 다시 입력하세요.'
    },
    max_length=256, label='메세지내용'
  )

  def clean(self):
    cleaned_data = super().clean()
    cpnumber = cleaned_data.get('cpnumber')
    msg_name = cleaned_data.get('msg_name')
    msg_content = cleaned_data.get('msg_content')


# class LoginForm(forms.Form):
#   userid = forms.CharField(
#     error_messages={
#       'required': '사용자 아이디를 입력하세요.'
#     },
#     max_length=64, label='사용자 아이디'
#   )
#   password = forms.CharField(
#     error_messages={
#       'required': '비밀번호를 입력하세요.'
#     },
#     widget=forms.PasswordInput, label='비밀번호'
#   )

#   def clean(self):
#     cleaned_data = super().clean()
#     userid = cleaned_data.get('userid')
#     password = cleaned_data.get('password')

#     if userid and password:
#       try:
#         evuser = Evuser.objects.get(userid=userid)
#       except Evuser.DoesNotExist:
#         self.add_error('userid', '아이디가 없습니다.')
#         return

#       if password != evuser.password:
#         self.add_error('password', '비밀번호가 틀렸습니다.')
#       else:
#         self.user_id = evuser.id

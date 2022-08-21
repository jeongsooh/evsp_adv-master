from django import forms
from evuser.models import Evuser
from evcharger.models import Evcharger

class CardinfoCreateRemoteForm(forms.Form):
  cardname = forms.CharField(
    error_messages={
      'required': '카드이름을 입력하세요.'
    },
    max_length=64, label='카드이름'
  )
  userid = forms.CharField(
    error_messages={
      'required': '회원아이디를 입력하세요.'
    },
    max_length=64, label='회원아이디'
  )
  cpnumber = forms.CharField(
    error_messages={
      'required': '충전기번호를 입력하세요.'
    },
    max_length=64, label='충전기번호'
  )

  def clean(self):
    cleaned_data = super().clean()
    userid = cleaned_data.get('userid')
    cpnumber = cleaned_data.get('cpnumber')
    cardname = cleaned_data.get('cardname')

    if userid and cpnumber:
      try:
        evuser = Evuser.objects.get(userid=userid)
        evcharger = Evcharger.objects.get(cpnumber=cpnumber)
      except Evuser.DoesNotExist:
        self.add_error('userid', '아이디가 없습니다.')
        return
      except Evcharger.DoesNotExist:
        self.add_error('cpnumber', '충전기번호가 없는 번호입니다.')
        return

      self.userid = evuser.id
      self.cpnumber = evcharger.id
      self.cardname = cardname


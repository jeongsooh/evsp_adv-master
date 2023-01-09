from django import forms

class CharginginfoFilterForm(forms.Form):
  cpnumber = forms.CharField()
  userid = forms.CharField()
  start_dttm = forms.DateTimeField(label="충전시작일")
  end_dttm = forms.DateTimeField(label="충전종료일")
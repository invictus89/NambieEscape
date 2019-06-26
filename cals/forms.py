from django import forms
from django.forms import DateInput
from .models import Event

title_choices = [
    ('기념일', '기념일'),
    ('뉴스', '뉴스'),
    ('사건사고', '사건사고'),
    ('역사', '역사'),
]


class EventForm(forms.ModelForm):
  title = forms.CharField(
      label='제목',
      widget=forms.TextInput(attrs={
          'placeholder': 'Enter the title',
      })
  )
  description = forms.CharField(
      label='내용',
      widget=forms.Textarea(attrs={
          'placeholder': 'Enter the description',
          'rows': 5,
          'cols': 50,
      })
  )
  title_type = forms.ChoiceField(
      label='종류',
      choices=title_choices,
  )

  class Meta:
    model = Event
    # fields = '__all__'
    fields = ('title', 'description','title_type',)

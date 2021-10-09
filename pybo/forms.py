from django import forms
from django.forms import widgets
from pybo.models import Question, Answer

class QuestionForm(forms.ModelForm):
    # 장고의 모델폼은 내부 클래스로 Meta클래스를 반드시 가져야 한다.
    # Meta 클래스에는 모델 폼이 사용할 모델명과 필드명을 적어야한다. 
    class Meta:
        model = Question
        fields = ['subject', 'content']
        # {{form.as_p}}를 사용하면 빠르게 템플릿을 만들 수 있지만 HTML 코드가 자동으로 생성되므로 디자인측면에서 제한이 생긴다. 
        # 또한 디자인영역과 서버프로그래밍 영역이 혼재되어 개발 역할을 분리하기도 애매해진다.
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class':'form-control'}),
        #     'content': forms.Textarea(attrs={'class':'form-control', 'rows':10}),
        # }
        labels = {
            'subject': '제목',
            'content': '내용',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }
from  django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ваше имя')
    email = forms.EmailField(label='e-mail')
    phone_number = forms.IntegerField(label='Телефон для связи')
    message = forms.CharField(widget=forms.Textarea(
            attrs={
                'placeholder': 'Услуги, пожелания, время',
                'class': 'form-control',
            }
        ), label='Комментарий')

    def save(self):
        pass


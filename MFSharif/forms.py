__author__ = 'Mpourreza'
from django import forms

class DocumentForm(forms.Form):
    docfile = forms.ImageField(
        label='Select an image',
        help_text='max. 42 megabytes'
    )

class RegisterUser(forms.Form):
    username = forms.CharField(max_length= 20, error_messages={'required': 'لطفاً نام کاربری مورد نظر را وارد نمایید'})
    first_name = forms.CharField(max_length= 20, error_messages={'required': 'طفاً نام خود را وارد نمایید'})
    last_name = forms.CharField(max_length= 30, error_messages={'required': 'لطفاً نام خانوادگی خود را وارد نمایید'})
    email = forms.EmailField(error_messages={'required':'لطفاً‌ایمیل خود را وارد نمایید' ,'invalid': 'ایمیل وارد شده معتبر نیست'})
    password = forms.CharField(max_length= 30, widget= forms.PasswordInput, error_messages={'required': 'وارد کردن کلمه‌ی عبور الزامی است'})

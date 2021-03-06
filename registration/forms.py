"""
Forms and validation code for user registration.

Note that all of these forms assume Django's bundle default ``User``
model; since it's not possible for a form to anticipate in advance the
needs of custom user models, you will need to write your own forms if
you're using a custom model.

"""

from MFSharif.models import *
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _


class RegistrationForm(forms.Form):
    """
    Form for registering a new user account.
    
    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.
    
    Subclasses should feel free to add any additional validation they
    need, but should avoid defining a ``save()`` method -- the actual
    saving of collected user data is delegated to the active
    registration backend.

    """
    required_css_class = 'required'
    
    username = forms.RegexField(regex=r'^[\w.@+-]+$',
                                max_length=30,
                                label=_("نام کاربری"),
                                error_messages={'invalid': _(" نام کاربری وارد شده معتبر نمی‌باشد")})
    first_name =forms.CharField(label=_("نام"), error_messages={'required': _('وارد کردن نام الزامی است')})
    last_name = forms.CharField(label=_("نام خانوادگی"), error_messages= {'required':'وارد کردن نام خانوادگی الزامی است'})
    email = forms.EmailField(label=_("ایمیل"), error_messages={'required': _('وارد کردن ایمیل الزامی است'), 'invalid':_('ایمیل وارد شده معتبر نیس')})
    password1 = forms.CharField(widget=forms.PasswordInput,
                                label=_("کلمه‌عبور"),error_messages={'required': _('لطفاً‌کلمه‌ی عبور مدنظر خود را وارد کنید')})
    password2 = forms.CharField(widget=forms.PasswordInput,
                                label=_(" تکرار کلمه‌ی عبور"), error_messages= {'required':_('این فیلد نباید خالی باشد')})

    postal_code = forms.IntegerField(label=_('کد پستی'), error_messages={'required':'لطفاً کد پستی خود را وارد کنید', 'min_value': 'کد پستی باید از ۱۱۱۱۱۱۱ بزرگتر و از ۹۹۹۹۹۹۹ کوچکتر باشد', 'max_value': 'کد پستی باید از ۱۱۱۱۱۱۱ بزرگتر و از ۹۹۹۹۹۹۹ کوچکتر باشد'})
    phone= forms.IntegerField(label=_('شماره تلفن') ,error_messages= {'required': 'وارد کردن شماره تلفن الزامی است'})
    city = forms.ChoiceField(label= _('شهر') ,choices=([('1', 'تهران'),('2','شیراز'),('3', 'مشهد'),('4', 'اصفهان')]),error_messages={'required': _('لطفاً شهر خود را انتخاب کنید')})
    address = forms.CharField(label= _('آدرس') ,max_length=150, widget=forms.Textarea, error_messages={'required':'وارد کردن آدرس الزامی است'})
    
    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        
        """
        existing = User.objects.filter(username__iexact=self.cleaned_data['username'])
        if existing.exists():
            raise forms.ValidationError(_("A user with that username already exists."))
        else:
            return self.cleaned_data['username']

    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.
        
        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields didn't match."))
        return self.cleaned_data


class RegistrationFormTermsOfService(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which adds a required checkbox
    for agreeing to a site's Terms of Service.
    
    """
    tos = forms.BooleanField(widget=forms.CheckboxInput,
                             label=_('I have read and agree to the Terms of Service'),
                             error_messages={'required': _("You must agree to the terms to register")})


class RegistrationFormUniqueEmail(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which enforces uniqueness of
    email addresses.
    
    """
    def clean_email(self):
        """
        Validate that the supplied email address is unique for the
        site.
        
        """
        if User.objects.filter(email__iexact=self.cleaned_data['email']):
            raise forms.ValidationError(_("This email address is already in use. Please supply a different email address."))
        return self.cleaned_data['email']


class RegistrationFormNoFreeEmail(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which disallows registration with
    email addresses from popular free webmail services; moderately
    useful for preventing automated spam registrations.
    
    To change the list of banned domains, subclass this form and
    override the attribute ``bad_domains``.
    
    """
    bad_domains = ['aim.com', 'aol.com', 'email.com', 'gmail.com',
                   'googlemail.com', 'hotmail.com', 'hushmail.com',
                   'msn.com', 'mail.ru', 'mailinator.com', 'live.com',
                   'yahoo.com']
    
    def clean_email(self):
        """
        Check the supplied email address against a list of known free
        webmail domains.
        
        """
        email_domain = self.cleaned_data['email'].split('@')[1]
        if email_domain in self.bad_domains:
            raise forms.ValidationError(_("Registration using free email addresses is prohibited. Please supply a different email address."))
        return self.cleaned_data['email']

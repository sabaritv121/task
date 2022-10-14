import mark as mark
from django.contrib.auth.forms import UserCreationForm


from django import forms
from django.forms import DateInput

from zf_app.models import Login, adm, student, marks


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2',)



class DateInput(forms.DateInput):
    input_type = 'date'

class AdminRegister(forms.ModelForm):
    dob = forms.DateField(widget=DateInput)
    class Meta:
        model = adm
        # fields = "__all__"
        fields = ('name','dob','contact_no','profile_pic')

        exclude = ("user",)


class StudentRegister(forms.ModelForm):
    dob = forms.DateField(widget=DateInput)
    class Meta:
        model = student
        # fields = "__all__"
        fields = ('name','dob','contact_no','profile_pic')
        exclude = ("user",)




class AddMarks(forms.ModelForm):
    class Meta:
        model = marks
        fields = ('user','mark')



class UserProfileUpdate(forms.ModelForm):


    class Meta:
        model = student
        fields = ('name','dob','contact_no','profile_pic')

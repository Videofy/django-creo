from django import forms
from django.contrib.auth.models import User
from Artist.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget =forms.PasswordInput(attrs = {"class":"form-control is-valid", "placeholder":"Password","label for":"exampleInputPassword1","size":"25"}))
    password1 = forms.CharField(widget =forms.PasswordInput(attrs = {"class":"form-control is-valid", "placeholder":"Password","label for":"exampleInputPassword1","size":"25"}),label="Password Confirmation")
    username = forms.CharField(widget = forms.TextInput(attrs = {"class":"form-control is-valid", "id":"exampleInputUserName1","placeholder":"Enter Username"}))
    email    = forms.EmailField(widget = forms.EmailInput(attrs = {"class":"form-control is-valid" ,"id":"exampleInputEmail1","placeholder":"Enter email"}))
    class Meta():
        model  = User
        fields = ('first_name','last_name','username','email','password')
    def clean_username(self, *args ,**kwargs):
        username = self.cleaned_data.get('username')
        username_qs = User.objects.filter(username=username)
        if username_qs.exists():
            raise forms.ValidationError("UserName Exists")
        return username
    def clean_password1(self):
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
        if password and password1 and password != password1:
            raise forms.ValidationError('Password do not match')
        return password1

class UserProfileInfoForm(forms.ModelForm):
    GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female'),
   ('O','Other')
   )   
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    class Meta():
        model  = UserProfileInfo
        fields = ('gender',)
    
class UserProfileInfoUpdateForm(forms.ModelForm):
    GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female'),
   ('O','Other')
   )
   # profile_pic= forms.ImageField(widget=PictureWidget)
   # portfolio_site = forms.URLField(widget = forms.URLInput(attrs = {"class":"form-control is-valid","placeholder":"Enter Portfolio Site"}))
    bio = forms.CharField(widget = forms.Textarea(attrs = {'rows':6,
                                    'cols'       :22,
                                    'style'      :'resize:none;',
                                    "class"      :"form-control is-valid",
                                    "id"         :"exampleInputUserName1",
                                    "placeholder":"Enter Bio"})) 
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    class Meta():
        model  = UserProfileInfo
        fields = ('portfolio_site','profile_pic','gender','bio','resume')
    


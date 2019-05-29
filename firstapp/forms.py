from django import forms
from firstapp.models import UserRole,UserInfo

class UserRoleForm(forms.ModelForm):
    class Meta():
        model=UserRole
        fields='__all__'
        #exclude=["role_id,role_name"]
        #to show it is custom use exclude, else use include
class UserInfoForm(forms.ModelForm):
    class Meta():
        model=UserInfo
        exclude=["id","name"]

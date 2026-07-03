from django import forms
from django.contrib.auth import get_user_model

# Changing the model or the underlying database schema later in the development
# cycle will not cause any breaking changes or system failures
User = get_user_model()

# -----------
# User Model
# -----------
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

# ---------------
# Password Model
# ---------------
class PasswordUpdateForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(), label='Old password')
    new_password = forms.CharField(widget=forms.PasswordInput(), label='New password')
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Confirm new password')

    def clean(self):
        # Information collection
        cleaned_data = super().clean()

        new_pw = cleaned_data.get('new_password')
        confirm_pw = cleaned_data.get("confirm_password")

        if new_pw and confirm_pw and new_pw != confirm_pw:
            # Show in the template
            raise forms.ValidationError("The new password and its repetition do not match")
        
        return cleaned_data
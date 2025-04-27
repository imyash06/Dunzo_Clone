# from django import forms
# from .models import CustomUser

# class CustomUserCreationForm(forms.ModelForm):
#     """
#     Form for registering a new user.
#     """
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
#     )

#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'std', 'div', 'date_of_birth', 'password']
#         widgets = {
#             'date_of_birth': forms.DateInput(attrs={'type': 'date'}),  # Calendar date picker
#         }

#     def save(self, commit=True):
#         """
#         Overriding the save method to hash the password before saving the user.
#         """
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         if commit:
#             user.save()
#         return user


# class CustomLoginForm(forms.Form):
#     """
#     Form for logging in an existing user.
#     """
#     username = forms.CharField(
#         max_length=150,
#         widget=forms.TextInput(attrs={
#             'placeholder': 'Username',
#             'class': 'form-control'
#         })
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={
#             'placeholder': 'Password',
#             'class': 'form-control'
#         })
#     )

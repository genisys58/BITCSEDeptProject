from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, SCIJournals, UnpaidScopus, PaidScopus, OtherJournals
import datetime

YEAR_CHOICES = []
for r in range(1970, (datetime.datetime.now().year + 1)):
    YEAR_CHOICES.append((r, r))


class UserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class RegForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    dept = forms.CharField(label='Department',
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}))
    desgn = forms.CharField(label='Designation',
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Designation'}))
    phone = forms.CharField(max_length=10,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))

    class Meta:
        model = Profile
        fields = (
            'name',
            'dept',
            'desgn',
            'phone',
        )

    def save(self, commit=True):
        profile = super(RegForm, self).save(commit=False)
        profile.name = self.cleaned_data["name"]
        profile.dept = self.cleaned_data["dept"]
        profile.desgn = self.cleaned_data["desgn"]
        profile.phone = self.cleaned_data["phone"]
        if commit:
            profile.save()
        return profile


class PapersForm(forms.ModelForm):
    authors = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 4, 'class': 'form-control', 'placeholder': 'Enter name of authors separated by comma'}))
    corresAuthors = forms.CharField(label='Corresponding Authors', widget=forms.Textarea(
        attrs={'rows': 4, 'class': 'form-control', 'placeholder': 'Enter name of authors separated by comma'}))
    paperTitle = forms.CharField(label='Paper Title',
                                 widget=forms.Textarea(
                                     attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Paper Title'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    impactFac = forms.CharField(label='Impact Factor',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Impact Factor'}))
    volume = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Volume'}))
    pp = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PP'}))
    year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))


class SCIForm(PapersForm):
    class Meta:
        model = SCIJournals
        fields = (
            'authors',
            'corresAuthors',
            'paperTitle',
            'name',
            'impactFac',
            'volume',
            'pp',
            'year',
        )


class UnpaidScopusForm(PapersForm):
    class Meta:
        model = UnpaidScopus
        fields = (
            'authors',
            'corresAuthors',
            'paperTitle',
            'name',
            'impactFac',
            'volume',
            'pp',
            'year',
        )


class PaidScopusForm(PapersForm):
    class Meta:
        model = PaidScopus
        fields = (
            'authors',
            'corresAuthors',
            'paperTitle',
            'name',
            'impactFac',
            'volume',
            'pp',
            'year',
        )


class OthersJournalsForm(PapersForm):
    class Meta:
        model = OtherJournals
        fields = (
            'authors',
            'corresAuthors',
            'paperTitle',
            'name',
            'impactFac',
            'volume',
            'pp',
            'year',
        )

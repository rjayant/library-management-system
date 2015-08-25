from django import forms
from .models import *
from django.forms.formsets import BaseFormSet

class contactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
class LinkForm(forms.ModelForm):
    class Meta:
        model = UserLink
    def __init__(self, *args, **kwargs):
        super(LinkForm, self).__init__(*args, **kwargs)
        self.fields['anchor'] = forms.CharField(max_length=100,
                             widget=forms.TextInput(
                                                    attrs={'placeholder':'Link name/Anchor Text'}
                                                    ),
                                                    required=False
                             )
        self.fields['url'] = forms.URLField(
                         widget=forms.URLInput(
                                               attr={'placeholder':'URl Link'}
                                               ),
                                               required = False
                         )
class UserProfile(forms.Form):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(UserProfile, self).__init__(*args, **kwargs)
        self.fields['first_name'] = forms.CharField(max_length=50,
                                                    initial=self.user.first_name,
                                                    widget=forms.TextInput(attrs={
                                                    'placeholder':'First Name',                        
                                                                                  }
                                                                           )
                                                    )
        self.fields['last_name'] = forms.CharField(max_length=50,
                                                   initial=self.user.last_name,
                                                   widget=forms.TextInput(attrs={'placeholder':'Last Name'})
                                                   
                                                   )

        
class BaseLinkFormSet(BaseFormSet):
    def clean(self):
        if any(self.errors()):
            return
        anchors = []
        urls = []
        duplicate = False
        super(BaseLinkFormSet, self).clean()
        for form in self.forms():
            anchor = form.cleaned_data['anchor']
            url  = form.cleaned_data['url']
            if url in urls:
                duplicate = True
            urls.append(url)
            if anchor in anchors:
                duplicate = True
            anchors.append(anchor)
            if duplicate:
                forms.ValidationError('Links must have unique url and anchor', code='duplicate_links')
            if url and not anchor:
                forms.ValidationError('Please give any anchor')
            if anchor and not url:
                forms.ValidationError('Please give any URl')


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        #fields = ['first_name', 'last_name', 'email', 'address', 'city', 'gender', 'age','state']
        readonly_fields=('aadhar_no')

        
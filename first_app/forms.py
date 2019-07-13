from django import forms
from django.core import validators
# you get a method from django forms which you use as the argument in the class.


print(forms)

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="enter your email again")
    text = forms.CharField(widget=forms.Textarea)
    # you can specify a widget for the form.
    # botcatcher does exactly what it sounds. It creates a hidden input field which catches bots. Bots search the HTML of a page, where they try to automatically fill in values. It will fill in this hidden field with a value, which hits the clean_botcatcher and reponds with the error
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(2)])

    # DJANGO HAS BUILT IN VALIDATORS!!!
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError('Gotcha Bot')
        return botcatcher

    def check_emails(self):
        # .clean is used to make sure that the data matches your own parameters. super().clean() takes all attributes and cleans all of them, then you can grab specific fields(email and verify email).
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        print(all_clean_data['text'])
        if email != vmail:
            raise form.ValidationError("Not the same")

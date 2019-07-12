from django import forms
# you get a method from django forms which you use as the argument in the class.

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

# you can specify a widget for the form.

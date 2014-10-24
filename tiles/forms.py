from django import forms

class ProfileImageForm(forms.Form):
	title = forms.CharField(
      widget = forms.Textarea(attrs = {'cols': 40, 'rows': 1}), required=False, label="Tile:")
	text = forms.CharField(
      widget = forms.Textarea(attrs = {'cols': 40, 'rows': 10}), required=False, label="Description:")
	image = forms.FileField(label='Upload a cool picture.')
    
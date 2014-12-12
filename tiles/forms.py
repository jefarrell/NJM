from django import forms

class ProfileImageForm(forms.Form):
	#myfield = forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))
	title = forms.CharField(
      widget = forms.TextInput(attrs = {'cols': 40, 'rows': 1, 'class' : 'titleclass'}), required=False, label="Tile:")
	text = forms.CharField(
      widget = forms.Textarea(attrs = {'cols': 40, 'rows': 10, 'class' : 'textclass'}), required=False, label="Description:")
	image = forms.FileField(label='Upload a cool picture.')
	weblink = forms.CharField(
      widget = forms.TextInput(attrs = {'cols': 40, 'rows': 1, 'class' : 'weblinkclass'}), required=False, label="Weblink:")
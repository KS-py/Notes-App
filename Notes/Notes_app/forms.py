from django import forms

class CreateNote(forms.Form):
	name = forms.CharField(label="Note Title", max_length=200)
	text = forms.CharField(max_length=255)
from django import forms

class FO_addnews(forms.Form):
    title = forms.CharField(
        label="Titulo",
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={'class':'input'})
    )
    description = forms.CharField(
        label="Contenido",
        widget=forms.Textarea(attrs={'class':'input'})
    )
    image = forms.ImageField()
from django import forms


class ColorPredictionForm(forms.Form):
    red = forms.IntegerField(min_value=0, max_value=255)
    green = forms.IntegerField(min_value=0, max_value=255)
    blue = forms.IntegerField(min_value=0, max_value=255)

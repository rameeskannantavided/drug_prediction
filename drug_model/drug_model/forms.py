from django import forms

class YourForm(forms.Form):
    age = forms.IntegerField()
    sex = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])
    bp = forms.ChoiceField(choices=[('LOW', 'Low'), ('NORMAL', 'Normal'), ('HIGH', 'High')])
    cholesterol = forms.ChoiceField(choices=[('NORMAL', 'Normal'), ('HIGH', 'High')])
    na_to_k = forms.DecimalField(max_digits=5, decimal_places=4)

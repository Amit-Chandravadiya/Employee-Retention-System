from django import forms

class Mlforms(forms.Form):
    salary=forms.CharField(max_length=6,min_length=3)
    promotion=forms.IntegerField(min_value=0)
    exp=forms.IntegerField(min_value=0)
    hrs=forms.IntegerField(min_value=1)
    projects=forms.IntegerField(min_value=1)
    perc1=forms.FloatField()
    perc2=forms.FloatField()
    workacc=forms.IntegerField(min_value=0)
    
class Contactforms(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    txtarea=forms.Textarea()
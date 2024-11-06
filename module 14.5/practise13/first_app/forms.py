from django import forms
# from django.forms.widgets import NumberInput
import datetime

class PractiseForm(forms.Form):
    name = forms.CharField(min_length=5,max_length=10, initial='Your name...',)
    email = forms.EmailField()
    comment =forms.CharField(widget =forms.Textarea(attrs={'rows':3}))
    # date = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    year_choices= ['1999','2001','2004']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=year_choices))
    day = forms.DateField(initial=datetime.date.today)
    agree = forms.BooleanField(label="I accept the terms & condition", initial=True)
    total_money = forms.DecimalField(initial=False)
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ]
    fav_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    FAVORITE_COLORS_CHOICES1 = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ]
    favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES1)
    
    roll_number = forms.IntegerField(max_value =100020, 
    help_text = "Enter 6 digit roll number") 
    geeks_field = forms.ImageField()
    file = forms.FileField()
    d_field = forms.DurationField( )

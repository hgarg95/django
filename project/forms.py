from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import RadioFieldRenderer
from django.core.validators import RegexValidator




class ContactForm(forms.Form):
  Name = forms.CharField()
  Email = forms.EmailField()
  Contact = forms.IntegerField()
  Post_Your_Query = forms.CharField(max_length=400, widget=forms.Textarea( attrs={'rows':'4', 'cols': '10'}))

  def clean_Contact(self):
    contact=self.cleaned_data.get("Contact")
    c = str(contact)

    if len(c) != 10:
      raise forms.ValidationError("Please Enter a Valid 10 digit Mobile Number")
    return contact    



class CareersForm(forms.Form):
  Name = forms.CharField(max_length=100)
  Email = forms.EmailField()
  Contact = forms.IntegerField()
  Address = forms.CharField()

  s="Choose Any One"
  Company  = 'Company'
  Educational_Institute = 'Educational Institute'
  Investor = 'Investor'
  Merger = 'Merger'
  Media_Partner = 'Media Partner'
  Others= 'Others'
  S_TYPE_CHOICES = (
    (s, "Choose Any One"),
    (Company, 'Company'),
    (Educational_Institute, 'Educational Institute'),
    (Investor, 'Investor'),
    (Merger, 'Merger'),
    (Media_Partner, 'Media Partner'),
    (Others, 'Others'),
    )
  Reach_Us_As_A = forms.ChoiceField(choices=S_TYPE_CHOICES)



  Post_Your_Query = forms.CharField(max_length=4000, widget=forms.Textarea( attrs={'rows':'4', 'cols': '10'}))

  def clean_Contact(self):
    contact=self.cleaned_data.get("Contact")
    c = str(contact)

    if len(c) != 10:
      raise forms.ValidationError("Please Enter a Valid 10 digit Mobile Number")
    return contact

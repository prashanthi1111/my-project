from django import forms
from .models import products
class ProductForm(forms.ModelForm):
	title=forms.CharField(label=' ',widget=forms.TextInput(attrs={"placeholder":"your text"}))
	email=forms.EmailField()
	description=forms.CharField(
		required=False,
		widget=forms.Textarea(
			attrs={
			"placeholder":"your description",
			"class":"new-class-name-two",
			"id":"my-id-for-text-area",
			"rows":20,
			"cols":120
			}
		)
	)
	class Meta:
		model=products
		fields=[
		'title',
		'description',
		'price'
 		]
def clean_title(self,*args,**Kwargs):
    title=self.cleaned_data.get("title")
    if not "CFE" in title:
        raise forms.ValidationError("this is not a valid title")
    if not "ME" in title:
        raise forms.ValidationError("this is not a valid title")
    return title

def clean_email(self,*args,**Kwargs):
    email=self.cleaned_data.get("email")
    if not email.endswith("edu"):      
        raise forms.ValidationError("this is not a valid title")
    return email	
class RawProductForm(forms.Form):
    title=forms.CharField(label=' ',widget=forms.TextInput(attrs={"placeholder":"your text"}))
    description=forms.CharField(
    	required=False,
    	widget=forms.Textarea(
    		attrs={
    		"placeholder":"your description",
    		"class":"new-class-name-two",
    		"id":"my-id-for-text-area",
    		"rows":20,
            "cols":120
            }
    	)
    	
    )
    		
    price=forms.DecimalField(initial=100.99)
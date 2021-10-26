from django import forms
from .models import Item, Job, Receipt


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields ="__all__"

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields ="__all__"

class SalesForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields ="__all__"



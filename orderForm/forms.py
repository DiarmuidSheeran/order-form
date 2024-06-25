from django import forms
from tayto.models import taytoProduct
from .models import taytoOrder

class taytoOrderForm(forms.ModelForm):
    products = forms.ModelMultipleChoiceField(
        queryset=taytoProduct.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False  # Set to False if products are added after form submission
    )

    class Meta:
        model = taytoOrder
        fields = ['products']  # Only include the products field in the form

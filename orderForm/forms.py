from django import forms
from tayto.models import taytoProduct
from .models import taytoOrder

class ProductQuantityForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=0, required=True)

    class Meta:
        model = taytoProduct
        fields = ['id', 'name', 'quantity']
        widgets = {
            'name': forms.HiddenInput(),
            'id': forms.HiddenInput(),  # Ensure id is treated as a hidden field
        }

ProductQuantityFormSet = forms.modelformset_factory(
    taytoProduct,
    form=ProductQuantityForm,
    extra=0,
    can_delete=False
)

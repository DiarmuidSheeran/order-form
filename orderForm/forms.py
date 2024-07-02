from django import forms
from tayto.models import taytoProduct
from walkers.models import walkersProduct
from .models import taytoOrder, walkersOrder

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

class WalkersProductQuantityForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=0, required=True)

    class Meta:
        model = walkersProduct
        fields = ['id', 'name', 'quantity']
        widgets = {
            'name': forms.HiddenInput(),
            'id': forms.HiddenInput(),  # Ensure id is treated as a hidden field
        }

ProductQuantityFormSet = forms.modelformset_factory(
    walkersProduct,
    form=ProductQuantityForm,
    extra=0,
    can_delete=False
)

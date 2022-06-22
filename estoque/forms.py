from django import forms
from estoque.models import Venda


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['produto', 'cliente', 'vendedor', 'data']

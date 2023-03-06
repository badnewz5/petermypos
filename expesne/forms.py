from django import forms
from . models import*
from branches.models import Branch
from products.models import Product



class CreateExpenseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'form-control'})
        
       

    class Meta:
        model = Expense
        fields = ['name', 'quantity', 'amount', 'description']

class ExpenseFiltersForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['date_from'].widget.attrs.update({'class': 'form-control'})
        self.fields['date_from'].widget.attrs.update({'placeholder': 'Date from'})
        self.fields['date_to'].widget.attrs.update({'class': 'form-control'})
        self.fields['date_to'].widget.attrs.update({'placeholder': 'Date to'})
        self.fields['branch'].widget.attrs.update({'class': 'form-control'})
        self.fields['date_from'].widget.attrs.update({'id': 'date_from'})
        self.fields['date_to'].widget.attrs.update({'id': 'date_to'})

    date_from = forms.DateField()
    date_to = forms.DateField()
    branch = forms.ModelChoiceField(
        queryset=Branch.objects.all(),
        # required=False
    )

class ProfitLoassFiltersForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['date_from'].widget.attrs.update({'class': 'form-control'})
        self.fields['date_from'].widget.attrs.update({'placeholder': 'Date from'})
        self.fields['date_to'].widget.attrs.update({'class': 'form-control'})
        self.fields['date_to'].widget.attrs.update({'placeholder': 'Date to'})
        self.fields['branch'].widget.attrs.update({'class': 'form-control'})
        self.fields['date_from'].widget.attrs.update({'id': 'date_from'})
        self.fields['date_to'].widget.attrs.update({'id': 'date_to'})

    date_from = forms.DateField()
    date_to = forms.DateField()
    branch = forms.ModelChoiceField(
        queryset=Branch.objects.all(),
        # required=False
    )

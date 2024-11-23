# strategies/forms.py

from django import forms
from .models import Strategy
import backtrader as bt

STRATEGY_TEMPLATE = '''
import backtrader as bt

class CustomStrategy(bt.Strategy):
    params = (
        ('param_name', default_value),
    )

    def __init__(self):
        # Initialize indicators
        pass

    def next(self):
        # Define your trading logic
        pass
'''

class StrategyForm(forms.ModelForm):
    class Meta:
        model = Strategy
        fields = ['name', 'description', 'code']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'mt-1 block w-full bg-gray-50 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500'
            }),
            'description': forms.Textarea(attrs={
                'class': 'mt-1 block w-full bg-gray-50 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500',
                'rows': 3
            }),
            'code': forms.Textarea(attrs={
                'class': 'mt-1 block w-full bg-gray-50 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 font-mono p-3',
                'rows': 10,
                'placeholder': '{"key": "value"}'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(StrategyForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:
            # Autofill with template if creating a new Strategy
            self.fields['code'].initial = STRATEGY_TEMPLATE

    def clean_code(self):
        code = self.cleaned_data.get('code')
        exec_globals = {}
        try:
            exec(code, exec_globals)
        except Exception as e:
            raise forms.ValidationError(f"Error executing code: {e}")

        # Check for Strategy class
        strategy_class = None
        for obj in exec_globals.values():
            if isinstance(obj, type) and issubclass(obj, bt.Strategy):
                strategy_class = obj
                break

        if not strategy_class:
            raise forms.ValidationError("The code must define a class that inherits from backtrader.Strategy.")

        return code
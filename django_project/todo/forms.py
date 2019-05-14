from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('description', 'due_date', 'done_percentage')
        widgets = {
            'due_date': DatePickerInput(format='%Y-%m-%d'), # specify date-frmat
        }
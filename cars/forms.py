from django import forms
from django.core.exceptions import ValidationError

from .models import Car, Person


class AddNewCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('owner', 'vin', 'model', 'brand', 'type', 'year', 'description')

    PESEL = forms.CharField(max_length=11)
    name = forms.CharField(max_length=25)
    surname = forms.CharField(max_length=25)
    date_of_birth = forms.DateTimeField()

    def is_valid(self):
        person_data = {k: self.fields[k] for k in ('PESEL', 'name', 'surname', 'date_of_birth') if k in self.fields}
        if len(person_data) < 4:
            raise ValidationError("This field is required")

        person = Person(**person_data)
        self.fields['owner'] = forms.ChoiceField((person,))

        return super(AddNewCarForm, self).is_valid()

    def save(self, commit=True):
        self.fields['owner'].save()
        return super(AddNewCarForm, self).save()

from bootstrap_modal_forms.forms import BSModalForm
from django import forms
from django.forms import modelformset_factory

from wyniki.models import Class, Student, Result


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = {"name", "year"}


StudentFormSet = modelformset_factory(
    Student, extra=3, fields=("first_name", "last_name")
)


class ResultForm(BSModalForm):
    class Meta:
        model = Result
        fields = {"value"}
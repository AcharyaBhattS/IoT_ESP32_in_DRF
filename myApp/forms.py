from django import forms
from .models import Upld_sbdb

class upld_form(forms.ModelForm):
    class Meta:
        model = Upld_sbdb
        fields = "__all__"

from typing import Any
from django import forms
from goplaces.models import Link


class LinkModelForm(forms.ModelForm):
    class Meta:
        model = Link
        exclude = ("owner",)

    def save(self, commit: bool = ...) -> Any:
        if not self.instance.pk:
            self.instance.owner = self.request.user

        return super().save(commit)

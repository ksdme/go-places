from django.contrib import auth
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


def validate_keyword(value):
    if " " in value:
        raise ValidationError("Keyword cannot contain spaces.")

    if not value.islower():
        raise ValidationError("Keyword needs to be lower case.")


class Link(models.Model):
    owner = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE, related_name="links")

    # TODO: Make sure the keyword is unique within the user queryset.
    keyword = models.CharField(max_length=32, validators=[MinLengthValidator(1), validate_keyword])
    url = models.URLField(verbose_name="Link")
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"go/{self.keyword}"

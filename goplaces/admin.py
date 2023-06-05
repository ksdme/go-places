from typing import Any, Optional
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from unfold.admin import ModelAdmin
from goplaces.forms import LinkModelForm
from goplaces.models import Link


@admin.register(Link)
class LinkModelAdmin(ModelAdmin):
    list_display = ("id", "keyword", "url", "active")
    form = LinkModelForm

    def get_form(self, request: Any, *args: Any, **kwargs: Any) -> Any:
        form = super().get_form(request, *args, **kwargs)
        form.request = request
        return form

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).filter(owner=request.user)

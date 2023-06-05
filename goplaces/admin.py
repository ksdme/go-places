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


import django.contrib.auth.models as auth_models
import django.contrib.auth.admin as auth_admin

admin.site.unregister(auth_models.User)
@admin.register(auth_models.User)
class UserAdmin(auth_admin.UserAdmin, ModelAdmin): pass

admin.site.unregister(auth_models.Group)
@admin.register(auth_models.Group)
class GroupAdmin(auth_admin.GroupAdmin, ModelAdmin): pass

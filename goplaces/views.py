from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from goplaces.models import Link


def idle(_):
    return redirect("admin:index")


@login_required(login_url="admin:login")
def handle_link(request, keyword):
    keyword = keyword.lower()

    link = Link.objects.filter(owner=request.user, keyword=keyword).first()
    if link is None:
        return redirect("admin:goplaces_link_changelist")

    if not link.active:
        return redirect("admin:goplaces_link_change", link.pk)

    return redirect(link.url)

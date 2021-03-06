from django.shortcuts import render, redirect, reverse
from rooms import models as room_models
from django.views.generic import TemplateView
from . import models

def toggle_room(request, room_pk):
    action = request.GET.get('action', None)
    room = room_models.Room.objects.get_or_none(pk=room_pk)
    if room is not None and action is not None:
        the_list, _ = models.List.objects.get_or_create(
            user=request.user, name="My Favourites Houses"
        )
        if action == "add":
            the_list.rooms.add(room)
        elif action == "remove":
            the_list.rooms.remove(room)
    return redirect(reverse("rooms:detail", kwargs={"pk": room_pk}))


# user의 list만 가져오면 되기때문에 Template만 랜더링하면됨 따라서 classBased로 구현
class SeeFavsView(TemplateView):

    template_name = "lists/list_detail.html"
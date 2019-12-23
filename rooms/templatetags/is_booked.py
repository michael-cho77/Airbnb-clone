import datetime
from django import template
from reservations import models as reservation_models

register = template.Library()


@register.simple_tag
def is_booked(room, day):
    if day.number == 0:
        return
    try:
        date = datetime.datetime(year=day.year, month=day.month, day=day.number)
        # relation을 이용해서 reservation의 room을 가져와야 하기때문에 reservation__room = room을 선언함 
        # __를 통한 검색법으로 reservation의 room으로 BookedDay를 찾을 수 있게됨 
        reservation_models.BookedDay.objects.get(day=date, reservation__room=room)
        return True
    except reservation_models.BookedDay.DoesNotExist:
        return False
        
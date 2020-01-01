from django.db import models
from . import managers


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    # TimeStampedModel을 상속받는 모든 클래스에 적용가능
    objects = managers.CustomModelManager()


    class Meta:
        abstract = True

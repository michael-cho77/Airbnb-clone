from django.db import models


class CustomModelManager(models.Manager):
    def get_by_natural_key(self, username):
        return self.get(username = username)
    
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None
    
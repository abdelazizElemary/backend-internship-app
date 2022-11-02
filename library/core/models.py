from django.db import models
from django.db.models.functions import Now
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from model_utils.fields import (
    AutoCreatedField,
    AutoLastModifiedField,
)

now = timezone.now()


class TimeStampedModel(models.Model):
    created_at = AutoCreatedField(_('created_at'))
    modified_at = AutoLastModifiedField(_('modified_at'))

    def save(self, *args, **kwargs):
        update_fields = kwargs.get('update_fields', None)
        if update_fields:
            kwargs['update_fields'] = set(update_fields).union({'modified_at'})

        super().save(*args, **kwargs)

    class Meta:
        abstract = True
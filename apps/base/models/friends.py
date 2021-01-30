# Standard Library
import os

# Django Library
from djongo import models
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..rename_image import RenameImage
from .usercustom import PyUser

def image_path(instance, filename):
    return os.path.join('friends', str(instance.pk) + '.' + filename.rsplit('.', 1)[1])

class PyFriends(models.Model):
    '''Friends Model
    '''

    id = models.AutoField(primary_key=True)

    is_accepted = models.BooleanField(_("Accepted"), default=False)
    
    created_at = models.DateTimeField(_("Created_at"), auto_now_add = True)

    sender_id = models.ForeignKey(PyUser, related_name='Sender', on_delete=models.PROTECT, null=False, blank=False)

    receptor_id = models.ForeignKey(PyUser, related_name='Receptor', on_delete=models.PROTECT, null=False, blank=False)
    
    class Meta:
        verbose_name = _('Friend')
        verbose_name_plural = _('Friends')


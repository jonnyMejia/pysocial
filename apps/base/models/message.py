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

class PyConversation(models.Model):
    '''Conversation Model
    '''
    created_at = models.DateTimeField(_("Created_at"), auto_now_add = True)

    sender_id = models.ForeignKey(PyUser, on_delete=models.CASCADE, related_name='+', null=False, blank=False)

    receptor_id = models.ForeignKey(PyUser, on_delete=models.CASCADE, related_name='+', null=False, blank=False)
    
    class Meta:
        verbose_name = _('Conversation')
        verbose_name_plural = _('Conversations')

class PyMessage(models.Model):
    '''Conversation Model
    '''
    content = models.CharField(_("Content"), max_length=300)

    created_at = models.DateTimeField(_("Created_at"), auto_now_add = True)

    user_id = models.ForeignKey(PyUser,related_name='Me',  on_delete=models.CASCADE, null=False, blank=False)

    conversation_id = models.ForeignKey(PyConversation, related_name='Conversation',  on_delete=models.CASCADE, null=False, blank=False)
    
    class Meta:
        verbose_name = _('Message')
        verbose_name_plural = _('Messages')


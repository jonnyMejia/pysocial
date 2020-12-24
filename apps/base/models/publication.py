# Standard Library
import os

# Django Library
from djongo import models
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from ..rename_image import RenameImage
from .usercustom import PyUser

def image_path(instance, filename):
    return os.path.join('publication', str(instance.pk) + '.' + filename.rsplit('.', 1)[1])

class PyPublication(models.Model):
    '''Publication Model
    '''

    content = models.CharField(_("Content"), max_length=500)

    likes = models.IntegerField(_("Likes"), default = 0)
    
    created_at = models.DateTimeField(_("Created_at"), auto_now_add = True)

    updated_at = models.DateTimeField(_("Update_at"), auto_now = True)

    user = models.ForeignKey(PyUser, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        verbose_name = _('Publication')
        verbose_name_plural = _('Publications')

# comments = models.ArrayField(model_container=PyComment)

class PyComment(models.Model):
    '''Comments Model
    '''

    likes = models.IntegerField(_("Likes"), default = 0)

    content = models.CharField(_("Content"), max_length=300)

    created_at = models.DateTimeField(_("Created_at"), auto_now_add = True)

    user = models.ForeignKey(PyUser, on_delete=models.CASCADE, null=False, blank=False)
    
    publication = models.ForeignKey(PyPublication, on_delete=models.CASCADE, null=False, blank=False)
    
    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

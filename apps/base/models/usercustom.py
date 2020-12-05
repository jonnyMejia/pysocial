# Standard Library
import os

# Django Library
from django.contrib.auth.models import AbstractUser
from djongo import models
from django.utils.translation import ugettext_lazy as _

# Localfolder Library
from . import PyUserManager
from ..rename_image import RenameImage

def image_path(instance, filename):
    return os.path.join('avatar', str(instance.pk) + '.' + filename.rsplit('.', 1)[1])

GENDER_CHOICE = (
    ("F", "Female"),
    ('M', 'Masculine'),
    ('U', 'Undefined'),
)


class PyUser(AbstractUser):
    '''User Models
    '''
    username = None
    email = models.EmailField(_("Email"), max_length=254, null=False, db_index=True, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = PyUserManager()

    first_name = models.CharField(_("First_name"), max_length=30)
    last_name = models.CharField(_("Last_Nanme"), max_length=30, blank=True, null=True)
    # celular = models.CharField(_("Numero Móvil"), max_length=255, blank=True, null=True)
    # avatar = models.ImageField(max_length=255, storage=RenameImage(), upload_to=image_path, blank=True, null=True, default='avatar/default_avatar.png')
    
    gender =  models.CharField(_("Gender"), choices=GENDER_CHOICE, max_length=64, default='U')

    avatar = models.ImageField(max_length=255, storage=RenameImage(), upload_to=image_path, blank=True, null=True, default='avatar/default_avatar.png')

    day_of_birth = models.DateField(_("Gender"), null = True, blank = True)
    
    
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

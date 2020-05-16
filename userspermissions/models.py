from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from django.conf import settings

from . managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
   
    email = models.EmailField(_('email address'), unique=True)
    
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'
        ),
    )

    # is_superuser field provided by PermissionsMixin
    # groups field provided by PermissionsMixin
    # user_permissions field provided by PermissionsMixin

    date_joined = models.DateTimeField(
        _('date joined'), default=timezone.now
    )

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_full_name(self):
        """
        Return the full name.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return '{}'.format(self.get_full_name())

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view this app?"
        # Simplest possible answer: Yes, always
        return True


class Role(models.Model):
    name = models.CharField(max_length=30, null=False, blank=True, unique=True)

    status = models.BooleanField(
        _('status'),
        default=False,
        help_text=_(
            'If disabled, this role will be removed from all users.'
        ),
    )
    
    desk_access = models.BooleanField(
        _('desk access'),
        default=True,
        help_text=_(
            'Designates whether the Role can have module access.'
        ),
    )

    date_created = models.DateTimeField(
        _('date created'), default=timezone.now
    )

    '''created_by = models.ForeignKey(
        CustomUser,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )'''

    def __str__(self):
        return str(self.name)    

class RoleProfile(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True)
    roles = models.ManyToManyField(Role)

    date_created = models.DateTimeField(
        _('date created'), default=timezone.now
    )

    def __str__(self):
        return str(self.name)


class ActivityLog(models.Model):
    session_key = models.CharField(max_length=1024, null=False, blank=True)
    path = models.CharField(max_length=1024, null=False, blank=True)
    method = models.CharField(max_length=8, null=False, blank=True)
    ip_address = models.CharField(max_length=45, null=False, blank=True)
    timestamp = models.DateTimeField(null=False, blank=True)

    def __str__(self):
        return str(self.session_key)



class AccessLog(models.Model):
    sys_id = models.AutoField(primary_key=True, null=False, blank=True)
    session_key = models.CharField(max_length=1024, null=False, blank=True)
    path = models.CharField(max_length=1024, null=False, blank=True)
    data = models.TextField(null=True, blank=True)
    ip_address = models.CharField(max_length=45, null=False, blank=True)
    referrer = models.CharField(max_length=512, null=True, blank=True)
    timestamp = models.DateTimeField(null=False, blank=True)

    def __str__(self):
        return str(self.sys_id)

